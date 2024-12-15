# Read input and construct the board
with open('input_day12.txt') as f:
    board = {
        i + 1j * j: x
        for i, l in enumerate(f.read().strip().split("\n"))
        for j, x in enumerate(l)
    }

four_sides = {1, -1, 1j, -1j}

graph = {}
for z in board:
    graph[z] = []
    for dz in four_sides:
        neighbor = z + dz
        if board.get(z) == board.get(neighbor):
            graph[z].append(neighbor)

def dfs(node, graph, visited):
    stack = [node]
    component = []
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            component.append(current)
            stack.extend(graph[current])
    return component

visited = set()
components = []
for node in graph:
    if node not in visited:
        component = dfs(node, graph, visited)
        components.append(component)

part2 = 0
for comp in components:
    wall = {(z, dz * 1j) for dz in four_sides for z in comp if z + dz not in comp}
    part2 += len(comp) * sum((z + dz, dz) not in wall for (z, dz) in wall)

print(part2)
