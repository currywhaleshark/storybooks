from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


WIDTH = 1054
HEIGHT = 1492
TITLE = "심해탐정 셜록 핀\n자줏빛 리본의 손님"


def make_cream_canvas() -> Image.Image:
    canvas = Image.new("RGB", (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(canvas)
    top = (253, 248, 235)
    bottom = (247, 239, 219)
    for y in range(HEIGHT):
        t = y / (HEIGHT - 1)
        color = tuple(round(a * (1 - t) + b * t) for a, b in zip(top, bottom))
        draw.line((0, y, WIDTH, y), fill=color)
    return canvas


def extract_object(source: Image.Image, box: tuple[int, int, int, int]) -> Image.Image:
    crop = source.crop(box).convert("RGBA")
    pixels = crop.load()
    for y in range(crop.height):
        for x in range(crop.width):
            r, g, b, _ = pixels[x, y]
            distance = ((r - 250) ** 2 + (g - 246) ** 2 + (b - 235) ** 2) ** 0.5
            alpha = max(0, min(255, round((distance - 10) * 7)))
            pixels[x, y] = (r, g, b, alpha)
    bbox = crop.getbbox()
    if bbox is None:
        raise RuntimeError("Could not extract prop from reference sheet")
    return crop.crop(bbox)


def resize_width(image: Image.Image, width: int) -> Image.Image:
    height = round(image.height * width / image.width)
    return image.resize((width, height), Image.Resampling.LANCZOS)


def paste_with_shadow(canvas: Image.Image, prop: Image.Image, position: tuple[int, int]) -> None:
    alpha = prop.getchannel("A")
    shadow = Image.new("RGBA", prop.size, (55, 43, 74, 0))
    shadow.putalpha(alpha.filter(ImageFilter.GaussianBlur(7)).point(lambda value: value * 55 // 255))
    canvas.paste(shadow, (position[0] + 5, position[1] + 8), shadow)
    canvas.paste(prop, position, prop)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--props", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--font", type=Path, default=Path(r"C:\Windows\Fonts\Katuri.ttf"))
    args = parser.parse_args()

    canvas = make_cream_canvas().convert("RGBA")
    draw = ImageDraw.Draw(canvas)

    coral = (226, 127, 113, 215)
    teal = (82, 151, 145, 180)
    navy = (43, 54, 78, 255)
    purple = (104, 55, 104, 255)
    gold = (190, 138, 57, 180)

    draw.rounded_rectangle((142, 54, 1010, 1438), radius=72, outline=coral, width=4)
    draw.rounded_rectangle((160, 74, 992, 1418), radius=60, outline=teal, width=3)

    font_series = ImageFont.truetype(str(args.font), 57)
    font_episode = ImageFont.truetype(str(args.font), 82)
    center_x = 575
    series_y = 424
    episode_y = 558

    draw.text((center_x, series_y), "심해탐정 셜록 핀", font=font_series, fill=navy, anchor="mm")
    draw.text((center_x, episode_y), "자줏빛 리본의 손님", font=font_episode, fill=purple, anchor="mm")

    draw.line((430, 670, 720, 670), fill=gold, width=3)
    draw.polygon(((575, 660), (585, 670), (575, 680), (565, 670)), fill=gold)

    props = Image.open(args.props).convert("RGB")
    card = resize_width(extract_object(props, (448, 70, 690, 420)), 170).rotate(
        -7, resample=Image.Resampling.BICUBIC, expand=True
    )
    ribbon = resize_width(extract_object(props, (52, 240, 430, 390)), 250).rotate(
        5, resample=Image.Resampling.BICUBIC, expand=True
    )

    paste_with_shadow(canvas, card, (374, 882))
    paste_with_shadow(canvas, ribbon, (555, 1114))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    canvas.convert("RGB").save(args.output, format="PNG", optimize=True)

    title_hash = hashlib.sha256(TITLE.encode("utf-8")).hexdigest().upper()
    print(f"output={args.output}")
    print(f"size={WIDTH}x{HEIGHT}")
    print(f"title_sha256={title_hash}")
    print("font=Katuri.ttf series=57px episode=82px")


if __name__ == "__main__":
    main()

