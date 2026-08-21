from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


CARD_W = 150
CARD_H = 200
PAGE_SIZE = (1054, 1492)
JAMO = ("ㅁ", "ㅣ", "ㅇ", "ㅕ", "ㄱ", "ㅅ", "ㅜ", "ㅍ")


def text_size(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont) -> tuple[int, int]:
    box = draw.textbbox((0, 0), text, font=font)
    return box[2] - box[0], box[3] - box[1]


def centered_text(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    text: str,
    font: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int],
    y_adjust: int = -6,
) -> None:
    x1, y1, x2, y2 = box
    w, h = text_size(draw, text, font)
    draw.text(((x1 + x2 - w) // 2, (y1 + y2 - h) // 2 + y_adjust), text, font=font, fill=fill)


def draw_corner_marks(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], color: tuple[int, int, int]) -> None:
    x1, y1, x2, y2 = box
    inset = 14
    arm = 18
    points = (
        ((x1 + inset, y1 + inset + arm), (x1 + inset, y1 + inset), (x1 + inset + arm, y1 + inset)),
        ((x2 - inset - arm, y1 + inset), (x2 - inset, y1 + inset), (x2 - inset, y1 + inset + arm)),
        ((x1 + inset, y2 - inset - arm), (x1 + inset, y2 - inset), (x1 + inset + arm, y2 - inset)),
        ((x2 - inset - arm, y2 - inset), (x2 - inset, y2 - inset), (x2 - inset, y2 - inset - arm)),
    )
    for p1, p2, p3 in points:
        draw.line((p1, p2, p3), fill=color, width=3, joint="curve")


def draw_card(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    letter: str,
    color: tuple[int, int, int],
    font: ImageFont.FreeTypeFont,
) -> None:
    x, y = xy
    box = (x, y, x + CARD_W, y + CARD_H)
    cream = (255, 249, 232)
    navy = (35, 48, 72)
    draw.rounded_rectangle(box, radius=19, fill=cream, outline=(74, 66, 79), width=8)
    draw.rounded_rectangle((x + 7, y + 7, x + CARD_W - 7, y + CARD_H - 7), radius=13, outline=color, width=6)
    draw.rounded_rectangle((x + 16, y + 16, x + CARD_W - 16, y + CARD_H - 16), radius=8, outline=color, width=2)
    draw_corner_marks(draw, (x + 6, y + 6, x + CARD_W - 6, y + CARD_H - 6), color)
    centered_text(draw, box, letter, font, navy, y_adjust=-9)


def draw_slot(draw: ImageDraw.ImageDraw, xy: tuple[int, int], color: tuple[int, int, int]) -> None:
    x, y = xy
    box = (x, y, x + CARD_W, y + CARD_H)
    pale = tuple(min(255, channel + 155) for channel in color)
    draw.rounded_rectangle(box, radius=20, fill=(255, 252, 240), outline=pale, width=6)
    draw.rounded_rectangle((x + 12, y + 12, x + CARD_W - 12, y + CARD_H - 12), radius=12, outline=color, width=3)
    draw_corner_marks(draw, (x + 4, y + 4, x + CARD_W - 4, y + CARD_H - 4), color)


def draw_cut_guide(draw: ImageDraw.ImageDraw, xy: tuple[int, int]) -> None:
    x, y = xy
    guide = (170, 166, 156)
    pad = 8
    x1, y1, x2, y2 = x - pad, y - pad, x + CARD_W + pad, y + CARD_H + pad
    dash = 10
    gap = 7
    for start in range(x1, x2, dash + gap):
        draw.line((start, y1, min(start + dash, x2), y1), fill=guide, width=2)
        draw.line((start, y2, min(start + dash, x2), y2), fill=guide, width=2)
    for start in range(y1, y2, dash + gap):
        draw.line((x1, start, x1, min(start + dash, y2)), fill=guide, width=2)
        draw.line((x2, start, x2, min(start + dash, y2)), fill=guide, width=2)


def draw_board(
    background: Path,
    output: Path,
    katuri: Path,
) -> None:
    canvas = Image.open(background).convert("RGB").resize(PAGE_SIZE, Image.Resampling.LANCZOS)
    draw = ImageDraw.Draw(canvas)
    navy = (46, 55, 79)
    teal = (38, 126, 128)
    gold = (184, 117, 29)
    coral = (190, 83, 72)
    purple = (124, 70, 130)
    cream = (255, 249, 232)

    title_font = ImageFont.truetype(str(katuri), 60)
    instruction_font = ImageFont.truetype(str(katuri), 33)
    result_font = ImageFont.truetype(str(katuri), 55)
    arrow_font = ImageFont.truetype(str(katuri), 48)

    title = "한글 놀이"
    w, _ = text_size(draw, title, title_font)
    draw.text(((1054 - w) // 2, 158), title, font=title_font, fill=navy)
    for idx, line in enumerate(("이야기 속 글자 카드를", "알맞은 칸에 놓아 보세요!")):
        w, _ = text_size(draw, line, instruction_font)
        draw.text(((1054 - w) // 2, 232 + idx * 40), line, font=instruction_font, fill=coral)

    rows = (
        (("slot", "slot"), "미", teal, 350),
        (("slot", "slot", "slot"), "역", gold, 630),
        (("slot", "slot", "slot"), "숲", purple, 910),
    )
    for slots, result, color, y in rows:
        slot_gap = 16
        arrow_w = 66
        result_w = 128
        total = len(slots) * CARD_W + (len(slots) - 1) * slot_gap + arrow_w + result_w
        x = 572 - total // 2
        for index in range(len(slots)):
            draw_slot(draw, (x, y), color)
            x += CARD_W
            if index != len(slots) - 1:
                x += slot_gap
        centered_text(draw, (x, y, x + arrow_w, y + CARD_H), "→", arrow_font, navy)
        x += arrow_w
        result_box = (x, y + 20, x + result_w, y + CARD_H - 20)
        draw.rounded_rectangle(result_box, radius=28, fill=cream, outline=color, width=6)
        centered_text(draw, result_box, result, result_font, color, y_adjust=-8)

    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output, format="PNG", optimize=True)


def draw_card_sheet(output: Path, katuri: Path, card_font_path: Path) -> None:
    canvas = Image.new("RGB", PAGE_SIZE, (255, 251, 239))
    draw = ImageDraw.Draw(canvas)
    navy = (46, 55, 79)
    teal = (38, 126, 128)
    gold = (184, 117, 29)
    coral = (190, 83, 72)
    purple = (124, 70, 130)

    title_font = ImageFont.truetype(str(katuri), 54)
    instruction_font = ImageFont.truetype(str(katuri), 29)
    card_font = ImageFont.truetype(str(card_font_path), 88)

    title = "오려 쓰는 글자 카드"
    w, _ = text_size(draw, title, title_font)
    draw.text(((1054 - w) // 2, 130), title, font=title_font, fill=navy)
    subtitle = "점선을 따라 오려서 31페이지에 놓아 보세요."
    w, _ = text_size(draw, subtitle, instruction_font)
    draw.text(((1054 - w) // 2, 202), subtitle, font=instruction_font, fill=coral)

    groups = (
        (("ㅁ", "ㅣ"), teal, 340),
        (("ㅇ", "ㅕ", "ㄱ"), gold, 635),
        (("ㅅ", "ㅜ", "ㅍ"), purple, 930),
    )
    for letters, color, y in groups:
        gap = 46
        total = len(letters) * CARD_W + (len(letters) - 1) * gap
        x = (1054 - total) // 2
        for letter in letters:
            draw_cut_guide(draw, (x, y))
            draw_card(draw, (x, y), letter, color, card_font)
            x += CARD_W + gap

    note = "활동판과 카드 시트를 같은 크기(100%)로 인쇄하세요."
    w, _ = text_size(draw, note, instruction_font)
    draw.text(((1054 - w) // 2, 1248), note, font=instruction_font, fill=navy)
    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output, format="PNG", optimize=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--background", required=True, type=Path)
    parser.add_argument("--board-output", required=True, type=Path)
    parser.add_argument("--cards-output", required=True, type=Path)
    parser.add_argument("--katuri", type=Path, default=Path(r"C:\Windows\Fonts\Katuri.ttf"))
    parser.add_argument("--card-font", type=Path, default=Path(r"C:\Windows\Fonts\malgunbd.ttf"))
    args = parser.parse_args()

    draw_board(args.background, args.board_output, args.katuri)
    draw_card_sheet(args.cards_output, args.katuri, args.card_font)
    digest = hashlib.sha256("".join(JAMO).encode("utf-8")).hexdigest().upper()
    print(f"board={args.board_output}")
    print(f"cards={args.cards_output}")
    print(f"size={PAGE_SIZE[0]}x{PAGE_SIZE[1]}")
    print(f"card_size={CARD_W}x{CARD_H}")
    print(f"jamo_sha256={digest}")


if __name__ == "__main__":
    main()
