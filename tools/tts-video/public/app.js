const state = {
  episodes: [],
  selected: null,
  texts: [],
  audioReview: null,
  jobId: null,
  jobKind: null,
  pollTimer: null,
  ttsPresets: null,
  activeScriptTextarea: null,
  directScriptContent: "",
  directScriptLabel: "",
};

const TAG_TRANSLATIONS = Object.freeze({
  "[amazed]": "놀라워하며",
  "[awkwardly]": "어색하게",
  "[brightly]": "밝게",
  "[calmly]": "차분하게",
  "[cheerfully]": "명랑하게",
  "[clearly]": "또렷하게",
  "[crying]": "울먹이며",
  "[curious]": "궁금한 듯",
  "[excited]": "신난 목소리로",
  "[excitedly]": "신나게",
  "[firmly]": "단호하게",
  "[formally]": "정중하게",
  "[frustrated]": "답답해하며",
  "[gasp]": "숨을 들이켜며",
  "[gently]": "부드럽게",
  "[giggles]": "킥킥 웃으며",
  "[laughs]": "웃으며",
  "[mischievously]": "장난스럽게",
  "[mysteriously]": "신비롭게",
  "[nervously]": "긴장해서",
  "[playfully]": "장난치듯",
  "[proudly]": "뿌듯하게",
  "[quietly]": "조용히",
  "[reassuringly]": "안심시키듯",
  "[relieved]": "안도하며",
  "[reluctantly]": "마지못해",
  "[serious]": "진지하게",
  "[sleepily]": "졸린 듯",
  "[softly]": "부드럽고 작게",
  "[surprised]": "놀라며",
  "[thoughtfully]": "생각에 잠겨",
  "[tired]": "지친 듯",
  "[trembling]": "떨리는 목소리로",
  "[very fast]": "매우 빠르게",
  "[very slow]": "매우 느리게",
  "[warmly]": "따뜻하게",
  "[whisper]": "속삭이며",
  "[whispers]": "속삭이며",
  "[yawn]": "하품하며",
  "[pause]": "잠깐 쉬기",
  "[short pause]": "짧게 쉬기",
  "[long pause]": "길게 쉬기",
  "[sigh]": "한숨 쉬며",
});

const episodeSelect = document.querySelector("#episodeSelect");
const scriptSelect = document.querySelector("#scriptSelect");
const reloadButton = document.querySelector("#reloadButton");
const extractButton = document.querySelector("#extractButton");
const extractPasteButton = document.querySelector("#extractPasteButton");
const saveButton = document.querySelector("#saveButton");
const renderButton = document.querySelector("#renderButton");
const reviewAudioButton = document.querySelector("#reviewAudioButton");
const voiceButton = document.querySelector("#voiceButton");
const sampleButton = document.querySelector("#sampleButton");
const ttsSelect = document.querySelector("#ttsSelect");
const geminiModel = document.querySelector("#geminiModel");
const geminiVoice = document.querySelector("#geminiVoice");
const cloudVoice = document.querySelector("#cloudVoice");
const stylePrompt = document.querySelector("#stylePrompt");
const speedInput = document.querySelector("#speedInput");
const pitchInput = document.querySelector("#pitchInput");
const gapInput = document.querySelector("#gapInput");
const outputName = document.querySelector("#outputName");
const sampleText = document.querySelector("#sampleText");
const sampleAudio = document.querySelector("#sampleAudio");
const speedValue = document.querySelector("#speedValue");
const pitchValue = document.querySelector("#pitchValue");
const gapValue = document.querySelector("#gapValue");
const summary = document.querySelector("#summary");
const pageCount = document.querySelector("#pageCount");
const pageStrip = document.querySelector("#pageStrip");
const scriptEditor = document.querySelector("#scriptEditor");
const scriptStatus = document.querySelector("#scriptStatus");
const statusLog = document.querySelector("#statusLog");
const jobState = document.querySelector("#jobState");
const scriptFileInput = document.querySelector("#scriptFileInput");
const scriptPaste = document.querySelector("#scriptPaste");
const manualAudioInput = document.querySelector("#manualAudioInput");
const manualAudioStatus = document.querySelector("#manualAudioStatus");
const audioReviewStatus = document.querySelector("#audioReviewStatus");
const audioReviewList = document.querySelector("#audioReviewList");
const presetSeriesLabel = document.querySelector("#presetSeriesLabel");
const presetCharacterSelect = document.querySelector("#presetCharacterSelect");
const presetDescription = document.querySelector("#presetDescription");
const presetTagList = document.querySelector("#presetTagList");

function imageUrl(path) {
  return `/image?path=${encodeURIComponent(path)}`;
}

function setStatus(message, isError = false) {
  statusLog.textContent = message;
  statusLog.classList.toggle("error", isError);
}

function appendStatus(message) {
  statusLog.textContent = `${statusLog.textContent.trim()}\n${message}`.trim();
  statusLog.scrollTop = statusLog.scrollHeight;
}

function selectedEpisode() {
  return state.episodes.find((episode) => episode.finalFolder === episodeSelect.value) || null;
}

function setButtonsDisabled(disabled) {
  extractButton.disabled = disabled;
  saveButton.disabled = disabled;
  renderButton.disabled = disabled;
  reviewAudioButton.disabled = disabled || ttsSelect.value === "manual";
  voiceButton.disabled = disabled;
}

function renderSettingsVisibility() {
  const tts = ttsSelect.value;
  document.querySelectorAll(".gemini-only").forEach((node) => {
    node.style.display = tts === "gemini" ? "" : "none";
  });
  document.querySelectorAll(".cloud-only").forEach((node) => {
    node.style.display = tts === "cloud" ? "" : "none";
  });
  document.querySelectorAll(".manual-only").forEach((node) => {
    node.style.display = tts === "manual" ? "" : "none";
  });
  sampleButton.disabled = tts === "manual";
  reviewAudioButton.disabled = tts === "manual";
  renderPresetPalette();
}

function updateRangeLabels() {
  speedValue.textContent = Number(speedInput.value).toFixed(2);
  pitchValue.textContent = Number(pitchInput.value).toFixed(1);
  gapValue.textContent = `${Number(gapInput.value).toFixed(1)}초`;
}

function renderEpisode() {
  state.selected = selectedEpisode();
  state.texts = [];
  state.audioReview = null;
  state.ttsPresets = null;
  state.activeScriptTextarea = null;
  state.directScriptContent = "";
  state.directScriptLabel = "";
  scriptEditor.innerHTML = "";

  if (!state.selected) {
    summary.textContent = "사용 가능한 final 이미지 폴더가 없습니다.";
    pageCount.textContent = "0장";
    pageStrip.innerHTML = "";
    renderPresetPalette();
    return;
  }

  summary.textContent = `${state.selected.series} / ${state.selected.title}`;
  pageCount.textContent = `${state.selected.imageCount}장`;
  outputName.value = `${state.selected.title}_gemini_tts.mp4`;

  scriptSelect.innerHTML = "";
  for (const script of state.selected.scripts) {
    const option = document.createElement("option");
    option.value = script.path;
    option.textContent = script.likely ? `추천: ${script.name}` : script.name;
    scriptSelect.append(option);
  }
  if (!state.selected.scripts.length) {
    const option = document.createElement("option");
    option.value = "";
    option.textContent = "대본 후보 없음";
    scriptSelect.append(option);
  }

  pageStrip.innerHTML = "";
  for (const image of state.selected.images) {
    const card = document.createElement("div");
    card.className = "page-card";
    const img = document.createElement("img");
    img.src = imageUrl(image);
    img.alt = image.split("/").pop();
    const label = document.createElement("span");
    label.textContent = image.split("/").pop();
    card.append(img, label);
    pageStrip.append(card);
  }

  scriptStatus.textContent = "대본 추출 전";
  renderAudioReview();
  renderPresetPalette();
  loadTtsPresets().catch((error) => {
    state.ttsPresets = null;
    renderPresetPalette();
    setStatus(error.message, true);
  });
  setStatus("대본 파일을 선택한 뒤 추출하세요.");
}

function renderScriptEditor() {
  scriptEditor.innerHTML = "";
  const images = state.selected?.images || [];
  state.texts = images.map((_, index) => state.texts[index] || "");
  images.forEach((image, index) => {
    const row = document.createElement("div");
    row.className = "script-page";
    const label = document.createElement("label");
    const name = document.createElement("span");
    name.textContent = image.split("/").pop();
    const count = document.createElement("span");
    count.textContent = `${(state.texts[index] || "").length}자`;
    const textarea = document.createElement("textarea");
    textarea.value = state.texts[index] || "";
    textarea.addEventListener("focus", () => {
      state.activeScriptTextarea = textarea;
    });
    textarea.addEventListener("input", () => {
      state.texts[index] = textarea.value;
      count.textContent = `${textarea.value.length}자`;
      invalidateAudioReview("대본이 변경되어 검수 음성을 다시 생성해야 합니다.");
    });
    label.append(name, count);
    row.append(label, textarea);
    scriptEditor.append(row);
  });
  scriptStatus.textContent = `${state.texts.filter((text) => text.trim()).length} / ${images.length}쪽`;
}

function hasReviewedAudio() {
  return Boolean(
    state.audioReview?.items?.length &&
      state.selected?.imageCount &&
      state.audioReview.items.length >= state.selected.imageCount,
  );
}

function invalidateAudioReview(message) {
  if (!state.audioReview) return;
  state.audioReview = null;
  renderAudioReview();
  if (message) setStatus(message);
}

function renderAudioReview() {
  audioReviewList.innerHTML = "";
  if (!state.audioReview?.items?.length) {
    audioReviewStatus.textContent = "미생성";
    audioReviewList.innerHTML = '<p class="hint">검수용 음성을 생성하면 페이지별 플레이어와 리롤 버튼이 표시됩니다.</p>';
    return;
  }

  audioReviewStatus.textContent = `${state.audioReview.items.length}개 생성됨`;
  for (const item of state.audioReview.items) {
    const row = document.createElement("div");
    row.className = "audio-review-item";

    const image = document.createElement("img");
    const imagePath = `${state.selected.finalFolder}/${item.image}`;
    image.src = imageUrl(imagePath);
    image.alt = item.image;

    const main = document.createElement("div");
    main.className = "audio-review-main";
    const title = document.createElement("div");
    title.className = "audio-review-title";
    title.textContent = `${String(item.index).padStart(2, "0")} · ${item.image}`;
    const audio = document.createElement("audio");
    audio.controls = true;
    audio.src = item.url;
    main.append(title, audio);

    const reroll = document.createElement("button");
    reroll.type = "button";
    reroll.className = "secondary";
    reroll.textContent = "리롤";
    reroll.addEventListener("click", () => rerollAudioPage(item.index, reroll));

    row.append(image, main, reroll);
    audioReviewList.append(row);
  }
}

function coverFallbackText() {
  if (!state.selected) return "";
  return state.selected.title.replaceAll("_", " ");
}

function alignExtractedTexts(texts) {
  const images = state.selected?.images || [];
  const hasCover = images.some((image) => image.split("/").pop().startsWith("00"));
  if (hasCover && texts.length === images.length - 1) {
    return [coverFallbackText(), ...texts];
  }
  return texts;
}

async function loadEpisodes() {
  setButtonsDisabled(true);
  setStatus("에피소드 목록을 불러오는 중입니다.");
  const previousFinalFolder = episodeSelect.value || state.selected?.finalFolder || "";
  const response = await fetch("/api/episodes");
  const data = await response.json();
  if (!response.ok || data.error) throw new Error(data.error || "에피소드 목록을 불러오지 못했습니다.");
  state.episodes = data.episodes || [];
  episodeSelect.innerHTML = "";
  for (const episode of state.episodes) {
    const option = document.createElement("option");
    option.value = episode.finalFolder;
    option.textContent = `${episode.series} / ${episode.title} (${episode.imageCount}장)`;
    episodeSelect.append(option);
  }
  if (state.episodes.some((episode) => episode.finalFolder === previousFinalFolder)) {
    episodeSelect.value = previousFinalFolder;
  }
  renderEpisode();
  setButtonsDisabled(false);
}

async function loadTtsPresets() {
  if (!state.selected) return;
  const response = await fetch(`/api/tts-presets?finalFolder=${encodeURIComponent(state.selected.finalFolder)}`);
  const data = await response.json();
  if (!response.ok || data.error) throw new Error(data.error || "TTS 프리셋을 불러오지 못했습니다.");
  state.ttsPresets = data.preset || null;
  renderPresetPalette();
}

function selectedPresetCharacter() {
  const characters = state.ttsPresets?.characters || {};
  return characters[presetCharacterSelect.value] || null;
}

function tagTooltipText(tag) {
  const translation = TAG_TRANSLATIONS[tag];
  return translation ? `${tag} - ${translation}` : `${tag} - 번역 없음`;
}

function renderPresetPalette() {
  if (!presetCharacterSelect || !presetDescription || !presetTagList || !presetSeriesLabel) return;
  const preset = state.ttsPresets;
  const characters = preset?.characters || {};
  const entries = Object.entries(characters);
  const previousValue = presetCharacterSelect.value;
  presetSeriesLabel.textContent = preset?.seriesLabel || "프리셋 없음";
  presetCharacterSelect.innerHTML = "";
  presetTagList.innerHTML = "";

  if (ttsSelect.value !== "gemini") {
    presetDescription.textContent = "캐릭터 태그는 Gemini-TTS에서만 사용합니다.";
    return;
  }

  if (!entries.length) {
    presetCharacterSelect.disabled = true;
    presetDescription.textContent = "이 시리즈의 캐릭터 프리셋 파일을 찾지 못했습니다.";
    presetTagList.innerHTML = '<p class="hint">series/<series>/docs/tts_voice_presets.yaml 파일이 필요합니다.</p>';
    return;
  }

  presetCharacterSelect.disabled = false;
  for (const [key, character] of entries) {
    const option = document.createElement("option");
    option.value = key;
    option.textContent = character.label || key;
    presetCharacterSelect.append(option);
  }
  if (characters[previousValue]) presetCharacterSelect.value = previousValue;

  const character = selectedPresetCharacter();
  if (!character) return;
  presetDescription.textContent = character.toneKo || character.promptKo || "";

  const tags = Array.from(new Set([character.defaultTag, ...(character.tagCandidates || [])].filter(Boolean)));
  for (const tag of tags) {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "tag-button";
    button.textContent = tag;
    button.title = tagTooltipText(tag);
    button.setAttribute("aria-label", tagTooltipText(tag));
    button.addEventListener("click", () => insertAudioTag(tag));
    presetTagList.append(button);
  }
}

function activeScriptTextarea() {
  if (state.activeScriptTextarea?.isConnected) return state.activeScriptTextarea;
  const firstTextarea = scriptEditor.querySelector("textarea");
  if (firstTextarea) {
    state.activeScriptTextarea = firstTextarea;
    return firstTextarea;
  }
  return null;
}

function insertAudioTag(tag) {
  const textarea = activeScriptTextarea();
  if (!textarea) {
    setStatus("태그를 넣을 TTS 원고 칸을 먼저 선택하세요.", true);
    return;
  }
  const insertText = `${tag} `;
  const start = textarea.selectionStart ?? textarea.value.length;
  const end = textarea.selectionEnd ?? textarea.value.length;
  textarea.value = `${textarea.value.slice(0, start)}${insertText}${textarea.value.slice(end)}`;
  const nextCursor = start + insertText.length;
  textarea.setSelectionRange(nextCursor, nextCursor);
  textarea.focus();
  textarea.dispatchEvent(new Event("input", { bubbles: true }));
}

async function extractScript() {
  if (state.directScriptContent) {
    await extractScriptContent(state.directScriptContent, state.directScriptLabel || "직접 선택한 대본");
    return;
  }
  if (!state.selected || !scriptSelect.value) return;
  setButtonsDisabled(true);
  setStatus("대본에서 페이지 텍스트를 추출하는 중입니다.");
  try {
    const response = await fetch("/api/extract", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({ sourcePath: scriptSelect.value }),
    });
    const data = await response.json();
    if (!response.ok || data.error) throw new Error(data.error || "대본 추출 실패");
    state.texts = alignExtractedTexts(data.texts || []);
    state.audioReview = null;
    renderScriptEditor();
    renderAudioReview();
    const diff = state.selected.imageCount - state.texts.length;
    setStatus(diff === 0 ? "대본 추출 완료." : `대본 추출 완료. 이미지와 텍스트 개수 차이: ${diff}`);
  } catch (error) {
    setStatus(error.message, true);
  } finally {
    setButtonsDisabled(false);
  }
}

async function extractScriptContent(content, label = "직접 입력") {
  if (!state.selected || !content.trim()) return;
  setButtonsDisabled(true);
  setStatus(`${label}에서 페이지 텍스트를 추출하는 중입니다.`);
  try {
    const response = await fetch("/api/extract-content", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({ content }),
    });
    const data = await response.json();
    if (!response.ok || data.error) throw new Error(data.error || "대본 추출 실패");
    state.texts = alignExtractedTexts(data.texts || []);
    state.audioReview = null;
    renderScriptEditor();
    renderAudioReview();
    const diff = state.selected.imageCount - state.texts.length;
    setStatus(diff === 0 ? "대본 추출 완료." : `대본 추출 완료. 이미지와 텍스트 개수 차이: ${diff}`);
  } catch (error) {
    setStatus(error.message, true);
  } finally {
    setButtonsDisabled(false);
  }
}

async function saveScript() {
  state.selected = selectedEpisode();
  if (!state.selected) return null;
  const response = await fetch("/api/save-script", {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({ episode: state.selected, texts: state.texts }),
  });
  const data = await response.json();
  if (!response.ok || data.error) throw new Error(data.error || "원고 저장 실패");
  setStatus(`원고 저장 완료\n${data.scriptPath}`);
  return data;
}

function renderSettings() {
  return {
    tts: ttsSelect.value,
    geminiModel: geminiModel.value,
    geminiVoice: geminiVoice.value,
    cloudVoice: cloudVoice.value,
    geminiPrompt: stylePrompt.value,
    speakingRate: Number(speedInput.value),
    pitch: Number(pitchInput.value),
    pageGap: Number(gapInput.value),
    outputName: outputName.value,
    sampleText: sampleText.value,
  };
}

function leadingNumberFromName(name) {
  const match = name.match(/^(\d+)/);
  return match ? Number(match[1]) : null;
}

function sortedManualAudioFiles() {
  return Array.from(manualAudioInput.files || []).sort((left, right) => {
    const leftNumber = leadingNumberFromName(left.name);
    const rightNumber = leadingNumberFromName(right.name);
    if (leftNumber !== null && rightNumber !== null && leftNumber !== rightNumber) {
      return leftNumber - rightNumber;
    }
    if (leftNumber !== null && rightNumber === null) return -1;
    if (leftNumber === null && rightNumber !== null) return 1;
    return left.name.localeCompare(right.name, "ko");
  });
}

function arrayBufferToBase64(buffer) {
  const bytes = new Uint8Array(buffer);
  const chunkSize = 0x8000;
  let binary = "";
  for (let offset = 0; offset < bytes.length; offset += chunkSize) {
    binary += String.fromCharCode(...bytes.subarray(offset, offset + chunkSize));
  }
  return btoa(binary);
}

async function manualAudioPayload() {
  const files = sortedManualAudioFiles();
  const expected = state.selected?.imageCount || 0;
  if (!files.length) {
    throw new Error("오디오 업로드 모드에서는 페이지별 오디오 파일을 선택해야 합니다.");
  }
  if (files.length < expected) {
    throw new Error(`오디오 파일이 부족합니다. 현재 ${files.length}개, 필요한 파일 ${expected}개입니다.`);
  }
  const selected = files.slice(0, expected);
  return Promise.all(
    selected.map(async (file) => ({
      name: file.name,
      type: file.type || "application/octet-stream",
      dataBase64: arrayBufferToBase64(await file.arrayBuffer()),
    })),
  );
}

async function previewVoice() {
  if (ttsSelect.value === "manual") {
    setStatus("오디오 업로드 모드는 미리듣기 대신 선택한 파일을 그대로 영상에 붙입니다.");
    return;
  }
  setButtonsDisabled(true);
  sampleButton.disabled = true;
  setStatus("보이스 샘플을 생성하는 중입니다.");
  try {
    const response = await fetch("/api/sample", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({ settings: renderSettings() }),
    });
    const data = await response.json();
    if (!response.ok || data.error) throw new Error(data.error || "샘플 생성 실패");
    sampleAudio.src = data.sample.url;
    await sampleAudio.play().catch(() => {});
    setStatus(`샘플 생성 완료\n${data.sample.path}`);
  } catch (error) {
    setStatus(error.message, true);
  } finally {
    setButtonsDisabled(false);
    sampleButton.disabled = false;
  }
}

async function startAudioReview() {
  state.selected = selectedEpisode();
  if (!state.selected || ttsSelect.value === "manual") return;
  setButtonsDisabled(true);
  jobState.textContent = "음성 생성 중";
  setStatus("페이지별 검수용 음성을 생성합니다.");
  try {
    const response = await fetch("/api/audio-review/start", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({ episode: state.selected, texts: state.texts, settings: renderSettings() }),
    });
    const data = await response.json();
    if (!response.ok || data.error) throw new Error(data.error || "검수용 음성 생성 시작 실패");
    state.jobId = data.job.id;
    state.jobKind = "audio-review";
    pollJob();
  } catch (error) {
    setButtonsDisabled(false);
    jobState.textContent = "실패";
    setStatus(error.message, true);
  }
}

async function rerollAudioPage(index, button) {
  state.selected = selectedEpisode();
  if (!state.selected) return;
  const previousText = button.textContent;
  button.disabled = true;
  button.textContent = "생성 중";
  setStatus(`${String(index).padStart(2, "0")}페이지 음성을 다시 생성합니다.`);
  try {
    const response = await fetch("/api/audio-review/reroll", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({ episode: state.selected, texts: state.texts, settings: renderSettings(), index }),
    });
    const data = await response.json();
    if (!response.ok || data.error) throw new Error(data.error || "페이지 음성 리롤 실패");
    if (!state.audioReview) state.audioReview = { items: [] };
    state.audioReview.scriptPath = data.audioReview.scriptPath;
    state.audioReview.outputDir = data.audioReview.outputDir;
    state.audioReview.items[index] = data.audioReview.item;
    renderAudioReview();
    setStatus(`${String(index).padStart(2, "0")}페이지 음성 리롤 완료.`);
  } catch (error) {
    setStatus(error.message, true);
  } finally {
    button.disabled = false;
    button.textContent = previousText;
  }
}

async function renderVideo() {
  state.selected = selectedEpisode();
  if (!state.selected) return;
  setButtonsDisabled(true);
  jobState.textContent = "실행 중";
  setStatus("렌더링 작업을 시작합니다.");
  try {
    const settings = renderSettings();
    if (settings.tts === "manual") {
      settings.manualAudioFiles = await manualAudioPayload();
    } else if (hasReviewedAudio()) {
      settings.reviewedAudio = true;
    }
    const response = await fetch("/api/render", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({ episode: state.selected, texts: state.texts, settings }),
    });
    const data = await response.json();
    if (!response.ok || data.error) throw new Error(data.error || "렌더링 시작 실패");
    state.jobId = data.job.id;
    state.jobKind = "render";
    pollJob();
  } catch (error) {
    setButtonsDisabled(false);
    jobState.textContent = "실패";
    setStatus(error.message, true);
  }
}

async function pollJob() {
  if (!state.jobId) return;
  const response = await fetch(`/api/jobs/${encodeURIComponent(state.jobId)}`);
  const data = await response.json();
  if (!response.ok || data.error) {
    setButtonsDisabled(false);
    setStatus(data.error || "작업 상태 조회 실패", true);
    return;
  }
  const job = data.job;
  jobState.textContent = job.status;
  const lines = [];
  lines.push(`작업: ${job.status}`);
  lines.push(`원고: ${job.scriptPath}`);
  lines.push(`출력: ${job.outputPath}`);
  if (job.stdout) lines.push("\n[stdout]\n" + job.stdout.trim());
  if (job.stderr) lines.push("\n[stderr]\n" + job.stderr.trim());
  setStatus(lines.join("\n"), job.status === "failed");
  if (job.status === "running") {
    state.pollTimer = window.setTimeout(pollJob, 1500);
  } else {
    if (job.status === "complete" && state.jobKind === "audio-review" && job.audioReview) {
      state.audioReview = job.audioReview;
      renderAudioReview();
      setStatus(`검수용 음성 생성 완료. 페이지별로 들어보고 필요한 페이지만 리롤하세요.\n원고: ${job.scriptPath}`);
    }
    setButtonsDisabled(false);
    state.jobKind = null;
  }
}

async function refreshVoices() {
  setButtonsDisabled(true);
  setStatus("Cloud TTS 보이스 목록을 불러오는 중입니다.");
  try {
    const response = await fetch("/api/voices?language=ko-KR");
    const data = await response.json();
    if (!response.ok || data.error) throw new Error(data.error || "보이스 목록 조회 실패");
    cloudVoice.innerHTML = "";
    for (const voice of data.voices || []) {
      const option = document.createElement("option");
      option.value = voice.name;
      option.textContent = `${voice.name} ${voice.gender ? `(${voice.gender})` : ""}`;
      cloudVoice.append(option);
    }
    setStatus(`${cloudVoice.options.length}개 보이스를 불러왔습니다.`);
  } catch (error) {
    setStatus(error.message, true);
  } finally {
    setButtonsDisabled(false);
  }
}

episodeSelect.addEventListener("change", renderEpisode);
scriptSelect.addEventListener("change", () => {
  state.directScriptContent = "";
  state.directScriptLabel = "";
});
reloadButton.addEventListener("click", () => loadEpisodes().catch((error) => setStatus(error.message, true)));
extractButton.addEventListener("click", extractScript);
extractPasteButton.addEventListener("click", () => extractScriptContent(scriptPaste.value, "붙여넣은 대본"));
scriptFileInput.addEventListener("change", async () => {
  const file = scriptFileInput.files?.[0];
  if (!file) return;
  const content = await file.text();
  state.directScriptContent = content;
  state.directScriptLabel = file.name;
  scriptPaste.value = content;
  extractScriptContent(content, file.name);
});
manualAudioInput.addEventListener("change", () => {
  const files = sortedManualAudioFiles();
  const names = files.slice(0, 4).map((file) => file.name).join(", ");
  const suffix = files.length > 4 ? "..." : "";
  manualAudioStatus.textContent = files.length
    ? `${files.length}개 선택됨: ${names}${suffix}`
    : "파일명 앞 숫자 기준으로 00, 01, 02 순서에 맞춰 붙입니다.";
});
saveButton.addEventListener("click", () => saveScript().catch((error) => setStatus(error.message, true)));
reviewAudioButton.addEventListener("click", startAudioReview);
renderButton.addEventListener("click", renderVideo);
voiceButton.addEventListener("click", refreshVoices);
sampleButton.addEventListener("click", previewVoice);
presetCharacterSelect.addEventListener("change", renderPresetPalette);
ttsSelect.addEventListener("change", () => {
  renderSettingsVisibility();
  invalidateAudioReview("TTS 방식이 변경되어 검수 음성을 다시 생성해야 합니다.");
});
[geminiModel, geminiVoice, cloudVoice].forEach((input) => {
  input.addEventListener("change", () => invalidateAudioReview("음성 설정이 변경되어 검수 음성을 다시 생성해야 합니다."));
});
stylePrompt.addEventListener("input", () => invalidateAudioReview("스타일이 변경되어 검수 음성을 다시 생성해야 합니다."));
[speedInput, pitchInput].forEach((input) => {
  input.addEventListener("input", () => {
    updateRangeLabels();
    invalidateAudioReview("속도 또는 피치가 변경되어 검수 음성을 다시 생성해야 합니다.");
  });
});
gapInput.addEventListener("input", updateRangeLabels);

renderSettingsVisibility();
updateRangeLabels();
renderAudioReview();
loadEpisodes().catch((error) => setStatus(error.message, true));
