import re
from math import floor

with open('input_day13.txt') as f:
    groups = [
        list(map(int, re.findall("\\d+", g))) for g in f.read().strip().split("\n\n")
    ]

def price(ax, ay, bx, by, tx, ty, offset=0):
    tx += offset
    ty += offset
    det = ax * by - ay * bx
    if det == 0:
        return 0  

    a = (tx * by - ty * bx) / det
    b = (ax * ty - ay * tx) / det

    if a >= 0 and b >= 0 and a.is_integer() and b.is_integer():
        return 3 * int(a) + int(b)

    return 0

print(f"Part 1 - Total tokens:", sum(price(*g) for g in groups))
print(f"Part 2 - New total tokens:", sum(price(*g, 10000000000000) for g in groups))
