#!/usr/bin/env python3
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# image things
font = ImageFont.truetype("arial.ttf", 100)

def generate(token_id, rare, blue):
    color = (0,0,255) if blue else (255,255,255)

    img = Image.new('RGB', (400, 400), (0, 0, 0))
    d = ImageDraw.Draw(img)
    d.text((0, 0), str(token_id), fill=color ,font = font)

    if rare:
        d.text((0,200), "Rare!", fill=color, font=font)
    return img
