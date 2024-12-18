with open('input_day18.txt') as file:
    falling_bytes = [int(line.split(',')[0]) + 1j * int(line.split(',')[1]) for line in file.readlines()]

def remake_path(current, explored):
    ## reconstruct path from exit to start
    path = []
    while current:
        path.append(current)
        current = explored[current]
    return path[::-1]

def bfs(start, exit_point):
    ## performs Breadth First Search to find shortest path from start to exit_point
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

## define memory space
memory_size = 71  ## grid dimensions = 0 to 70
start_point = 0  ## top-left corner (0, 0)
exit_point = 70 + 70 * 1j  ## bottom-right corner (70, 70)

safe_memory = set(r + 1j * c for r in range(memory_size) for c in range(memory_size)) - set(falling_bytes[:1024])
minimum_steps = len(bfs(start_point, exit_point))

print(minimum_steps)
