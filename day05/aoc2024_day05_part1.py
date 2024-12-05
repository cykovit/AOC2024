def valid_order(update, rules):
    ordering_rules = [
        (int(a), int(b)) for rule in rules 
        for a, b in [rule.split('|')] 
        if int(a) in update and int(b) in update
    ]
    
    for i, page in enumerate(update):
        for j, next_page in enumerate(update[i+1:], start=i+1):
            if (next_page, page) in ordering_rules:
                return False
    return True

def solve(filename):
    with open(filename, 'r') as file:
        rules, updates = file.read().strip().split('\n\n')
        rules = rules.split('\n')
        updates = [list(map(int, update.split(','))) for update in updates.split('\n')]
    
    return sum(update[len(update)//2] for update in updates if valid_order(update, rules))

print(solve('input_day05.txt'))
