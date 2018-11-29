#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont

def addNum(img):
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('/Library/Fonts/AppleMyungjo.ttf', 30)
    draw.text((img.size[0]-40, 0), '99', fill='#ff0000', font=font)
    img.save('result.png', 'png')
    return 0
if __name__ == '__main__':
    image = Image.open('avatar.png')
    addNum(image)
