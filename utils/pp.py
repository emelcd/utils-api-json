from PIL import Image, ImageFilter, ImageEnhance

img = Image.open('land.jpg')

img = img.filter(ImageFilter.SMOOTH())
img = img.filter(ImageFilter.DETAIL())
img=img.convert("L")
img.show()