from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


PAGE_TEXT = """사건 파일
자줏빛 리본의 손님

단서 1
세 간판이 규칙대로
한 칸씩 옮겨졌어요.

단서 2
자줏빛 리본은 곱게 묶여
눈에 띄었어요.

단서 3
소용돌이 카드와 글자 카드는
풀기 좋게 나뉘어 있었어요.

결론
누군가 셜록 핀이 알아보도록
만든 초대장이었어요.
글자 카드는 ‘미역숲’을 가리켰어요."""


def text_width(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont) -> int:
    box = draw.textbbox((0, 0), text, font=font)
    return box[2] - box[0]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--background", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--font", type=Path, default=Path(r"C:\Windows\Fonts\Katuri.ttf"))
    args = parser.parse_args()

    canvas = Image.open(args.background).convert("RGB").resize((1054, 1492), Image.Resampling.LANCZOS)
    draw = ImageDraw.Draw(canvas)

    navy = (46, 55, 79)
    teal = (38, 116, 116)
    gold = (166, 105, 35)
    coral = (190, 83, 72)
    purple = (112, 66, 117)
    cream = (255, 249, 232)

    title_font = ImageFont.truetype(str(args.font), 62)
    subtitle_font = ImageFont.truetype(str(args.font), 34)
    label_font = ImageFont.truetype(str(args.font), 36)
    body_font = ImageFont.truetype(str(args.font), 40)
    conclusion_font = ImageFont.truetype(str(args.font), 37)

    left, right = 210, 906
    title = "사건 파일"
    draw.text(((1054 - text_width(draw, title, title_font)) // 2, 176), title, font=title_font, fill=navy)
    subtitle = "자줏빛 리본의 손님"
    draw.text(((1054 - text_width(draw, subtitle, subtitle_font)) // 2, 252), subtitle, font=subtitle_font, fill=purple)

    clues = [
        (gold, "단서 1", ("세 간판이 규칙대로", "한 칸씩 옮겨졌어요.")),
        (purple, "단서 2", ("자줏빛 리본은 곱게 묶여", "눈에 띄었어요.")),
        (teal, "단서 3", ("소용돌이 카드와 글자 카드는", "풀기 좋게 나뉘어 있었어요.")),
    ]

    y = 330
    card_h = 190
    for color, label, lines in clues:
        draw.rounded_rectangle((left, y, right, y + card_h), radius=34, fill=cream, outline=color, width=5)
        draw.rounded_rectangle((left + 24, y + 25, left + 164, y + 78), radius=22, fill=color)
        label_x = left + 94 - text_width(draw, label, label_font) // 2
        draw.text((label_x, y + 29), label, font=label_font, fill=cream)
        line_y = y + 92
        for line in lines:
            draw.text((left + 42, line_y), line, font=body_font, fill=navy)
            line_y += 47
        y += card_h + 25

    conclusion_top = y + 2
    conclusion_bottom = 1280
    draw.rounded_rectangle(
        (left, conclusion_top, right, conclusion_bottom),
        radius=38,
        fill=(255, 245, 226),
        outline=coral,
        width=6,
    )
    label = "결론"
    draw.rounded_rectangle((left + 24, conclusion_top + 24, left + 156, conclusion_top + 79), radius=23, fill=coral)
    label_x = left + 90 - text_width(draw, label, label_font) // 2
    draw.text((label_x, conclusion_top + 29), label, font=label_font, fill=cream)

    conclusion_lines = (
        "누군가 셜록 핀이 알아보도록",
        "만든 초대장이었어요.",
        "글자 카드는 ‘미역숲’을 가리켰어요.",
    )
    line_y = conclusion_top + 99
    for idx, line in enumerate(conclusion_lines):
        color = teal if idx == 2 else navy
        if text_width(draw, line, conclusion_font) > right - left - 74:
            raise RuntimeError(f"Conclusion line exceeds safe area: {line}")
        draw.text((left + 38, line_y), line, font=conclusion_font, fill=color)
        line_y += 47

    if line_y > conclusion_bottom - 20:
        raise RuntimeError("Conclusion exceeds bottom safe area")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(args.output, format="PNG", optimize=True)
    digest = hashlib.sha256(PAGE_TEXT.encode("utf-8")).hexdigest().upper()
    print(f"output={args.output}")
    print(f"size={canvas.width}x{canvas.height}")
    print(f"text_sha256={digest}")
    print(f"bottom={line_y}")


if __name__ == "__main__":
    main()
