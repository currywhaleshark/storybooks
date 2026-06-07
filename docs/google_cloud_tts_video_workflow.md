# Google Cloud / Gemini TTS Storybook Video Workflow

This note explains how to recreate narrated storybook videos from the existing page images and `tts_script.md` files.

## What This Workflow Produces

- Page-by-page MP4 storybook narration videos.
- Google Cloud Text-to-Speech voices such as `ko-KR-Chirp3-HD-Kore`.
- Gemini-TTS narration using voices such as `Kore`.
- Optional silence between pages so the narration does not feel rushed.

## Local Web App

The browser workflow is available as a local web app:

```powershell
C:\Users\yurib\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe tools\tts-video\server.py
```

Open:

```text
http://localhost:4174
```

The app can:

- Discover episode `final` image folders under `series`.
- Preview page images.
- Extract page narration from markdown script files.
- Edit and save `tts_script.md`.
- Select TTS mode, model, voice, style prompt, speed, pitch, and page gap.
- Select `gemini-3.1-flash-tts-preview` when it is available to the current Google Cloud project.
- Assemble a video from already generated page audio files if a preview TTS model is not reachable from this app.
- Generate page-by-page review audio, listen to each page, reroll only weak pages, then assemble the final video from the approved audio files.
- Start a render job and poll its progress.

Current example output:

`series/sherlock-fin-deep-city/videos/누가_먼저_왔을까_tts_google/sherlock_fin_ep01_gemini25_kore_gap.mp4`

## Episode Script Storage

For every storybook episode, keep the full source prompt/script Markdown in the series project folder:

```text
series/<series-name>/docs/episodes/<episode-title>.md
```

This full source file should preserve scene directions, composition notes, key emotions, image prompts, and page text.

When a separate narration-only file is useful, keep it beside the source script:

```text
series/<series-name>/docs/episodes/<episode-title>_tts.md
```

The TTS web app lists both files as script candidates for the matching episode image folder and prefers `_tts.md` files when they match the episode title. For reliable extraction, the TTS file should include a `### 페이지 텍스트` heading followed by a fenced `text` block containing only the narration for that page.

When the web app saves edited narration for a specific video run, it still writes that run-specific copy to:

```text
series/<series-name>/videos/<episode-title>_tts_app/tts_script.md
```

## Required Local Tools

Install or verify these on each computer:

1. Google Cloud CLI
   - Needed for local Application Default Credentials.
2. FFmpeg
   - Needed to assemble images and audio into MP4.
3. Python 3.11+
   - The Codex bundled Python also works in this workspace.

Check:

```powershell
gcloud --version
ffmpeg -version
python --version
```

In Codex Desktop, the bundled Python may be at:

```powershell
C:\Users\yurib\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe
```

## Google Authentication Without Service Account Keys

This workflow avoids service account JSON keys. That matters because many Google Cloud organizations block key creation with the `iam.disableServiceAccountKeyCreation` policy.

Run this once per computer:

```powershell
gcloud init
gcloud services enable texttospeech.googleapis.com
gcloud auth application-default login
gcloud auth application-default set-quota-project YOUR_PROJECT_ID
```

Replace `YOUR_PROJECT_ID` with the Google Cloud project ID that should pay for TTS quota.

After this, an ADC file should exist at:

```text
%APPDATA%\gcloud\application_default_credentials.json
```

Do not commit this credential file.

## Script Location

The current reusable script is:

```text
series/sherlock-fin-deep-city/videos/누가_먼저_왔을까_tts_google/make_tts_video.py
```

The narration source is:

```text
series/sherlock-fin-deep-city/videos/누가_먼저_왔을까_tts_google/tts_script.md
```

The page images are read from:

```text
series/sherlock-fin-deep-city/images/episodes/누가_먼저_왔을까/final
```

## List Available Korean Cloud TTS Voices

```powershell
python make_tts_video.py --list-cloud-voices --cloud-language ko-KR
```

Useful Korean voices seen in this workspace:

- `ko-KR-Chirp3-HD-Kore`
- `ko-KR-Chirp3-HD-Aoede`
- `ko-KR-Neural2-A`
- `ko-KR-Wavenet-A`

## Render With Standard Google Cloud TTS

```powershell
python make_tts_video.py `
  --tts cloud `
  --cloud-voice ko-KR-Chirp3-HD-Kore `
  --speaking-rate 0.9 `
  --page-gap 0.8 `
  --output sherlock_fin_ep01_cloud_kore_tts.mp4
```

## Render With Gemini-TTS

Current verified model:

```text
gemini-2.5-flash-tts
```

The web app also exposes:

```text
gemini-3.1-flash-tts-preview
```

This model is still preview-labeled. If the Cloud Text-to-Speech API rejects it for the current account, region, or project, generate page audio separately in Google Cloud Studio or another supported console, download the files, and use the web app's `오디오 파일 업로드` mode.

Example:

```powershell
python make_tts_video.py `
  --tts gemini `
  --gemini-model gemini-2.5-flash-tts `
  --gemini-voice Kore `
  --speaking-rate 0.9 `
  --page-gap 0.8 `
  --output sherlock_fin_ep01_gemini25_kore_gap.mp4
```

The default Gemini prompt in the script asks for warm, clear children's storybook narration. You can override it:

```powershell
python make_tts_video.py `
  --tts gemini `
  --gemini-voice Kore `
  --gemini-prompt "따뜻하고 다정한 어린이 그림책 선생님처럼, 문장 끝을 부드럽게 쉬어 가며 읽어 주세요." `
  --page-gap 1.0 `
  --output output.mp4
```

## Page Gap

Use `--page-gap` to add silence after each page's narration.

Good starting values:

- `0.5`: only a small breath.
- `0.8`: comfortable default.
- `1.0`: more picture-book-like pacing.
- `1.5`: slow bedtime-story pacing.

## Reusing Already Generated Audio

If audio files already exist and only video timing changed:

```powershell
python make_tts_video.py --tts gemini --reuse-audio --page-gap 1.0 --output output_gap_1s.mp4
```

Important: `--reuse-audio` reuses whatever is in the `audio` folder, so only use it when the audio was generated with the intended voice/model.

## Building Video From Downloaded Audio

In the web app, choose `TTS 방식` -> `오디오 파일 업로드`.

Prepare one audio file per page, including the cover page when the episode has `00_...` as the first image. Name the files with matching leading numbers:

```text
00.mp3
01.mp3
02.mp3
...
```

Then select all audio files in the upload field and click `영상 만들기`. Files are matched by the leading number in the filename. MP3 files are used directly; WAV, M4A, OGG, and OPUS files are converted to MP3 with FFmpeg before assembly.

## Page Audio Review Workflow

For normal Gemini or Cloud TTS work, use this flow instead of creating the final video immediately:

1. Extract or edit the TTS script.
2. Select model, voice, style, speed, and pitch.
3. Click `검수용 음성 생성`.
4. Listen to each page in `음성 검수`.
5. Click `리롤` only on pages with bad pronunciation or weak delivery.
6. Click `영상 만들기`.

When page review audio exists, `영상 만들기` reuses the approved `audio/00.mp3`, `audio/01.mp3`, ... files instead of calling TTS again. Changing the script, model, voice, style, speed, or pitch invalidates the review audio and requires generating it again.

## Porting To Another Episode

For another episode:

1. Copy the video folder pattern to a new episode-specific folder.
2. Create a new `tts_script.md`.
3. Update `EPISODE_DIR` in `make_tts_video.py` to point to that episode's `final` image folder.
4. Ensure the `## image_filename.png` headings in `tts_script.md` exactly match the page image filenames.
5. Run a Gemini or Cloud TTS render command.

Recommended future improvement: move `EPISODE_DIR` and `SCRIPT_PATH` to command-line arguments so the same script can run any episode without editing Python.

## Troubleshooting

If `gcloud` works in a normal PowerShell but not in Codex, the Codex shell may not have the updated PATH. The script can still work if ADC exists at `%APPDATA%\gcloud\application_default_credentials.json`.

If the API says quota project is missing:

```powershell
gcloud auth application-default set-quota-project YOUR_PROJECT_ID
```

If service account key creation is blocked by organization policy, keep using ADC login. Do not create or commit service account JSON keys unless the project owner explicitly allows that.

If the narration feels rushed, increase:

```powershell
--page-gap 1.0
```

If a page audio sounds wrong, delete only that page's audio file from the `audio` folder and rerun without `--reuse-audio`.
