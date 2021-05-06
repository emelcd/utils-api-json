from PIL import Image, ImageFilter, ImageEnhance
import os
def show_img(f):
    img = Image.open(f)
    try:
        os.remove('tmp\max.png')
    except:
        pass        
    img = img.filter(ImageFilter.SMOOTH())
    img = img.filter(ImageFilter.DETAIL())
    img = img.convert("L")
    img.save('tmp\max.png')
    