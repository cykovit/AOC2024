def racetrack_pos(target_elements):
    return {row + 1j * col for row in range(rows) for col in range(cols) if racetrack[row][col] in target_elements}

def remake_path(current_pos, visited_nodes):
    path = []
    while current_pos:
        path.append(current_pos)
        current_pos = visited_nodes[current_pos][0]
    return path[::-1]

def calc_distance(pos1, pos2):
    return abs(pos1.real - pos2.real) + abs(pos1.imag - pos2.imag)

def bfs(start_pos):
    visited_nodes = {start_pos: (None, 0)}  
    queue = [start_pos]  
    while queue:
        current_pos = queue.pop(0)  
        for direction in (1, -1, 1j, -1j):  
            neighbor = current_pos + direction
            if neighbor in track_pos and neighbor not in visited_nodes:
                visited_nodes[neighbor] = (current_pos, visited_nodes[current_pos][1] + 1)
                queue.append(neighbor)
    return visited_nodes

def calc_cheat(cheat_duration):
    cheat_savings = {}
    for i, start_pos in enumerate(opti_path):
        for end_pos in opti_path[i + 1:]:
            distance = calc_distance(start_pos, end_pos)
            if distance <= cheat_duration and visited_from_end[end_pos][1] + distance < visited_from_end[start_pos][1]:
                time_saved = int(visited_from_end[start_pos][1] - visited_from_end[end_pos][1] - distance)
                if time_saved >= 100:
                    cheat_savings.setdefault(time_saved, set()).add((start_pos, end_pos))

    return sum(len(pairs) for pairs in cheat_savings.values())

racetrack = [list(line.strip()) for line in open('input_day20.txt')]
rows, cols = len(racetrack), len(racetrack[0])

wall_pos = racetrack_pos('#')
track_pos = racetrack_pos('.')
start_pos = next(iter(racetrack_pos('S')))
end_pos = next(iter(racetrack_pos('E')))

track_pos.update([start_pos, end_pos])

visited_from_end = bfs(end_pos)

opti_path = remake_path(start_pos, visited_from_end)[::-1]

print(f"Part 1 - Total of cheats to save at least 100 picoseconds:", calc_cheat(2))
print(f"Part 2 - New total of cheats to save at least 100 picoseconds:", calc_cheat(20))
