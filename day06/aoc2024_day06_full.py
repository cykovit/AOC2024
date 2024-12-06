def solve_part1(lab_map):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir_map = {'^': 0, '>': 1, 'v': 2, '<': 3}
    
    def start_position(maze):
        for y, row in enumerate(maze):
            for x, cell in enumerate(row):
                if cell in dir_map:
                    return (y, x), dir_map[cell]
        return None, None
    
    guard_pos, direction_idx = start_position(lab_map)
    
    if guard_pos is None:
        return 0
    
    ## clear start cell
    visited = {guard_pos}
    lab_map[guard_pos[0]][guard_pos[1]] = '.'
    rows, cols = len(lab_map), len(lab_map[0])
    
    while True:
        ## find next position
        dy, dx = directions[direction_idx]
        next_pos = (guard_pos[0] + dy, guard_pos[1] + dx)
        if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols):
            break
        
        ## check if next position is obstacle
        if lab_map[next_pos[0]][next_pos[1]] == '#':
            direction_idx = (direction_idx + 1) % 4
        else:
            guard_pos = next_pos
            visited.add(guard_pos)
    
    return len(visited)

def solve_part2(lab_map, initial_pos, initial_dir, obstacle_pos):
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
        solve_part2(lab_map, guard_pos, direction_idx, (y, x))
        for y in range(len(lab_map))
        for x in range(len(lab_map[0]))
        if lab_map[y][x] == '.'
    )

file_path = 'input_day06.txt'

with open(file_path, 'r') as f:
    lab_map_part1 = [list(line.strip()) for line in f.readlines()]
result_part1 = solve_part1(lab_map_part1)
print(f"Part 1 - Distinct positions visited: {result_part1}")


with open(file_path, 'r') as f:
    lab_map_part2 = [list(line.strip()) for line in f.readlines()]
result_part2 = find_obstacle_pos(lab_map_part2)
print(f"Part 2 - Different obstruction positions: {result_part2}")
