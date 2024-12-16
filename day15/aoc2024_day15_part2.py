vec = {">": 1j, "<": -1j, "v": 1, "^": -1}
rows, cols = 0, 0
free, rocks, walls, lr, rr = set(), set(), set(), set(), set()
cp = 0  

def parse(map_str):
    global rows, cols, free, rocks, walls, cp
    
    map_grid = [list(l) for l in map_str.splitlines()]
    rows, cols = len(map_grid), len(map_grid[0])
    
    rock_set = {r + 1j * c for r in range(rows) for c in range(cols) if map_grid[r][c] == "O"}
    wall_set = {r + 1j * c for r in range(rows) for c in range(cols) if map_grid[r][c] == "#"}
    free_set = {r + 1j * c for r in range(rows) for c in range(cols) if map_grid[r][c] == "."}
    
    free = {2j * f.imag + f.real for f in free_set}
    rocks = {2j * f.imag + f.real for f in rock_set}
    walls = {2j * f.imag + f.real for f in wall_set}
    
    new_free = {f + 1j for f in free}
    new_rocks = {f + 1j for f in rocks}
    new_walls = {f + 1j for f in walls}
    
    free |= new_free
    walls |= new_walls
    
    ## find starting point
    cp = [r + 1j * c for r in range(rows) for c in range(cols) if map_grid[r][c] == "@"][0]
    cp = 2j * cp.imag + cp.real
    
    global lr, rr
    lr, rr = rocks, new_rocks
    cols *= 2
    
    free.add(cp + 1j)
    
    return cp

def find(look, ins, frr, flr):
    if look not in rr and look not in lr:
        return look in free
    
    if look in rr:
        frr.add(look)
        flr.add(look - 1j)
        return all([find(la, ins, frr, flr) for la in [look + vec[ins], look + vec[ins] - 1j]]) if ins in "v^" else find(look + 2 * vec[ins], ins, frr, flr)
    
    elif look in lr:
        flr.add(look)
        frr.add(look + 1j)
        return all([find(la, ins, frr, flr) for la in [look + vec[ins], look + vec[ins] + 1j]]) if ins in "v^" else find(look + 2 * vec[ins], ins, frr, flr)

def solve(cp, instructions):
    global free, lr, rr
    
    for ins in instructions:
        flr, frr = set(), set()
        if find(cp + vec[ins], ins, frr, flr):
            lr -= flr
            lr |= (mlr := set(c + vec[ins] for c in flr))
            rr -= frr
            rr |= (mrr := set(c + vec[ins] for c in frr))
            free |= flr | frr
            free -= mlr | mrr
            free.add(cp)
            cp += vec[ins]
            free.remove(cp)
    
    return int(sum(100 * c.real + c.imag for c in lr))

with open('input_day15.txt', 'r') as f:
    map_str, instructions = f.read().strip().split('\n\n')

cp = parse(map_str)

instructions = instructions.replace('\n', '')

result = solve(cp, instructions)
print(result)
