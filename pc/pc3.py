import re

with open(r"C:\pc3.txt") as f:
    data = f.read()

pattern = re.compile(r"[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]")
r = "".join(pattern.findall(data))
print(r)
