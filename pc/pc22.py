from PIL import Image

im = Image.open('white.gif')
r = []
try:
    while 1:
        im.seek(im.tell() + 1)
        x, y = im.getbbox()[0:2]
        r.append((x - 100, y - 100))
except EOFError:
    pass
print(r)

nm = Image.new(im.mode, im.size, 0)

pos = (30, 30)
letter = 1
for a1, a2 in r:
    if (a1, a2) == (0, 0):
        letter += 1
        pos = 30 * letter, 30 * letter
    nm.putpixel(pos, 255)
    pos = pos[0] + a1, pos[1] + a2

nm.save("pc22.gif")
