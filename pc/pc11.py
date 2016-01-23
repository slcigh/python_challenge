from PIL import Image

im = Image.open("C:\\cave.jpg")
w, h = im.size
for i in range(w):
    for j in range(h):
        if (i + j) % 2 == 1:
            im.putpixel((i, j), 0)
im.save("pc11.jpg")
