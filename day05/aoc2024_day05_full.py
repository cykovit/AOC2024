def valid_order(update, rules):
    ordering_rules = [
        (int(a), int(b)) for rule in rules 
        for a, b in [rule.split('|')] 
        if int(a) in update and int(b) in update
    ]
    
    sorted_update = sorted(update, key=lambda page: 
        sum(1 for x, y in ordering_rules if y == page and x in update)
    )
    
    if sorted_update == update:
        return update
    
    return sorted_update

def solve_part1(filename):
    with open(filename, 'r') as file:
        rules, updates = file.read().strip().split('\n\n')
        rules = rules.split('\n')
        updates = [list(map(int, update.split(','))) for update in updates.split('\n')]
    
    return sum(
        update[len(update)//2] 
        for update in updates 
        if valid_order(update, rules) == update
    )

def solve_part2(filename):
    with open(filename, 'r') as file:
        rules, updates = file.read().strip().split('\n\n')
        rules = rules.split('\n')
        updates = [list(map(int, update.split(','))) for update in updates.split('\n')]
    
    return sum(
        corrected[len(corrected)//2] 
        for update in updates 
        if (corrected := valid_order(update, rules)) != update
    )

print(f"Part 1 - Sum of middle pages for valid updates:", solve_part1('input_day05.txt')) 
print(f"Part 2 - Sum of middle pages for corrected updates:", solve_part2('input_day05.txt'))
