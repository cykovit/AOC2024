def cat(a, b):
    return int(str(a) + str(b))

def eval(num, ops):
    result = num[0]
    for i, op in enumerate(ops):
        if op == '+':
            result += num[i+1]
        elif op == '*':
            result *= num[i+1]
        else: 
            result = cat(result, num[i+1])
    return result

def solve(filename):
    total_result = 0
    
    with open(filename, 'r') as f:
        for line in f:
            target, nums_str = line.strip().split(': ')
            target = int(target)
            num = list(map(int, nums_str.split()))
            
            ops_positions = len(num) - 1
            
            equation_solved = False
            
            for i in range(3**ops_positions): 
                ops = []
                temp_i = i
                for _ in range(ops_positions):
                    remainder = temp_i % 3
                    if remainder == 0:
                        ops.append('+')
                    elif remainder == 1:
                        ops.append('*')
                    else:
                        ops.append('||')
                    temp_i //= 3
                
                try:
                    if eval(num, ops) == target:
                        equation_solved = True
                        break
                except Exception:
                    continue
            
            if equation_solved:
                total_result += target
    
    return total_result

result = solve('input_day07.txt')
print(f"New calibration result: {result}")
