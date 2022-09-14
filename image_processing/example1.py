from PIL import Image

im=Image.open('Screenshot (1).png')
im2=Image.open(r'C:\Users\saroj\Pictures\123.jpeg')

print(im)

im.rotate(90).show()
im2.rotate(45).show()
