const state = {
  books: [],
  selected: null,
  spreadIndex: 0,
};

const bookSelect = document.querySelector("#bookSelect");
const summary = document.querySelector("#summary");
const coverStage = document.querySelector("#coverStage");
const sheetStage = document.querySelector("#sheetStage");
const spreadLabel = document.querySelector("#spreadLabel");
const prevButton = document.querySelector("#prevButton");
const nextButton = document.querySelector("#nextButton");
const coverButton = document.querySelector("#coverButton");
const bodyButton = document.querySelector("#bodyButton");
const bothButton = document.querySelector("#bothButton");
const statusBox = document.querySelector("#status");

function imageUrl(path) {
  return `/image?path=${encodeURIComponent(path)}`;
}

function setStatus(message, isError = false) {
  statusBox.textContent = message;
  statusBox.classList.toggle("error", isError);
}

function currentSpreads() {
  if (!state.selected) return [];
  const pages = state.selected.bodyPages;
  const spreads = [];
  for (let index = 0; index < pages.length; index += 2) {
    spreads.push([pages[index], pages[index + 1] || null]);
  }
  return spreads;
}

function renderCover() {
  coverStage.innerHTML = "";
  const page = document.createElement("div");
  page.className = "cover-page";
  if (state.selected?.cover) {
    const image = document.createElement("img");
    image.src = imageUrl(state.selected.cover);
    image.alt = "표지";
    page.append(image);
  } else {
    page.textContent = "표지 없음";
  }
  coverStage.append(page);
}

function renderBody() {
  sheetStage.innerHTML = "";
  const spreads = currentSpreads();
  const spread = spreads[state.spreadIndex] || [null, null];
  const sheet = document.createElement("div");
  sheet.className = "sheet";

  for (const pagePath of spread) {
    const slot = document.createElement("div");
    slot.className = pagePath ? "slot" : "slot blank";
    if (pagePath) {
      const image = document.createElement("img");
      image.src = imageUrl(pagePath);
      image.alt = pagePath.split("/").pop();
      slot.append(image);
    } else {
      slot.textContent = "빈 칸";
    }
    sheet.append(slot);
  }

  sheetStage.append(sheet);
  spreadLabel.textContent = spreads.length ? `${state.spreadIndex + 1} / ${spreads.length}` : "0 / 0";
  prevButton.disabled = state.spreadIndex <= 0;
  nextButton.disabled = state.spreadIndex >= spreads.length - 1;
}

function renderSelectedBook() {
  const book = state.selected;
  const disabled = !book?.available;
  coverButton.disabled = disabled;
  bodyButton.disabled = disabled;
  bothButton.disabled = disabled;
  prevButton.disabled = true;
  nextButton.disabled = true;

  if (!book) {
    summary.textContent = "사용 가능한 책 폴더가 없습니다.";
    coverStage.innerHTML = "";
    sheetStage.innerHTML = "";
    setStatus("series 폴더 아래에서 00_표지.png와 번호가 붙은 본문 이미지를 찾지 못했습니다.", true);
    return;
  }

  summary.textContent = `${book.bodyPageCount}쪽, 인쇄 ${book.bodySheetCount}장`;
  state.spreadIndex = Math.min(state.spreadIndex, Math.max(book.bodySheetCount - 1, 0));
  renderCover();
  renderBody();

  if (book.available) {
    setStatus(`선택됨: ${book.folder}`);
  } else {
    setStatus(book.unavailableReason || "이 폴더는 인쇄할 수 없습니다.", true);
  }
}

function selectBook(folder) {
  state.selected = state.books.find((book) => book.folder === folder) || state.books[0] || null;
  state.spreadIndex = 0;
  if (state.selected) bookSelect.value = state.selected.folder;
  renderSelectedBook();
}

async function loadBooks() {
  try {
    const response = await fetch("/api/books");
    const data = await response.json();
    state.books = data.books || [];
    bookSelect.innerHTML = "";
    for (const book of state.books) {
      const option = document.createElement("option");
      option.value = book.folder;
      option.textContent = book.title;
      option.disabled = !book.available;
      bookSelect.append(option);
    }
    selectBook(state.books.find((book) => book.available)?.folder);
  } catch (error) {
    setStatus(`책 목록을 불러오지 못했습니다.\n${error.message}`, true);
  }
}

async function generate(target) {
  if (!state.selected) return;
  setStatus("PDF 생성 중입니다...");
  coverButton.disabled = true;
  bodyButton.disabled = true;
  bothButton.disabled = true;
  try {
    const response = await fetch("/api/generate", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({ folder: state.selected.folder, target }),
    });
    const data = await response.json();
    if (!response.ok || data.error) {
      throw new Error(data.error || "PDF 생성 실패");
    }
    const result = data.result;
    const lines = ["PDF 생성 완료"];
    if (result.cover_pdf) lines.push(`표지: ${result.cover_pdf}`);
    if (result.body_pdf) lines.push(`본문: ${result.body_pdf}`);
    setStatus(lines.join("\n"));
  } catch (error) {
    setStatus(error.message, true);
  } finally {
    renderSelectedBook();
  }
}

bookSelect.addEventListener("change", () => selectBook(bookSelect.value));
prevButton.addEventListener("click", () => {
  state.spreadIndex = Math.max(0, state.spreadIndex - 1);
  renderBody();
});
nextButton.addEventListener("click", () => {
  state.spreadIndex = Math.min(currentSpreads().length - 1, state.spreadIndex + 1);
  renderBody();
});
coverButton.addEventListener("click", () => generate("cover"));
bodyButton.addEventListener("click", () => generate("body"));
bothButton.addEventListener("click", () => generate("both"));

loadBooks();
