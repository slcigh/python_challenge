# coding=utf-8
from PIL import Image


def bfs(graph):
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    start = (639, 0)
    goal = (1, 640)
    wall = (255, 255, 255, 255)
    q = [[start, []]]
    while q:
        cur, visited = q.pop(0)
        for dx, dy in dirs:
            x, y = cur[0] + dx, cur[1] + dy
            if -1 < x < 641 and -1 < y < 641 and (x, y) not in visited:
                pos = (x, y)
                if graph.getpixel(pos) != wall:
                    if pos == goal:
                        return visited + [cur]
                    else:
                        q.append([pos, visited + [cur]])


im = Image.open('maze.png')

m = bfs(im)
f = open('maze.zip', 'wb')
for i in m[1::2]:
    f.write(str.encode(chr(im.getpixel(i)[0])))
f.close()

"""
print(im.size)
print(im.getpixel((639, 0)))  # start
print(im.getpixel((639, 1)))
print(im.getpixel((637, 3)))
print(im.getpixel((1, 640)))  # goal
print(im.getpixel((635, 55)))
print(im.getpixel((637, 55)))
print(im.getpixel((636, 55)))
"""

"""
for p in m:
    im.putpixel(p, (0, 255,) * 2)

im.save("pc24-t.png")
"""

"""
from timeit import timeit

print(timeit('bfs(im)', setup='from __main__ import bfs, im', number=1))
"""
# test change
