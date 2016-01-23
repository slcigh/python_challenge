from PIL import Image

im = Image.open(r"C:\pc16.gif")
w, h = im.size
'''
# print(im.getpixel((434, 0)))
# print([im.getpixel((i, 0)) for i in range(w)])
# print([im.getpixel((i, 1)) for i in range(w)])
#  251, 195, 195, 195, 195, 195, 251
# 195 only appearance total 5 times and in a row
# pos = find(195) , range(pos) range(pos,edge)
# for i in range(w):
#     if im.getpixel((i, 99)) == 195:
#         print(i)
'''
straight = Image.new(im.mode, im.size, 0)

pixel_list = [[im.getpixel((i, j)) for i in range(w)] for j in range(h)]
r = []
for i in pixel_list:
    pos = i.index(195)
    r.append(i[pos:] + i[0:pos])

for j in range(h):
    for i in range(w):
        straight.putpixel((i, j), r[j][i])

straight.save("pc16.gif")
