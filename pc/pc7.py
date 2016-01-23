from PIL import Image

im = Image.open("C:\\o.png")
width, height = im.size
gr = int(height / 2)
r = ""
for i in range(1, width, 7):
    r += chr(im.getpixel((i, gr))[0])
print(r)

l = [105, 110, 116, 101, 103, 114, 105, 116, 121]
r2 = ""
for i in l:
    r2 += chr(i)

print(r2)
