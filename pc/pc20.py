"""
X-Powered-By: PHP/5.3.3-7+squeeze19
Content-Type: image/jpeg
Content-Range: bytes 0-30202/2123456789
Connection: close
Date: Thu, 14 Jan 2016 04:14:19 GMT
Server: lighttpd/1.4.28
"""

import requests
from requests.auth import HTTPBasicAuth

url = "http://www.pythonchallenge.com/pc/hex/idiot2.html"
url2 = "http://www.pythonchallenge.com/pc/hex/unreal.jpg"
headers = {"Range": 'bytes=1152983631-'}
r = requests.get(url2, headers=headers, auth=HTTPBasicAuth('butter', 'fly'))

# print(r.content)
# print(r.headers['Content-Range'])
data = r.content
# print(data[:20])
with open("pc20.zip", 'wb') as f:
    f.write(data)
