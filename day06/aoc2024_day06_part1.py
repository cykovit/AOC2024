def solve(lab_map):
    ## up, right, down, left
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

file_path = "input_day06.txt"
with open(file_path, 'r') as f:
    lab_map = [list(line.strip()) for line in f.readlines()]

result = solve(lab_map)
print(f"Distinct positions visited: {result}")
