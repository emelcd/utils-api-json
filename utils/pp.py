from PIL import Image, ImageFilter, ImageEnhance
import os
def show_img(f):
    img = Image.open(f)
    os.remove('tmp\max.png')
    img = img.filter(ImageFilter.SMOOTH())
    img = img.filter(ImageFilter.DETAIL())
    img = img.convert("L")
    img.save('tmp\max.png')
    