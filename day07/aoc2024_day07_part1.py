def eval(num, ops):
    if len(num) - 1 != len(ops):
        return None
    
    result = num[0]
    for i, op in enumerate(ops):
        if op == '+':
            result += num[i+1]
        elif op == '*':
            result *= num[i+1]
    
    return result

def solve(input_file):
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
            
            ## find/store valid equations
            valid_equations_found = False
            for ops in ops_combinations:
                result = eval(nums, ops)
                if result == test_value:
                    valid_equations_found = True
                    break
            
            if valid_equations_found:
                total_calibration_result += test_value
    
    return total_calibration_result

result = solve('input_day07.txt')
print(f"Total calibration result: {result}")
