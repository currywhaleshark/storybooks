const http = require("http");
const fs = require("fs");
const path = require("path");
const os = require("os");
const crypto = require("crypto");
const { spawn } = require("child_process");

const repoRoot = path.resolve(__dirname, "..", "..");
const publicDir = path.join(__dirname, "public");
const seriesDir = path.join(repoRoot, "series");
const rendererScript = path.join(
  repoRoot,
  "series",
  "sherlock-fin-deep-city",
  "videos",
  "누가_먼저_왔을까_tts_google",
  "make_tts_video.py",
);
const port = Number(process.env.PORT || 4174);
const imageExtensions = new Set([".png", ".jpg", ".jpeg", ".webp"]);
const jobs = new Map();

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

function toRepoPath(absolutePath) {
  return path.relative(repoRoot, absolutePath).replaceAll(path.sep, "/");
}

function isImageFile(filePath) {
  return fs.statSync(filePath).isFile() && imageExtensions.has(path.extname(filePath).toLowerCase());
}

function leadingNumber(filename) {
  const match = filename.match(/^(\d+)/);
  return match ? Number(match[1]) : Number.MAX_SAFE_INTEGER;
}

function sortedImages(folder) {
  if (!fs.existsSync(folder)) return [];
  return fs
    .readdirSync(folder)
    .map((name) => path.join(folder, name))
    .filter((filePath) => fs.existsSync(filePath) && isImageFile(filePath))
    .sort((a, b) => leadingNumber(path.basename(a)) - leadingNumber(path.basename(b)) || path.basename(a).localeCompare(path.basename(b), "ko"));
}

function discoverBookFolder(folder) {
  const images = sortedImages(folder)
    .map((filePath) => ({ filePath, number: leadingNumber(path.basename(filePath)) }))
    .filter((item) => item.number !== Number.MAX_SAFE_INTEGER);

  const cover = images.find((item) => item.number === 0);
  const bodyPages = images.filter((item) => item.number > 0);
  if (!cover && bodyPages.length === 0) return null;

  const seriesRoot = seriesRootForEpisodeFolder(folder);
  const episodeFolder = path.basename(folder) === "final" ? path.dirname(folder) : folder;
  const episodeTitle = path.basename(episodeFolder);
  const seriesName = seriesRoot ? path.basename(seriesRoot) : "";
  const imageFiles = images.map((item) => item.filePath);
  return {
    id: toRepoPath(folder),
    title: episodeTitle,
    series: seriesName,
    finalFolder: toRepoPath(folder),
    imageCount: imageFiles.length,
    images: imageFiles.map(toRepoPath),
    scripts: seriesRoot ? scriptCandidates(seriesRoot, episodeTitle) : [],
    defaultOutputDir: toRepoPath(path.join(seriesRoot || repoRoot, "videos", `${episodeTitle}_tts_app`)),
  };
}

function findBookFolders(folder, depth = 0) {
  if (!fs.existsSync(folder) || depth > 7) return [];
  const entries = fs.readdirSync(folder, { withFileTypes: true });
  const current = discoverBookFolder(folder);
  const folders = [];
  for (const entry of entries) {
    if (!entry.isDirectory()) continue;
    if (["audio", "segments", "work", "drafts", "rejected", "print-output"].includes(entry.name)) continue;
    if (/^batch(?:_|$)/i.test(entry.name)) continue;
    if (current && entry.name === "final") continue;
    folders.push(...findBookFolders(path.join(folder, entry.name), depth + 1));
  }
  return current ? [current, ...folders] : folders;
}

function seriesRootForEpisodeFolder(episodeFolder) {
  const parts = episodeFolder.split(path.sep);
  const imagesIndex = parts.lastIndexOf("images");
  if (imagesIndex <= 0) return null;
  return parts.slice(0, imagesIndex).join(path.sep);
}

function scriptCandidates(seriesRoot, episodeTitle) {
  const docsEpisodeDir = path.join(seriesRoot, "docs", "episodes");
  const candidates = [];
  if (!fs.existsSync(docsEpisodeDir)) return candidates;
  const normalizedTitle = episodeTitle.replaceAll("_", "").toLowerCase();
  for (const name of fs.readdirSync(docsEpisodeDir)) {
    if (path.extname(name).toLowerCase() !== ".md") continue;
    const absolutePath = path.join(docsEpisodeDir, name);
    const normalizedName = path.basename(name, ".md").replaceAll("_", "").toLowerCase();
    candidates.push({
      path: toRepoPath(absolutePath),
      name,
      likely: normalizedName.includes(normalizedTitle) || normalizedTitle.includes(normalizedName),
    });
  }
  return candidates.sort((a, b) => {
    const aTts = /(?:^|[_-])tts(?:[_-]|\.|$)/i.test(a.name);
    const bTts = /(?:^|[_-])tts(?:[_-]|\.|$)/i.test(b.name);
    return Number(b.likely) - Number(a.likely) || Number(bTts) - Number(aTts) || a.name.localeCompare(b.name, "ko");
  });
}

function discoverEpisodes() {
  return findBookFolders(seriesDir);
}

function stripOuterQuotes(text) {
  let result = text.trim();
  result = result.replace(/^["“]+/, "").replace(/["”]+$/, "");
  return result.trim();
}

function cleanExtractedText(text) {
  return stripOuterQuotes(text)
    .replace(/\r\n/g, "\n")
    .replace(/\n{3,}/g, "\n\n")
    .trim();
}

function extractTextBlocks(markdown) {
  const blocks = [];
  const pageTextPattern = /###\s*페이지\s*텍스트[\s\S]*?```text\s*\n([\s\S]*?)```/g;
  let match;
  while ((match = pageTextPattern.exec(markdown))) {
    blocks.push(cleanExtractedText(match[1]));
  }
  if (blocks.length) return blocks;

  const fencedTextPattern = /(?:^|\n)Text:\s*\n```text\s*\n([\s\S]*?)```/g;
  while ((match = fencedTextPattern.exec(markdown))) {
    blocks.push(cleanExtractedText(match[1]));
  }
  if (blocks.length) return blocks;

  const quotedTextPattern = /(?:^|\n)Text:\s*\n([“"][\s\S]*?[”"])(?=\n\s*(?:---|##|###|$))/g;
  while ((match = quotedTextPattern.exec(markdown))) {
    blocks.push(cleanExtractedText(match[1]));
  }
  return blocks;
}

function buildScriptMarkdown(title, images, texts) {
  const lines = [`# ${title} TTS 원고`, ""];
  images.forEach((imagePath, index) => {
    lines.push(`## ${path.basename(imagePath)}`, "");
    lines.push((texts[index] || "").trim(), "");
  });
  return lines.join("\n").trimEnd() + "\n";
}

function outputPathForVideo(outputDir, outputName) {
  const safeName = (outputName || "storybook_tts_video.mp4").replace(/[\\/:*?"<>|]/g, "_");
  return path.join(outputDir, safeName.toLowerCase().endsWith(".mp4") ? safeName : `${safeName}.mp4`);
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
  if (!fs.existsSync(filePath) || !isImageFile(filePath)) {
    sendText(res, 404, "Image not found");
    return;
  }
  const extension = path.extname(filePath).toLowerCase();
  const contentType = extension === ".webp" ? "image/webp" : extension === ".jpg" || extension === ".jpeg" ? "image/jpeg" : "image/png";
  res.writeHead(200, { "content-type": contentType });
  fs.createReadStream(filePath).pipe(res);
}

function serveMedia(res, relativePath) {
  const filePath = repoPath(relativePath);
  if (!fs.existsSync(filePath) || !fs.statSync(filePath).isFile()) {
    sendText(res, 404, "Media not found");
    return;
  }
  const extension = path.extname(filePath).toLowerCase();
  const contentTypes = {
    ".mp3": "audio/mpeg",
    ".wav": "audio/wav",
    ".mp4": "video/mp4",
  };
  res.writeHead(200, { "content-type": contentTypes[extension] || "application/octet-stream" });
  fs.createReadStream(filePath).pipe(res);
}

function readJsonBody(req) {
  return new Promise((resolve, reject) => {
    let data = "";
    req.on("data", (chunk) => {
      data += chunk;
      if (data.length > 2 * 1024 * 1024) {
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

function saveScript({ episode, texts, outputDir }) {
  const finalFolder = repoPath(episode.finalFolder);
  const targetOutputDir = repoPath(outputDir || episode.defaultOutputDir);
  fs.mkdirSync(targetOutputDir, { recursive: true });
  const images = sortedImages(finalFolder).map(toRepoPath);
  const script = buildScriptMarkdown(episode.title, images, texts);
  const scriptPath = path.join(targetOutputDir, "tts_script.md");
  fs.writeFileSync(scriptPath, script, "utf8");
  return { scriptPath: toRepoPath(scriptPath), outputDir: toRepoPath(targetOutputDir), script };
}

function startRenderJob({ episode, texts, settings }) {
  const saved = saveScript({ episode, texts, outputDir: settings.outputDir || episode.defaultOutputDir });
  const outputDir = repoPath(saved.outputDir);
  const outputVideo = outputPathForVideo(outputDir, settings.outputName);
  const args = [
    rendererScript,
    "--episode-dir",
    repoPath(episode.finalFolder),
    "--script-path",
    repoPath(saved.scriptPath),
    "--out-dir",
    outputDir,
    "--tts",
    settings.tts || "gemini",
    "--speaking-rate",
    String(settings.speakingRate ?? 1),
    "--pitch",
    String(settings.pitch ?? 0),
    "--page-gap",
    String(settings.pageGap ?? 0.8),
    "--output",
    path.basename(outputVideo),
  ];

  if (settings.tts === "cloud") {
    args.push("--cloud-voice", settings.cloudVoice || "ko-KR-Chirp3-HD-Kore");
  }
  if ((settings.tts || "gemini") === "gemini") {
    args.push("--gemini-model", settings.geminiModel || "gemini-2.5-flash-tts");
    args.push("--gemini-voice", settings.geminiVoice || "Kore");
    args.push("--gemini-prompt", settings.geminiPrompt || "");
  }

  const id = crypto.randomUUID();
  const job = {
    id,
    status: "running",
    startedAt: new Date().toISOString(),
    finishedAt: null,
    stdout: "",
    stderr: "",
    scriptPath: saved.scriptPath,
    outputPath: toRepoPath(outputVideo),
    command: `${bundledPython()} ${args.map((arg) => JSON.stringify(String(arg))).join(" ")}`,
  };
  jobs.set(id, job);

  const child = spawn(bundledPython(), args, {
    cwd: repoRoot,
    env: { ...process.env, PYTHONIOENCODING: "utf-8", PYTHONUTF8: "1" },
    windowsHide: true,
  });
  child.stdout.on("data", (chunk) => {
    job.stdout += chunk.toString();
  });
  child.stderr.on("data", (chunk) => {
    job.stderr += chunk.toString();
  });
  child.on("error", (error) => {
    job.status = "failed";
    job.stderr += `\n${error.message}`;
    job.finishedAt = new Date().toISOString();
  });
  child.on("close", (code) => {
    job.status = code === 0 ? "complete" : "failed";
    job.exitCode = code;
    job.finishedAt = new Date().toISOString();
  });

  return job;
}

function runVoiceList(languageCode) {
  return new Promise((resolve, reject) => {
    const child = spawn(
      bundledPython(),
      [rendererScript, "--list-cloud-voices", "--cloud-language", languageCode || "ko-KR"],
      { cwd: repoRoot, env: { ...process.env, PYTHONIOENCODING: "utf-8", PYTHONUTF8: "1" }, windowsHide: true },
    );
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
        reject(new Error(stderr || `voice list failed: ${code}`));
        return;
      }
      const voices = stdout
        .split(/\r?\n/)
        .map((line) => line.trim())
        .filter(Boolean)
        .map((line) => {
          const [name, gender, sampleRate, languages] = line.split("\t");
          return { name, gender, sampleRate, languages };
        });
      resolve(voices);
    });
  });
}

function createVoiceSample(settings) {
  return new Promise((resolve, reject) => {
    const sampleDir = path.join(repoRoot, "tools", "tts-video", "runtime", "samples");
    fs.mkdirSync(sampleDir, { recursive: true });
    const samplePath = path.join(sampleDir, `${crypto.randomUUID()}.mp3`);
    const args = [
      rendererScript,
      "--tts",
      settings.tts || "gemini",
      "--speaking-rate",
      String(settings.speakingRate ?? 1),
      "--pitch",
      String(settings.pitch ?? 0),
      "--sample-text",
      settings.sampleText || "포포는 안 졸려요. 낮잠은 신나게 놀 힘을 모으는 시간이래요.",
      "--sample-output",
      samplePath,
    ];
    if (settings.tts === "cloud") {
      args.push("--cloud-voice", settings.cloudVoice || "ko-KR-Chirp3-HD-Kore");
    }
    if ((settings.tts || "gemini") === "gemini") {
      args.push("--gemini-model", settings.geminiModel || "gemini-2.5-flash-tts");
      args.push("--gemini-voice", settings.geminiVoice || "Kore");
      args.push("--gemini-prompt", settings.geminiPrompt || "");
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
        reject(new Error(stderr || stdout || `sample failed: ${code}`));
        return;
      }
      resolve({ path: toRepoPath(samplePath), url: `/media?path=${encodeURIComponent(toRepoPath(samplePath))}` });
    });
  });
}

async function handleRequest(req, res) {
  try {
    const url = new URL(req.url, `http://${req.headers.host}`);
    if (url.pathname === "/api/episodes") {
      sendJson(res, 200, { episodes: discoverEpisodes() });
      return;
    }
    if (url.pathname === "/image") {
      serveImage(res, url.searchParams.get("path"));
      return;
    }
    if (url.pathname === "/media") {
      serveMedia(res, url.searchParams.get("path"));
      return;
    }
    if (url.pathname === "/api/extract" && req.method === "POST") {
      const body = await readJsonBody(req);
      const sourcePath = repoPath(body.sourcePath);
      const markdown = fs.readFileSync(sourcePath, "utf8");
      sendJson(res, 200, { texts: extractTextBlocks(markdown) });
      return;
    }
    if (url.pathname === "/api/save-script" && req.method === "POST") {
      const body = await readJsonBody(req);
      const saved = saveScript(body);
      sendJson(res, 200, saved);
      return;
    }
    if (url.pathname === "/api/render" && req.method === "POST") {
      const body = await readJsonBody(req);
      const job = startRenderJob(body);
      sendJson(res, 200, { job });
      return;
    }
    if (url.pathname.startsWith("/api/jobs/")) {
      const id = decodeURIComponent(url.pathname.slice("/api/jobs/".length));
      const job = jobs.get(id);
      if (!job) {
        sendJson(res, 404, { error: "작업을 찾을 수 없습니다." });
        return;
      }
      sendJson(res, 200, { job });
      return;
    }
    if (url.pathname === "/api/voices") {
      const voices = await runVoiceList(url.searchParams.get("language") || "ko-KR");
      sendJson(res, 200, { voices });
      return;
    }
    if (url.pathname === "/api/sample" && req.method === "POST") {
      const body = await readJsonBody(req);
      const sample = await createVoiceSample(body.settings || {});
      sendJson(res, 200, { sample });
      return;
    }
    serveStatic(req, res, url);
  } catch (error) {
    sendJson(res, 500, { error: error.message || String(error) });
  }
}

const server = http.createServer(handleRequest);
server.listen(port, () => {
  console.log(`TTS video web tool: http://localhost:${port}`);
});
