with open('input_day15.txt') as file:
    w_map, robot_move = file.read().split('\n\n')

## part 1
robot_move = robot_move.replace('\n', '')
w_grid = [[cell for cell in row] for row in w_map.splitlines()]
rows, cols = len(w_grid), len(w_grid[0])
w_state = {
    "boxes": set(r + 1j * c for r in range(rows) for c in range(cols) if w_grid[r][c] == "O"),
    "walls": set(r + 1j * c for r in range(rows) for c in range(cols) if w_grid[r][c] == "#"),
    "open_spaces": set(r + 1j * c for r in range(rows) for c in range(cols) if w_grid[r][c] == "."),
}
robot_pos = [r + 1j * c for r in range(rows) for c in range(cols) if w_grid[r][c] == "@"][0]
movement_dir = {">": 1j, "<": -1j, "v": 1, "^": -1}

for move in robot_move:
    push_box = set()
    target_pos = robot_pos + movement_dir[move]
    while target_pos in w_state["boxes"]:
        push_box.add(target_pos)
        target_pos += movement_dir[move]
    if target_pos in w_state["open_spaces"]:
        update_box = set(box + movement_dir[move] for box in push_box)
        w_state["boxes"].difference_update(push_box)
        w_state["boxes"].update(update_box)
        w_state["open_spaces"].update(push_box)
        w_state["open_spaces"].difference_update(update_box)
        w_state["open_spaces"].add(robot_pos)
        robot_pos += movement_dir[move]
        w_state["open_spaces"].remove(robot_pos)

solve_part1 = int(sum(100 * spot.real + spot.imag for spot in w_state["boxes"]))

## part 2
vec = {">": 1j, "<": -1j, "v": 1, "^": -1}
rows, cols = 0, 0
free, rocks, walls, lr, rr = set(), set(), set(), set(), set()
cp = 0

map_grid = [list(l) for l in w_map.splitlines()]
rows, cols = len(map_grid), len(map_grid[0])
rock_set = {r + 1j * c for r in range(rows) for c in range(cols) if map_grid[r][c] == "O"}
wall_set = {r + 1j * c for r in range(rows) for c in range(cols) if map_grid[r][c] == "#"}
free_set = {r + 1j * c for r in range(rows) for c in range(cols) if map_grid[r][c] == "."}

free = {2j * f.imag + f.real for f in free_set}
rocks = {2j * f.imag + f.real for f in rock_set}
walls = {2j * f.imag + f.real for f in wall_set}

new_free = {f + 1j for f in free}
new_rocks = {f + 1j for f in rocks}
new_walls = {f + 1j for f in walls}
free |= new_free
walls |= new_walls

cp = [r + 1j * c for r in range(rows) for c in range(cols) if map_grid[r][c] == "@"][0]
cp = 2j * cp.imag + cp.real
lr, rr = rocks, new_rocks
cols = 2
free.add(cp + 1j)

def find(look, ins, frr, flr):
    if look not in rr and look not in lr:
        return look in free

    if look in rr:
        frr.add(look)
        flr.add(look - 1j)
        return all([find(la, ins, frr, flr) for la in [look + vec[ins], look + vec[ins] - 1j]]) if ins in "v^" else find(look + 2 * vec[ins], ins, frr, flr)

    elif look in lr:
        flr.add(look)
        frr.add(look + 1j)
        return all([find(la, ins, frr, flr) for la in [look + vec[ins], look + vec[ins] + 1j]]) if ins in "v^" else find(look + 2 * vec[ins], ins, frr, flr)

def solve(cp, instructions):
    global free, lr, rr

    for ins in instructions:
        flr, frr = set(), set()
        if find(cp + vec[ins], ins, frr, flr):
            lr -= flr
            lr |= (mlr := set(c + vec[ins] for c in flr))
            rr -= frr
            rr |= (mrr := set(c + vec[ins] for c in frr))
            free |= flr | frr
            free -= mlr | mrr
            free.add(cp)
            cp += vec[ins]
            free.remove(cp)

    return int(sum(100 * c.real + c.imag for c in lr))

instructions = robot_move.replace('\n', '')
solve_part2 = solve(cp, instructions)

echo = f"Part 1 - Sum of GPS coordinates: {solve_part1}\nPart 2 - Sum of final GPS coordinates: {solve_part2}"
print(echo)
