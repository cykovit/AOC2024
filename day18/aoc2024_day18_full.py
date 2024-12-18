with open('input_day18.txt') as file:
    falling_bytes = [int(line.split(',')[0]) + 1j * int(line.split(',')[1]) for line in file.readlines()]

def remake_path(current, explored):
    path = []
    while current:
        path.append(current)
        current = explored[current]
    return path[::-1]

def bfs(start, exit_point):
    explored, queue = {}, []
    explored[start] = None
    queue.append(start)
    while queue:
        current = queue.pop(0)  
        if current == exit_point:
            return remake_path(current, explored)
        for next in [(current + d) for d in (1, -1, 1j, -1j) if (current + d) in safe_memory]:
            if next not in explored:
                explored[next] = current
                queue.append(next)

memory_size = 71  
start_point = 0 
exit_point = 70 + 70 * 1j  

## part 1
safe_memory = set(r + 1j * c for r in range(memory_size) for c in range(memory_size)) - set(falling_bytes[:1024])
minimum_steps = len(bfs(start_point, exit_point))

## part 2
first_byte = None
for num_bytes in range(len(falling_bytes), 0, -1):
    safe_memory = set(r + 1j * c for r in range(memory_size) for c in range(memory_size)) - set(falling_bytes[:num_bytes])
    if bfs(start_point, exit_point) is not None:
        first_byte = falling_bytes[num_bytes]
        break

print(f"Part 1 - Minimum steps to exit: {minimum_steps}")
if first_byte is not None:
    print(f"Part 2 - First byte coordinates: {first_byte.real:.0f},{first_byte.imag:.0f}")
