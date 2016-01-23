with open("C:\\v.txt", ) as f:
    some = f.read()

print("".join([i for i in some if i.isalpha()]))
