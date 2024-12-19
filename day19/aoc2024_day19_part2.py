patterns, designs = open('input_day19.txt').read().split('\n\n')

memo = {}

def fill(d):
    if d in memo:
        return memo[d]
    if d == '':
        result = 1
    elif len(v := [p for p in patterns.split(', ') if d.startswith(p)]) == 0:
        result = 0
    else:
        result = sum([fill(d[len(p):]) for p in v])
    memo[d] = result
    return result

print(sum(fill(d) for d in designs.splitlines()))
