import numpy as np

def count(p, rmin, rmax, cmin, cmax):
    return sum(cmin <= c < cmax and rmin <= r < rmax for c, r in p)

def part1():
    ## calc new pos after velocity is applied
    pos = [[(p[0] + 100 * v[0]) % cols, (p[1] + 100 * v[1]) % rows] for p, v in zip(positions, velocities)]
    
    a = count(pos, 0, rows // 2, 0, cols // 2)
    b = count(pos, rows // 2 + 1, rows, 0, cols // 2)
    c = count(pos, 0, rows // 2, cols // 2 + 1, cols)
    d = count(pos, rows // 2 + 1, rows, cols // 2 + 1, cols)
    
    return a * b * c * d

rows, cols = 103, 101

with open('input_day14.txt') as f:
    data = f.readlines()

positions = []
velocities = []

for line in data:
    parts = line.split(' ')
    pos = list(map(int, parts[0].split('=')[1].split(',')))
    vel = list(map(int, parts[1].split('=')[1].split(',')))
    
    positions.append(pos)
    velocities.append(vel)

print(part1())
