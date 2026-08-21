from __future__ import annotations

import argparse
import hashlib
import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


EXPECTED_TEXT = """딥시티에 아침이 왔어요.

그런데 산호 골목이
온통 뒤죽박죽이었어요!

빵집 앞에는
조개 간식 간판이,

간식 가게 앞에는
책 간판이,

도서관 앞에는
빵 간판이 걸려 있었어요.

“어? 빵집이 어디지?”

손님들이 이리저리
헤맸어요."""


def extract_scene01_text(script_path: Path) -> str:
    source = script_path.read_text(encoding="utf-8").replace("\r\n", "\n")
    match = re.search(
        r"(?ms)^### 01\s*$.*?^Text:\s*$\n+(.*?)(?=^### 02\s*$)",
        source,
    )
    if not match:
        raise RuntimeError("Could not locate scene 01 Text block")
    body = match.group(1).strip()
    if body != EXPECTED_TEXT:
        raise RuntimeError("Scene 01 text differs from the approved exact text")
    return body


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--background", required=True, type=Path)
    parser.add_argument("--script", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument(
        "--font",
        type=Path,
        default=Path(r"C:\Windows\Fonts\NotoSansKR-VF.ttf"),
    )
    args = parser.parse_args()

    body = extract_scene01_text(args.script)

    canvas = Image.open(args.background).convert("RGB")
    canvas = canvas.resize((1054, 1492), Image.Resampling.LANCZOS)
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.truetype(str(args.font), 48)
    try:
        axes = font.get_variation_axes()
        if axes:
            font.set_variation_by_axes([450])
    except (AttributeError, OSError):
        pass

    paragraphs = [paragraph.splitlines() for paragraph in body.split("\n\n")]
    default_color = (46, 55, 79)
    emphasis_color = (184, 74, 78)
    dialogue_color = (40, 112, 112)
    line_advance = 66
    paragraph_gap = 28

    line_count = sum(len(paragraph) for paragraph in paragraphs)
    total_height = line_count * line_advance + (len(paragraphs) - 1) * paragraph_gap
    y = max(195, (1492 - total_height) // 2 - 10)
    x = 224
    max_right = 938

    for paragraph_index, paragraph in enumerate(paragraphs):
        color = default_color
        if paragraph_index == 1:
            color = emphasis_color
        elif paragraph_index == 5:
            color = dialogue_color

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
