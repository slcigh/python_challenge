from PIL import Image

im = Image.open("C:\\wire.png")
# print(im.mode)
spiral = Image.new("RGB", (100, 100), 0)

up, left, down, right = 0, 0, 99, 99
direct = 0  # 0: go right   1: go down  2: go left  3: go up
z = 0
while left <= right:
    if direct == 0:
        for i in range(left, right + 1):
            spiral.putpixel((up, i), im.getpixel((z, 0)))
            z += 1
        up += 1
    if direct == 1:
        for i in range(up, down + 1):
            spiral.putpixel((i, right), im.getpixel((z, 0)))
            z += 1
        right -= 1
    if direct == 2:
        for i in range(right, left - 1, -1):
            spiral.putpixel((down, i), im.getpixel((z, 0)))
            z += 1
        down -= 1
    if direct == 3:
        for i in range(down, up - 1, -1):
            spiral.putpixel((i, left), im.getpixel((z, 0)))
            z += 1
        left += 1
    direct = (direct + 1) % 4

spiral.save("pc14.jpg")

'''
        up = 0; left = 0
        down = len(matrix)-1
        right = len(matrix[0])-1
        direct = 0  # 0: go right   1: go down  2: go left  3: go up
        res = []
        while True:
            if direct == 0:
                for i in range(left, right+1):
                    res.append(matrix[up][i])
                up += 1
            if direct == 1:
                for i in range(up, down+1):
                    res.append(matrix[i][right])
                right -= 1
            if direct == 2:
                for i in range(right, left-1, -1):
                    res.append(matrix[down][i])
                down -= 1
            if direct == 3:
                for i in range(down, up-1, -1):
                    res.append(matrix[i][left])
                left += 1
            if up > down or left > right: return res
            direct = (direct+1) % 4
'''
