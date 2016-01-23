# a = 1, 11, 21, 1211, 111221,
# look and say, 1"1">>11, 2"1">>21, 1"2"1"1">>1211 oeis.org
from itertools import groupby


def say(number):
    num_list = [list(g) for k, g in groupby(str(number))]
    r = []
    for i in num_list:
        r.extend([str(len(i)), i[0]])
    return int("".join(r))


num = 1
for j in range(30):
    print([j + 1, len(str(say(num)))])
    num = say(num)
