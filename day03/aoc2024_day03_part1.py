import re

def corrupted_memory(filename):
    with open(filename, 'r') as file:
        corrupted_memory = file.read().strip()
    
    mul_pattern = r'mul\s*\(\s*(\d+)\s*,\s*(\d+)\s*\)'
    
    matches = re.findall(mul_pattern, corrupted_memory)
    
    total_sum = sum(int(x) * int(y) for x, y in matches)
    
    return total_sum

result = corrupted_memory(r'input_day03.txt')
print(f"Sum of multiplication results: {result}")
