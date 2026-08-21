from __future__ import annotations

import argparse
import hashlib
import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


EXPECTED_TEXT = """이번에는 간판 아래를
살펴보았어요.

간판은 아주 높은데,
모래에는 사다리 자국이
하나도 없었어요.

양쪽 고리는
가지런히 묶여 있었지요.

그리고 한쪽에는
자줏빛 리본 조각이
곱게 매여 있었어요.

셜록 핀이 리본 끝을 보았어요.

“찢겨 걸린 게 아니야.
반듯하게 자른 뒤
일부러 묶어 놓았어.

높이 헤엄쳐 올라가
두 손을 자유롭게 쓴 친구야.

두 번째 단서!”"""


def extract_scene04_text(script_path: Path) -> str:
    source = script_path.read_text(encoding="utf-8").replace("\r\n", "\n")
    match = re.search(
        r"(?ms)^### 04\s*$.*?^Text:\s*$\n+(.*?)(?=^### 05\s*$)",
        source,
    )
    if not match:
        raise RuntimeError("Could not locate scene 04 Text block")
    body = match.group(1).strip()
    if body != EXPECTED_TEXT:
        raise RuntimeError("Scene 04 text differs from the approved exact text")
    return body


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--background", required=True, type=Path)
    parser.add_argument("--script", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument(
        "--font",
        type=Path,
        default=Path(r"C:\Windows\Fonts\Katuri.ttf"),
    )
    args = parser.parse_args()

    body = extract_scene04_text(args.script)
    canvas = Image.open(args.background).convert("RGB")
    canvas = canvas.resize((1054, 1492), Image.Resampling.LANCZOS)
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.truetype(str(args.font), 42)

    paragraphs = [paragraph.splitlines() for paragraph in body.split("\n\n")]
    navy = (46, 55, 79)
    coral = (190, 74, 60)
    teal = (38, 116, 116)
    paragraph_colors = {
        3: coral,
        5: teal,
        6: teal,
        7: teal,
    }
    line_advance = 55
    paragraph_gap = 15

    line_count = sum(len(paragraph) for paragraph in paragraphs)
    total_height = line_count * line_advance + (len(paragraphs) - 1) * paragraph_gap
    y = max(185, (1492 - total_height) // 2 - 10)
    x = 224
    max_right = 938

    for paragraph_index, paragraph in enumerate(paragraphs):
        color = paragraph_colors.get(paragraph_index, navy)
        for line in paragraph:
            bounds = draw.textbbox((x, y), line, font=font)
            if bounds[2] > max_right:
                raise RuntimeError(f"Text exceeds safe area: {line}")
            draw.text((x, y), line, font=font, fill=color)
            y += line_advance
        if paragraph_index != len(paragraphs) - 1:
            y += paragraph_gap

    if y > 1270:
        raise RuntimeError(f"Text exceeds bottom safe area: y={y}")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(args.output, format="PNG", optimize=True)
    digest = hashlib.sha256(body.encode("utf-8")).hexdigest().upper()
    print(f"output={args.output}")
    print(f"size={canvas.width}x{canvas.height}")
    print(f"text_sha256={digest}")
    print(f"paragraphs={len(paragraphs)} lines={line_count} bottom={y}")


if __name__ == "__main__":
    main()
