import numpy as np

def count(p, rmin, rmax, cmin, cmax):
    return sum(cmin <= c < cmax and rmin <= r < rmax for c, r in p)


def part1():
    pos = [[(p[0] + 100 * v[0]) % cols, (p[1] + 100 * v[1]) % rows] for p, v in zip(positions, velocities)]
    
    a = count(pos, 0, rows // 2, 0, cols // 2)
    b = count(pos, rows // 2 + 1, rows, 0, cols // 2)
    c = count(pos, 0, rows // 2, cols // 2 + 1, cols)
    d = count(pos, rows // 2 + 1, rows, cols // 2 + 1, cols)
    
    return a * b * c * d


def part2():
    store = np.zeros((10000, len(positions), 2))
    
    for it in range(store.shape[0]):
        for i, (p, v) in enumerate(zip(positions, velocities)):
            store[it, i] = [(p[0] + it * v[0]) % cols, (p[1] + it * v[1]) % rows]
    
    return np.argmin(np.var(store, axis=1)[:, 1] * np.var(store, axis=1)[:, 0])

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

print(f"Part 1 - Safety factor:", part1())
print(f"Part 2 - Fewest number of seconds:", part2())
