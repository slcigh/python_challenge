import bz2
import zlib

pack = open('pc20\package.pack', "rb").read()
unpack = zlib.decompress(pack)


def uncompress(data, logs):
    if data[:2] == b'x\x9c':
        logs.append(" ")
        return zlib.decompress(data), logs
    elif data[:2] == b'BZ':
        logs.append("*")
        return bz2.decompress(data), logs
    elif data[-2:] == b'\x9cx':
        logs.append("#")
        return zlib.decompress(data[::-1]), logs
    elif data[-2:] == b'ZB':
        logs.append("@")
        return bz2.decompress(data[::-1]), logs
    else:
        raise ValueError


logs = []

while True:
    try:
        unpack, logs = uncompress(unpack, logs)
    except ValueError:
        print(unpack)
        for i in "".join(logs).split("#"):
            print(i)
        break
