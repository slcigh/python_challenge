import pickle

# from urllib import request

# url = 'http://www.pythonchallenge.com/pc/def/banner.p'
# data = pickle.loads(request.urlopen(url).read())

with open("C:\\banner.p", "rb") as f:
    some = pickle.load(f)
print(some)

for i in some:
    print("".join([j[0] * j[1] for j in i]))
