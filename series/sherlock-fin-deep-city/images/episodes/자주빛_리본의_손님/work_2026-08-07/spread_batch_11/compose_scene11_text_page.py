from __future__ import annotations

import argparse
import hashlib
import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


EXPECTED_TEXT = """그때 모리가
금빛 회중시계를 꺼냈어요.

딸깍.

시계를 본 모리가
싱긋 웃었어요.

“이제 곧이네.”

펄리가 고개를 갸웃했어요.

“뭐가 곧이라는 거예요?”

작은 거품들이
더 빠르게 흘렀어요.

멀리서 물살 소리가
다가왔어요.

쉬이이이—!"""


def extract_scene11_text(script_path: Path) -> str:
    source = script_path.read_text(encoding="utf-8").replace("\r\n", "\n")
    match = re.search(
        r"(?ms)^### 11\s*$.*?^Text:\s*$\n+(.*?)(?=^### 12\s*$)",
        source,
    )
    if not match:
        raise RuntimeError("Could not locate scene 11 Text block")
    body = match.group(1).strip()
    if body != EXPECTED_TEXT:
        raise RuntimeError("Scene 11 text differs from the approved exact text")
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

    body = extract_scene11_text(args.script)
    canvas = Image.open(args.background).convert("RGB")
    canvas = canvas.resize((1054, 1492), Image.Resampling.LANCZOS)
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.truetype(str(args.font), 48)

    paragraphs = [paragraph.splitlines() for paragraph in body.split("\n\n")]
    purple = (112, 66, 117)
    gold = (151, 103, 40)
    coral = (185, 88, 105)
    teal = (38, 116, 116)
    paragraph_colors = {
        0: purple,
        1: gold,
        2: purple,
        3: purple,
        4: coral,
        5: coral,
        6: teal,
        7: teal,
        8: teal,
    }
    line_advance = 62
    paragraph_gap = 18

    line_count = sum(len(paragraph) for paragraph in paragraphs)
    total_height = line_count * line_advance + (len(paragraphs) - 1) * paragraph_gap
    y = max(185, (1492 - total_height) // 2 - 10)
    x = 224
    max_right = 938

    for paragraph_index, paragraph in enumerate(paragraphs):
        color = paragraph_colors[paragraph_index]
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
