import re

def corrupted_memory(filename):
    with open(filename, 'r') as file:
        content = file.read()
    
    mul_enabled = True
    total_part1 = 0
    total_part2 = 0
    
    for match in re.findall(r'(mul\(\d+,\d+\)|do\(\)|don\'?t\(\))', content):
        if match == 'do()':
            mul_enabled = True
        elif match == 'dont()' or match == "don't()":
            mul_enabled = False
        elif match.startswith('mul'):
            x, y = map(int, re.findall(r'\d+', match))
            
            ## part 1: always add multiplication
            total_part1 += x * y
            
            ## part 2: add only if enabled
            if mul_enabled:
                total_part2 += x * y
    
    return total_part1, total_part2

part1_result, part2_result = corrupted_memory(r'input_day03.txt')
print(f"Part 1 - Sum of multiplication results: {part1_result}")
print(f"Part 2 - Sum of enabled multiplication results: {part2_result}")
