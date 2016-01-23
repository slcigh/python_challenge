import re

import requests

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
num = 12345
for i in range(500):
    r = requests.get(url + str(num)).text
    try:
        num = re.findall(r'nothing is (\d+)', r)[0]
        print(r)
    except:
        num = int(num) / 2  # Yes. Divide by two and keep going.
        print(r)
