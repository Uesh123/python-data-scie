from PIL import Image, ImageFilter,ImageEnhance

im=Image.open('Screenshot (1).png')
im2=Image.open(r'C:\Users\saroj\Pictures\123.jpeg')

# im2.filter(ImageFilter.EMBOSS).show()
# im2.filter(ImageFilter.CONTOUR).show()
# im2.filter(ImageFilter.FIND_EDGES).show()
# im2.filter(ImageFilter.BLUR).show()
# im2.filter(ImageFilter.SHARPEN).show()
# im2.filter(ImageFilter.SMOOTH).show()
# im2.filter(ImageFilter.MaxFilter(3)).show()
# im2.filter(ImageFilter.MinFilter(3)).show()
# im2.filter(ImageFilter.MedianFilter(5)).show()
# im.filter(ImageFilter.GaussianBlur(100)).show()
# eim=ImageEnhance.Color(im)
# for i in range(-10,11,2):
#     eim.enhance(i).show()
imc=im.copy()
im2_s= im2.resize((200,240))
imc.paste(im2,(0,0))
imc.show()

