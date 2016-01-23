import codecs
import re
from difflib import ndiff

with open(r"C:\delta.txt") as f:
    data = f.read()

list_d = data.split("\n")
d1 = [i[0:53] for i in list_d]
d2 = [i[56:] for i in list_d]


def unhex(s):
    return codecs.getdecoder('hex')(re.sub('[^0-9a-fA-F]', '', s))[0]


diff = list(ndiff(d1, d2))

with open("pc18-0.png", "wb") as ff:
    for i in diff:
        if i[0] == " ":
            ff.write(unhex(i))

with open("pc18-1.png", "wb") as ff:
    for i in diff:
        if i[0] == "+":
            ff.write(unhex(i))

with open("pc18-2.png", "wb") as ff:
    for i in diff:
        if i[0] == "-":
            ff.write(unhex(i))
