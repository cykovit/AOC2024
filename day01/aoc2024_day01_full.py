def solve_aoc_day01(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    
    left_list = []
    right_list = []
    
    for line in data:
        left, right = map(int, line.strip().split())
        left_list.append(left)
        right_list.append(right)
    
    ## part 1
    sorted_left = sorted(left_list)
    sorted_right = sorted(right_list)
    total_distance = sum(abs(left - right) for left, right in zip(sorted_left, sorted_right))
    
    ## part 2
    right_count = {}
    for num in right_list:
        right_count[num] = right_count.get(num, 0) + 1
    
    similarity = sum(left * right_count.get(left, 0) for left in left_list)
    
    return total_distance, similarity

file_path = r'input_day01.txt'
part1_result, part2_result = solve_aoc_day01(file_path)

print("Part 1 - Total distance:", part1_result)
print("Part 2 - Similarity score:", part2_result)
