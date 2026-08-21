from __future__ import annotations

import argparse
import hashlib
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


LOGO_TEXT = "심해탐정 셜록 핀"


def text_size(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont) -> tuple[int, int]:
    box = draw.textbbox((0, 0), text, font=font)
    return box[2] - box[0], box[3] - box[1]


def spiral_points(cx: float, cy: float, start_r: float, end_r: float, turns: float, count: int) -> list[tuple[float, float]]:
    points = []
    for i in range(count):
        t = i / (count - 1)
        angle = turns * 2 * math.pi * t - math.pi / 2
        radius = start_r + (end_r - start_r) * t
        points.append((cx + math.cos(angle) * radius, cy + math.sin(angle) * radius))
    return points


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
    gold = (186, 126, 43)
    cream = (255, 249, 232)
    center_x = 550

    # Magnifying-glass emblem.
    ring_box = (center_x - 102, 455, center_x + 102, 659)
    draw.ellipse(ring_box, fill=cream, outline=gold, width=16)
    draw.ellipse((center_x - 78, 479, center_x + 78, 635), outline=teal, width=5)
    draw.line((center_x + 73, 630, center_x + 158, 715), fill=gold, width=24)
    draw.line((center_x + 78, 625, center_x + 163, 710), fill=(126, 78, 38), width=6)
    spiral = spiral_points(center_x, 557, 8, 60, 2.25, 110)
    draw.line(spiral, fill=teal, width=12, joint="curve")

    font = ImageFont.truetype(str(args.font), 72)
    w, _ = text_size(draw, LOGO_TEXT, font)
    draw.text((center_x - w // 2, 790), LOGO_TEXT, font=font, fill=navy)

    line_y = 922
    draw.line((center_x - 155, line_y, center_x - 20, line_y), fill=gold, width=4)
    draw.line((center_x + 20, line_y, center_x + 155, line_y), fill=gold, width=4)
    diamond = ((center_x, line_y - 12), (center_x + 12, line_y), (center_x, line_y + 12), (center_x - 12, line_y))
    draw.polygon(diamond, fill=gold)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(args.output, format="PNG", optimize=True)
    digest = hashlib.sha256(LOGO_TEXT.encode("utf-8")).hexdigest().upper()
    print(f"output={args.output}")
    print(f"size={canvas.width}x{canvas.height}")
    print(f"text_sha256={digest}")


if __name__ == "__main__":
    main()
