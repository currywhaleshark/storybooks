from __future__ import annotations

import argparse
import hashlib
import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


EXPECTED_TEXT = """빠른 물살이
미역숲을 가르며 지나갔어요.

모리는 기다렸다는 듯
그 물살에 몸을 맡겼어요.

“다음에 또 놀자,
셜록 핀!”

“잠깐!”

셜록 핀이 손을 뻗었지만,
모리는 좁은 물길을 타고
쏜살같이 멀어졌어요.

물살이 지나가자
미역은 다시 닫혔어요.

펄리가 말했어요.

“회중시계는
물살이 오는 시간을
보고 있었던 거군요!”

셜록 핀이 고개를 끄덕였어요.

“만날 곳뿐 아니라
떠날 때까지 계산했어.
마지막 수는 내가 놓쳤네.”

셜록 핀의 손에는
소용돌이 카드 한 장만
남아 있었어요."""


def extract_scene12_text(script_path: Path) -> str:
    source = script_path.read_text(encoding="utf-8").replace("\r\n", "\n")
    match = re.search(
        r"(?ms)^### 12\s*$.*?^Text:\s*$\n+(.*?)(?=^### 13\s*$)",
        source,
    )
    if not match:
        raise RuntimeError("Could not locate scene 12 Text block")
    body = match.group(1).strip()
    if body != EXPECTED_TEXT:
        raise RuntimeError("Scene 12 text differs from the approved exact text")
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

    body = extract_scene12_text(args.script)
    canvas = Image.open(args.background).convert("RGB")
    canvas = canvas.resize((1054, 1492), Image.Resampling.LANCZOS)
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.truetype(str(args.font), 36)

    paragraphs = [paragraph.splitlines() for paragraph in body.split("\n\n")]
    navy = (46, 55, 79)
    teal = (38, 116, 116)
    coral = (185, 88, 105)
    purple = (112, 66, 117)
    paragraph_colors = {
        0: teal,
        1: purple,
        2: purple,
        3: teal,
        4: navy,
        5: teal,
        6: coral,
        7: coral,
        8: navy,
        9: teal,
        10: purple,
    }
    line_advance = 43
    paragraph_gap = 6

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
