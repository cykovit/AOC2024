from collections import defaultdict

puzzle_data = {}
with open('input_day21.txt', 'r') as file:
    for line in file:
        cleaned = line.strip()
        puzzle_data[int(cleaned[:3])] = cleaned

path_cache = {}
opti_cache = {}

keypad_layout = {
    'A': (0, 2),
    '^': (0, 1),
    'v': (1, 1),
    '<': (1, 0),
    '>': (1, 2),
}

numpad_layout = {}
for idx in range(9):
    row, col = 2 - (idx // 3), idx % 3
    numpad_layout[str(idx + 1)] = (row, col)
numpad_layout.update({
    '0': (3, 1),
    'A': (3, 2)
})

forbidden_moves = {
    '0': '<',
    '1': 'v',
    '4': 'vv',
    '7': 'vvv',
    '^': '<',
    '<': '^',
    'A': '<<'
}

def gen_path_options(pos, target_pos, current_pos):
    vertical_diff = target_pos[0] - current_pos[0]
    horizontal_diff = target_pos[1] - current_pos[1]
    
    vertical_move = '^' if vertical_diff < 0 else 'v'
    horizontal_move = '<' if horizontal_diff < 0 else '>'
    
    possible_combinations = []
    move_sequences = [
        (vertical_move * abs(vertical_diff) + horizontal_move * abs(horizontal_diff)),
        (horizontal_move * abs(horizontal_diff) + vertical_move * abs(vertical_diff))
    ]
    
    for sequence in move_sequences:
        if pos not in forbidden_moves or not sequence.startswith(forbidden_moves[pos]):
            possible_combinations.append(sequence)
    
    return list(set(possible_combinations))

navigation_maps = {
    'k': defaultdict(dict),
    'n': defaultdict(dict)
}

for layout_type, layout in [('k', keypad_layout), ('n', numpad_layout)]:
    for pos in layout:
        for target in layout:
            navigation_maps[layout_type][pos][target] = gen_path_options(
                pos, layout[target], layout[pos]
            )

def calc_path(sequence, layout_type):
    cache_key = (sequence, layout_type)
    if cache_key in path_cache:
        return path_cache[cache_key]
    
    current = 'A'
    paths = ['']
    
    for next_pos in sequence:
        temp_path = []
        for existing_path in paths:
            for new_segment in navigation_maps[layout_type][current][next_pos]:
                temp_path.append(existing_path + new_segment + 'A')
        paths = temp_path
        current = next_pos
    
    path_cache[cache_key] = paths
    return paths

def opti_path(sequence, depth, layout_type):
    cache_key = (sequence, depth, layout_type)
    if cache_key in opti_cache:
        return opti_cache[cache_key]
    
    expanded = calc_path(sequence, layout_type)
    
    if depth < 1:
        result = min(len(path) for path in expanded)
    else:
        minimum_length = []
        for path in expanded:
            segments = path.split('A')
            total_length = sum(
                opti_path(segment + 'A', depth - 1, 'k')
                for segment in segments
            )
            minimum_length.append(total_length)
        result = min(minimum_length) - 1
    
    opti_cache[cache_key] = result
    return result

print(f"Part 1 - Sum of the complexities:", sum(key * opti_path(value, 2, 'n') for key, value in puzzle_data.items()))
print(f"Part 2 - New sum of the complexities:", sum(key * opti_path(value, 25, 'n') for key, value in puzzle_data.items()))
