with open("C:\\e.gfx", "rb") as f:
    gfx = f.read()

for i in range(5):
    open("pc12-%d.gif" % i, "wb").write(gfx[i::5])
