from __future__ import annotations

import argparse
import hashlib
import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


EXPECTED_TEXT = """사건은 해결되었어요.

하지만 셜록 핀은
소용돌이 카드를 들고
미역숲 쪽을 바라보았어요.

“이번에는
수수께끼는 풀었지만
마지막 수를 놓쳤어.”

셜록 핀이
모자를 고쳐 썼어요.

“하지만 다음에는
네가 움직이기 전에
내가 먼저 알아낼 거야.”

단서는 무엇을 말하는지뿐 아니라,
왜 그곳에 놓였는지도
생각해 보세요.

꼬마 탐정단,
다음에 계속!"""


def extract_scene14_text(script_path: Path) -> str:
    source = script_path.read_text(encoding="utf-8").replace("\r\n", "\n")
    match = re.search(
        r"(?ms)^### 14\s*$.*?^Text:\s*$\n+(.*?)(?=^## 품질 검사\s*$)",
        source,
    )
    if not match:
        raise RuntimeError("Could not locate scene 14 Text block")
    body = match.group(1).strip()
    if body != EXPECTED_TEXT:
        raise RuntimeError("Scene 14 text differs from the approved exact text")
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

    body = extract_scene14_text(args.script)
    canvas = Image.open(args.background).convert("RGB")
    canvas = canvas.resize((1054, 1492), Image.Resampling.LANCZOS)
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.truetype(str(args.font), 44)

    paragraphs = [paragraph.splitlines() for paragraph in body.split("\n\n")]
    navy = (46, 55, 79)
    teal = (38, 116, 116)
    gold = (151, 103, 40)
    coral = (185, 88, 105)
    purple = (112, 66, 117)
    paragraph_colors = {
        0: navy,
        1: purple,
        2: purple,
        3: gold,
        4: teal,
        5: navy,
        6: coral,
    }
    line_advance = 54
    paragraph_gap = 12

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
