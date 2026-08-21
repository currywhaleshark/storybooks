from __future__ import annotations

import argparse
import hashlib
import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


EXPECTED_TEXT = """크랩슨이 달려왔어요.

“셜록 핀, 큰일이야!

밤사이에 누가
간판을 전부 바꿔 놨어.”

빵집 주인도 말했어요.

“손님들이 자꾸
다른 가게로 들어가요.”

셜록 핀이 물었어요.

“다친 친구는 없나요?
간판은 부서지지 않았고요?”

“다행히 모두 괜찮아.”

셜록 핀이 모자를
살짝 눌러썼어요.

“그럼 왜 이런 일이 일어났는지
잘 살펴보자.”"""


def extract_scene02_text(script_path: Path) -> str:
    source = script_path.read_text(encoding="utf-8").replace("\r\n", "\n")
    match = re.search(
        r"(?ms)^### 02\s*$.*?^Text:\s*$\n+(.*?)(?=^### 03\s*$)",
        source,
    )
    if not match:
        raise RuntimeError("Could not locate scene 02 Text block")
    body = match.group(1).strip()
    if body != EXPECTED_TEXT:
        raise RuntimeError("Scene 02 text differs from the approved exact text")
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

    body = extract_scene02_text(args.script)
    canvas = Image.open(args.background).convert("RGB")
    canvas = canvas.resize((1054, 1492), Image.Resampling.LANCZOS)
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.truetype(str(args.font), 44)

    paragraphs = [paragraph.splitlines() for paragraph in body.split("\n\n")]
    navy = (46, 55, 79)
    crabson = (190, 74, 60)
    baker = (190, 86, 103)
    sherlock = (38, 116, 116)
    paragraph_colors = {
        1: crabson,
        2: crabson,
        4: baker,
        6: sherlock,
        9: sherlock,
    }
    line_advance = 58
    paragraph_gap = 18

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
