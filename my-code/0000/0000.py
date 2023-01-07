from PIL import ImageDraw,Image
import os

with Image.open("bilibili.webp") as im:
    draw = ImageDraw.Draw(im)
    draw.text(xy=(im.width-10,0),text='9',fill='red')
    im.save('0000out.png')