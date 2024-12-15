import numpy as np

def part2():
    store = np.zeros((10000, len(positions), 2))
    
    for it in range(store.shape[0]):
        for i, (p, v) in enumerate(zip(positions, velocities)):
            store[it, i] = [(p[0] + it * v[0]) % cols, (p[1] + it * v[1]) % rows]
    
    ## find time step with minimum variance for y & x
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

print(part2())
