from __future__ import annotations

import argparse
import hashlib
import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


EXPECTED_TEXT = """그때 셜록 핀이
문득 멈칫했어요.

“……잠깐.”

간판은 규칙대로 움직였어요.
리본은 곱게 묶여 있었어요.
카드는 풀기 좋게 나뉘어 있었지요.

“모두 너무 잘 보여.

이건 실수로 남은 흔적이 아니야.
내가 알아보도록
일부러 만든 문제야!”

펄리가 놀랐어요.

“그럼 누군가
셜록 핀을 부르는 거예요?”

“맞아. 이건 초대장이야.”"""


def extract_scene06_text(script_path: Path) -> str:
    source = script_path.read_text(encoding="utf-8").replace("\r\n", "\n")
    match = re.search(
        r"(?ms)^### 06\s*$.*?^Text:\s*$\n+(.*?)(?=^### 07\s*$)",
        source,
    )
    if not match:
        raise RuntimeError("Could not locate scene 06 Text block")
    body = match.group(1).strip()
    if body != EXPECTED_TEXT:
        raise RuntimeError("Scene 06 text differs from the approved exact text")
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

    body = extract_scene06_text(args.script)
    canvas = Image.open(args.background).convert("RGB")
    canvas = canvas.resize((1054, 1492), Image.Resampling.LANCZOS)
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.truetype(str(args.font), 44)

    paragraphs = [paragraph.splitlines() for paragraph in body.split("\n\n")]
    navy = (46, 55, 79)
    coral = (190, 74, 60)
    teal = (38, 116, 116)
    gold = (174, 115, 34)
    purple = (112, 66, 132)
    paragraph_colors = {
        1: teal,
        3: teal,
        4: teal,
        5: coral,
        6: coral,
        7: teal,
    }
    line_colors = {
        "간판은 규칙대로 움직였어요.": gold,
        "리본은 곱게 묶여 있었어요.": purple,
        "카드는 풀기 좋게 나뉘어 있었지요.": teal,
    }
    line_advance = 57
    paragraph_gap = 15

    line_count = sum(len(paragraph) for paragraph in paragraphs)
    total_height = line_count * line_advance + (len(paragraphs) - 1) * paragraph_gap
    y = max(185, (1492 - total_height) // 2 - 10)
    x = 224
    max_right = 938

    for paragraph_index, paragraph in enumerate(paragraphs):
        paragraph_color = paragraph_colors.get(paragraph_index, navy)
        for line in paragraph:
            color = line_colors.get(line, paragraph_color)
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
