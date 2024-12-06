def obstacle(lab_map, initial_pos, initial_dir, obstacle_pos):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] 
    rows, cols = len(lab_map), len(lab_map[0])
    direction_idx = initial_dir
    guard_pos = initial_pos
    visited = set()
   
    while True:
        state = (guard_pos, direction_idx)
        if state in visited:
            return True 
       
        visited.add(state)
       
        ## next position
        dy, dx = directions[direction_idx]
        next_pos = (guard_pos[0] + dy, guard_pos[1] + dx)
       
        ## check for boundary/obstacle
        if 0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols:
            if lab_map[next_pos[0]][next_pos[1]] == '#' or next_pos == obstacle_pos:
                direction_idx = (direction_idx + 1) % 4
            else:
                guard_pos = next_pos
        else:
            return False

def find_obstacle_pos(lab_map):
    direction_map = {'^': 0, '>': 1, 'v': 2, '<': 3}
   
    ## start position
    for y, row in enumerate(lab_map):
        for x, cell in enumerate(row):
            if cell in direction_map:
                guard_pos = (y, x)
                direction_idx = direction_map[cell]
                lab_map[y][x] = '.'
                break

    return sum(
        obstacle(lab_map, guard_pos, direction_idx, (y, x))
        for y in range(len(lab_map))
        for x in range(len(lab_map[0]))
        if lab_map[y][x] == '.'
    )

file_path = 'input_day06.txt'
with open(file_path, 'r') as f:
    lab_map = [list(line.strip()) for line in f]

print(f"Different obstruction positions: {find_obstacle_pos(lab_map)}")
