s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. " \
    "rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr" \
    " ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. " \
    "lmu ynnjw ml rfc spj."

r = ""
for i in s:
    if i == "y":
        r += "a"
    elif i == "z":
        r += "b"
    elif i.islower():
        r += chr(ord(i) + 2)
    else:
        r += i

print(r)
