import requests
# get"info=you+should+have+followed+busynothing..." from flidder
# [Cookie(version=0, name='info', value='B',
# value ...
from urllib.parse import unquote_plus
import bz2

num = 12345
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing="
s = ""
'''
for i in range(200):
    r = requests.get(url+str(num))
    ck = str(list(r.cookies))
    #print(ck)
    value = re.findall(r"value=\'(.*)\'\,\spo", ck)
    if value:
        print(value[0])
        s += value[0]
    try:
        num = re.findall(r'busynothing is (\d+)', r.text)[0]
    except:
        print(s)
        raise IndexError
'''

ss = "BZh91AY%26SY%94%3A%E2I%00%00%21%19%8" \
     "0P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%D4%D1%E2%8" \
     "D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E" \
     "1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96K" \
     "O%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90"

z = unquote_plus(ss, "latin-1").encode("latin-1")
print(z)
print(bz2.decompress(z))

url2 = "http://www.pythonchallenge.com/pc/stuff/violin.php"
headers = {"Cookie": "info=the+flowers+are+on+their+way"}
r = requests.get(url2, headers=headers)
print(r.text)
