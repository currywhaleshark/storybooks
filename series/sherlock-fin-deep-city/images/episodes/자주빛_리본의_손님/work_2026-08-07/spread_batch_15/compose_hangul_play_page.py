from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


PAGE_TEXT = """한글 놀이
글자 카드를 합쳐 보세요!

ㅁ + ㅣ = 미
ㅇ + ㅕ + ㄱ = 역
ㅅ + ㅜ + ㅍ = 숲

미 + 역 + 숲 = 미역숲"""


def text_size(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont) -> tuple[int, int]:
    box = draw.textbbox((0, 0), text, font=font)
    return box[2] - box[0], box[3] - box[1]


def centered_text(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    text: str,
    font: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int],
) -> None:
    x1, y1, x2, y2 = box
    w, h = text_size(draw, text, font)
    draw.text(((x1 + x2 - w) // 2, (y1 + y2 - h) // 2 - 5), text, font=font, fill=fill)


def draw_equation(
    draw: ImageDraw.ImageDraw,
    y: int,
    jamo: tuple[str, ...],
    result: str,
    color: tuple[int, int, int],
    card_font: ImageFont.FreeTypeFont,
    symbol_font: ImageFont.FreeTypeFont,
    result_font: ImageFont.FreeTypeFont,
) -> None:
    cream = (255, 249, 232)
    navy = (46, 55, 79)
    card_w, card_h = 88, 92
    result_w = 116
    gap_symbol = 52
    equal_w = 58
    total = len(jamo) * card_w + (len(jamo) - 1) * gap_symbol + equal_w + result_w
    x = 560 - total // 2

    for index, letter in enumerate(jamo):
        card = (x, y, x + card_w, y + card_h)
        draw.rounded_rectangle(card, radius=24, fill=cream, outline=color, width=5)
        centered_text(draw, card, letter, card_font, color)
        x += card_w
        if index != len(jamo) - 1:
            centered_text(draw, (x, y, x + gap_symbol, y + card_h), "+", symbol_font, navy)
            x += gap_symbol

    centered_text(draw, (x, y, x + equal_w, y + card_h), "=", symbol_font, navy)
    x += equal_w
    result_box = (x, y - 7, x + result_w, y + card_h + 7)
    draw.rounded_rectangle(result_box, radius=29, fill=color)
    centered_text(draw, result_box, result, result_font, cream)


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
    subtitle_font = ImageFont.truetype(str(args.font), 35)
    card_font = ImageFont.truetype(str(args.font), 53)
    symbol_font = ImageFont.truetype(str(args.font), 44)
    result_font = ImageFont.truetype(str(args.font), 51)
    final_font = ImageFont.truetype(str(args.font), 43)

    title = "한글 놀이"
    w, _ = text_size(draw, title, title_font)
    draw.text(((1054 - w) // 2, 176), title, font=title_font, fill=navy)
    subtitle = "글자 카드를 합쳐 보세요!"
    w, _ = text_size(draw, subtitle, subtitle_font)
    draw.text(((1054 - w) // 2, 258), subtitle, font=subtitle_font, fill=coral)

    draw_equation(draw, 382, ("ㅁ", "ㅣ"), "미", teal, card_font, symbol_font, result_font)
    draw_equation(draw, 626, ("ㅇ", "ㅕ", "ㄱ"), "역", gold, card_font, symbol_font, result_font)
    draw_equation(draw, 870, ("ㅅ", "ㅜ", "ㅍ"), "숲", purple, card_font, symbol_font, result_font)

    final_box = (224, 1090, 932, 1270)
    draw.rounded_rectangle(final_box, radius=38, fill=(255, 245, 226), outline=coral, width=6)
    final_text = "미 + 역 + 숲 = 미역숲"
    centered_text(draw, final_box, final_text, final_font, teal)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(args.output, format="PNG", optimize=True)
    digest = hashlib.sha256(PAGE_TEXT.encode("utf-8")).hexdigest().upper()
    print(f"output={args.output}")
    print(f"size={canvas.width}x{canvas.height}")
    print(f"text_sha256={digest}")
    print("jamo_cards=8 result_syllables=3 final_word=미역숲")


if __name__ == "__main__":
    main()
