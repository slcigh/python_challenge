from zipfile import ZipFile

num = 90052
r = []
with ZipFile("C:\\channel.zip") as myzip:
    for i in range(909):
        with myzip.open(str(num) + ".txt") as myfile:
            # decode bytes to string
            cm = myzip.getinfo(str(num) + ".txt").comment.decode()
            r.append(cm)
            s = str(myfile.read())
            pos = s.find("is")
            num = s[pos + 3:-1]

print("".join(r))
