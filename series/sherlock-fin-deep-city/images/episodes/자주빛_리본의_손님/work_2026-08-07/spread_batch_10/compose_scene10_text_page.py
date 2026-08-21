from __future__ import annotations

import argparse
import hashlib
import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


EXPECTED_TEXT = """셜록 핀이 물었어요.

“왜 간판을 바꾼 거예요?”

모리가 웃었어요.

“네가 얼마나 잘하는지
보고 싶었어.

간판도 아무렇게나
섞은 게 아니야.
모두 한 칸씩 옮겼지.

너라면 원래 자리쯤
금방 알아볼 수 있잖아?”

셜록 핀이 말했어요.

“알아낼 수 있는 것과
다른 친구들의 일을
마음대로 어지럽히는 건 달라요.

손님들은 길을 잃었고,
가게 주인들은 걱정했어요.”

모리가 잠시 눈을 깜빡였어요.

“……다치지 않아도
곤란하게 만들 수 있구나.
그건 내가 잘못 생각했네.”"""


def extract_scene10_text(script_path: Path) -> str:
    source = script_path.read_text(encoding="utf-8").replace("\r\n", "\n")
    match = re.search(
        r"(?ms)^### 10\s*$.*?^Text:\s*$\n+(.*?)(?=^### 11\s*$)",
        source,
    )
    if not match:
        raise RuntimeError("Could not locate scene 10 Text block")
    body = match.group(1).strip()
    if body != EXPECTED_TEXT:
        raise RuntimeError("Scene 10 text differs from the approved exact text")
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

    body = extract_scene10_text(args.script)
    canvas = Image.open(args.background).convert("RGB")
    canvas = canvas.resize((1054, 1492), Image.Resampling.LANCZOS)
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.truetype(str(args.font), 38)

    paragraphs = [paragraph.splitlines() for paragraph in body.split("\n\n")]
    navy = (46, 55, 79)
    teal = (38, 116, 116)
    purple = (112, 66, 117)
    paragraph_colors = {
        1: teal,
        3: purple,
        4: purple,
        5: purple,
        7: teal,
        8: teal,
        10: purple,
    }
    line_advance = 49
    paragraph_gap = 8

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
