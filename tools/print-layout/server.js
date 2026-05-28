const http = require("http");
const fs = require("fs");
const path = require("path");
const os = require("os");
const { spawn } = require("child_process");

const repoRoot = path.resolve(__dirname, "..", "..");
const publicDir = path.join(__dirname, "public");
const seriesDir = path.join(repoRoot, "series");
const port = Number(process.env.PORT || 4173);
const imageExtensions = new Set([".png", ".jpg", ".jpeg", ".webp"]);

function bundledPython() {
  const candidate = path.join(
    os.homedir(),
    ".cache",
    "codex-runtimes",
    "codex-primary-runtime",
    "dependencies",
    "python",
    "python.exe",
  );
  return fs.existsSync(candidate) ? candidate : "python";
}

function isInside(parent, child) {
  const relative = path.relative(parent, child);
  return relative === "" || (!relative.startsWith("..") && !path.isAbsolute(relative));
}

function repoPath(relativePath) {
  const resolved = path.resolve(repoRoot, relativePath || "");
  if (!isInside(repoRoot, resolved)) {
    throw new Error("저장소 밖의 경로는 사용할 수 없습니다.");
  }
  return resolved;
}

function leadingNumber(filename) {
  const match = filename.match(/^(\d+)/);
  return match ? Number(match[1]) : null;
}

function isImageFile(filePath) {
  return fs.statSync(filePath).isFile() && imageExtensions.has(path.extname(filePath).toLowerCase());
}

function discoverBookFolder(folder) {
  const entries = fs.existsSync(folder) ? fs.readdirSync(folder) : [];
  const images = entries
    .map((name) => path.join(folder, name))
    .filter((filePath) => isImageFile(filePath))
    .map((filePath) => ({ filePath, number: leadingNumber(path.basename(filePath)) }))
    .filter((item) => item.number !== null)
    .sort((a, b) => a.number - b.number || path.basename(a.filePath).localeCompare(path.basename(b.filePath), "ko"));

  const cover = images.find((item) => item.number === 0);
  const bodyPages = images.filter((item) => item.number > 0);
  if (!cover && bodyPages.length === 0) return null;

  const relativeFolder = path.relative(repoRoot, folder).replaceAll(path.sep, "/");
  return {
    id: relativeFolder,
    title: relativeFolder.replaceAll("/", " / "),
    folder: relativeFolder,
    available: Boolean(cover && bodyPages.length),
    unavailableReason: !cover ? "표지 이미지가 없습니다." : bodyPages.length ? "" : "본문 페이지가 없습니다.",
    cover: cover ? path.relative(repoRoot, cover.filePath).replaceAll(path.sep, "/") : null,
    bodyPages: bodyPages.map((item) => path.relative(repoRoot, item.filePath).replaceAll(path.sep, "/")),
    bodyPageCount: bodyPages.length,
    bodySheetCount: Math.ceil(bodyPages.length / 2),
  };
}

function walkForBooks(folder, depth = 0) {
  if (!fs.existsSync(folder) || depth > 5) return [];
  const current = discoverBookFolder(folder);
  const childBooks = fs
    .readdirSync(folder, { withFileTypes: true })
    .filter((entry) => entry.isDirectory() && entry.name !== "print-output")
    .flatMap((entry) => walkForBooks(path.join(folder, entry.name), depth + 1));
  return current ? [current, ...childBooks] : childBooks;
}

function sendJson(res, status, payload) {
  const body = JSON.stringify(payload);
  res.writeHead(status, {
    "content-type": "application/json; charset=utf-8",
    "content-length": Buffer.byteLength(body),
  });
  res.end(body);
}

function sendText(res, status, text) {
  res.writeHead(status, { "content-type": "text/plain; charset=utf-8" });
  res.end(text);
}

function serveStatic(req, res, url) {
  const pathname = url.pathname === "/" ? "/index.html" : url.pathname;
  const filePath = path.resolve(publicDir, `.${pathname}`);
  if (!isInside(publicDir, filePath) || !fs.existsSync(filePath) || !fs.statSync(filePath).isFile()) {
    sendText(res, 404, "Not found");
    return;
  }
  const extension = path.extname(filePath).toLowerCase();
  const contentTypes = {
    ".html": "text/html; charset=utf-8",
    ".css": "text/css; charset=utf-8",
    ".js": "text/javascript; charset=utf-8",
  };
  res.writeHead(200, { "content-type": contentTypes[extension] || "application/octet-stream" });
  fs.createReadStream(filePath).pipe(res);
}

function serveImage(res, relativePath) {
  const filePath = repoPath(relativePath);
  if (!isImageFile(filePath)) {
    sendText(res, 404, "Image not found");
    return;
  }
  const extension = path.extname(filePath).toLowerCase();
  const contentType = extension === ".webp" ? "image/webp" : extension === ".jpg" || extension === ".jpeg" ? "image/jpeg" : "image/png";
  res.writeHead(200, { "content-type": contentType });
  fs.createReadStream(filePath).pipe(res);
}

function readJsonBody(req) {
  return new Promise((resolve, reject) => {
    let data = "";
    req.on("data", (chunk) => {
      data += chunk;
      if (data.length > 1024 * 1024) {
        reject(new Error("요청이 너무 큽니다."));
        req.destroy();
      }
    });
    req.on("end", () => {
      try {
        resolve(data ? JSON.parse(data) : {});
      } catch (error) {
        reject(error);
      }
    });
    req.on("error", reject);
  });
}

function generatePdf(folder, target, layout, excludedPages = []) {
  return new Promise((resolve, reject) => {
    const absoluteFolder = repoPath(folder);
    const args = ["-m", "tools.print_layout.pdf_layout", absoluteFolder, "--target", target, "--layout", layout];
    for (const page of excludedPages) {
      args.push("--exclude", repoPath(page));
    }
    const child = spawn(bundledPython(), args, {
      cwd: repoRoot,
      env: { ...process.env, PYTHONIOENCODING: "utf-8", PYTHONUTF8: "1" },
      windowsHide: true,
    });
    let stdout = "";
    let stderr = "";
    child.stdout.on("data", (chunk) => {
      stdout += chunk.toString();
    });
    child.stderr.on("data", (chunk) => {
      stderr += chunk.toString();
    });
    child.on("error", reject);
    child.on("close", (code) => {
      if (code !== 0) {
        reject(new Error(stderr || stdout || `PDF 생성 실패: exit ${code}`));
        return;
      }
      try {
        resolve(JSON.parse(stdout));
      } catch (error) {
        reject(new Error(`PDF 결과를 읽을 수 없습니다: ${stdout}`));
      }
    });
  });
}

async function handleRequest(req, res) {
  try {
    const url = new URL(req.url, `http://${req.headers.host}`);
    if (url.pathname === "/api/books") {
      sendJson(res, 200, { books: walkForBooks(seriesDir) });
      return;
    }
    if (url.pathname === "/image") {
      serveImage(res, url.searchParams.get("path"));
      return;
    }
    if (url.pathname === "/api/generate" && req.method === "POST") {
      const body = await readJsonBody(req);
      const target = ["cover", "body", "both", "booklet"].includes(body.target) ? body.target : "both";
      const layout = ["landscape", "portrait"].includes(body.layout) ? body.layout : "landscape";
      const excludedPages = Array.isArray(body.excludedPages) ? body.excludedPages : [];
      const result = await generatePdf(body.folder, target, layout, excludedPages);
      sendJson(res, 200, { result });
      return;
    }
    serveStatic(req, res, url);
  } catch (error) {
    sendJson(res, 500, { error: error.message || String(error) });
  }
}

const server = http.createServer(handleRequest);
server.listen(port, () => {
  console.log(`Print layout web tool: http://localhost:${port}`);
});
