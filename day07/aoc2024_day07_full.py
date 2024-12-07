def cat(a, b):
    return int(str(a) + str(b))

def eval(num, ops):
    ## eval func for part 1 & 2
    result = num[0]
    for i, op in enumerate(ops):
        if op == '+':
            result += num[i+1]
        elif op == '*':
            result *= num[i+1]
        elif op == '||': 
            result = cat(result, num[i+1])
    return result

def solve_part1(input_file):
    total_calibration_result = 0
   
    with open(input_file, 'r') as f:
        for line in f:
            test_value, nums_str = line.strip().split(': ')
            test_value = int(test_value)
            nums = list(map(int, nums_str.split()))
           
            num_ops = len(nums) - 1
           
            ops_combinations = []
            for i in range(2**num_ops):
                ops = []
                for j in range(num_ops):
                    ops.append('+' if i & (1 << j) else '*')
                ops_combinations.append(ops)
           
            valid_equations_found = False
            for ops in ops_combinations:
                result = eval(nums, ops)
                if result == test_value:
                    valid_equations_found = True
                    break
           
            if valid_equations_found:
                total_calibration_result += test_value
   
    return total_calibration_result

def solve_part2(filename):
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

result_part1 = solve_part1('input_day07.txt')
result_part2 = solve_part2('input_day07.txt')

print(f"Part 1 - Total calibration result: {result_part1}")
print(f"Part 2 - New calibration result: {result_part2}")
