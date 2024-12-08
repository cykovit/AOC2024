import numpy as np

filename = 'input_day08.txt'
with open(filename, 'r') as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]
grid = np.array([list(line) for line in lines])
frequencies = set(grid.flatten()) - {'\n', '.'}

nodes = {freq: {complex(r, c) for r in range(grid.shape[0]) 
                for c in range(grid.shape[1]) if grid[r, c] == freq} 
         for freq in frequencies}

part1_antinodes = {freq: set() for freq in frequencies}
for freq in frequencies:
    for node1 in nodes[freq]:
        for node2 in nodes[freq] - {node1}:
            step = -(node2 - node1)
            current = node1 + step
            if (0 <= current.real < grid.shape[0] and 
                0 <= current.imag < grid.shape[1]):
                part1_antinodes[freq].add(current)

part1_result = len(set().union(*part1_antinodes.values()))

part2_antinodes = {freq: set() for freq in frequencies}
for freq in frequencies:
    for node1 in nodes[freq]:
        for node2 in nodes[freq] - {node1}:
            for direction in [-1, 1]:
                step = direction * (node2 - node1)
                current = node1
                
                for n in range(1, 100):
                    current += step
                    
                    if (0 <= current.real < grid.shape[0] and 
                        0 <= current.imag < grid.shape[1]):
                        part2_antinodes[freq].add(current)
                    else:
                        break

part2_result = len(set().union(*part2_antinodes.values()))

print(f"Part 1 - Unique antinode locations: {part1_result}")
print(f"Part 2 - New unique antinode locations: {part2_result}")
