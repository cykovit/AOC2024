def is_safe_report(levels):
    increasing = all(
        0 < levels[i+1] - levels[i] <= 3 
        for i in range(len(levels) - 1)
    )
    
    decreasing = all(
        0 < levels[i] - levels[i+1] <= 3 
        for i in range(len(levels) - 1)
    )
    
    return increasing or decreasing

def count_safe_reports_dampener(filename):
    safe_report_count = 0
    
    with open(filename, 'r') as file:
        for line in file:
            levels = [int(x) for x in line.strip().split()]
            
            if is_safe_with_dampener(levels):
                safe_report_count += 1
    
    return safe_report_count

def is_safe_with_dampener(levels):
    if is_safe_report(levels):
        return True
    
    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i+1:]
        
        if is_safe_report(modified_levels):
            return True
    
    return False

result = count_safe_reports_dampener(r'input_day02.txt')
print(f"Safe reports with problem dampener: {result}")
