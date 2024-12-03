import re

def corrupted_memory_v2(filename):
    with open(filename, 'r') as file:
        content = file.read()
    
    mul_enabled = True
    total = 0
    
    for match in re.findall(r'(mul\(\d+,\d+\)|do\(\)|don\'?t\(\))', content):
        if match == 'do()':
            mul_enabled = True
        elif match == 'dont()' or match == "don't()":
            mul_enabled = False
        elif mul_enabled and match.startswith('mul'):
            x, y = map(int, re.findall(r'\d+', match))
            total += x * y
    
    return total

result = corrupted_memory_v2(r'input_day03.txt')
print(f"Sum of enabled multiplication results: {result}")
