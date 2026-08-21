from __future__ import annotations

import argparse
import hashlib
import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


EXPECTED_TEXT = """셜록 핀과 친구들은
간판을 제자리로
돌려놓았어요.

“모두 한 칸씩 옮겨졌으니
반대로 한 칸씩 돌리면 돼.”

빵집 앞에는 빵 간판.
간식 가게 앞에는 간식 간판.
도서관 앞에는 책 간판.

“이제 됐다!”

골목이 다시
제자리를 찾았어요.

“고마워, 셜록 핀!”"""


def extract_scene13_text(script_path: Path) -> str:
    source = script_path.read_text(encoding="utf-8").replace("\r\n", "\n")
    match = re.search(
        r"(?ms)^### 13\s*$.*?^Text:\s*$\n+(.*?)(?=^### 14\s*$)",
        source,
    )
    if not match:
        raise RuntimeError("Could not locate scene 13 Text block")
    body = match.group(1).strip()
    if body != EXPECTED_TEXT:
        raise RuntimeError("Scene 13 text differs from the approved exact text")
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

    body = extract_scene13_text(args.script)
    canvas = Image.open(args.background).convert("RGB")
    canvas = canvas.resize((1054, 1492), Image.Resampling.LANCZOS)
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.truetype(str(args.font), 52)

    paragraphs = [paragraph.splitlines() for paragraph in body.split("\n\n")]
    navy = (46, 55, 79)
    teal = (38, 116, 116)
    gold = (151, 103, 40)
    coral = (185, 88, 105)
    purple = (112, 66, 117)
    paragraph_colors = {
        0: navy,
        1: teal,
        2: gold,
        3: coral,
        4: teal,
        5: purple,
    }
    line_advance = 66
    paragraph_gap = 20

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
