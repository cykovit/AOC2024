with open('input_day15.txt') as file:
    w_map, robot_move = file.read().split('\n\n')

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

print(int(sum(100 * spot.real + spot.imag for spot in w_state["boxes"])))
