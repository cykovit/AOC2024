with open('input_day16.txt') as f:
    data = [line.strip() for line in f]

def find_routes(data):
    grid = []
    start = None
    end = None

    ## parse grid to locate the start (S) & end (E) points
    for y, row in enumerate(data):
        grid_row = []
        for x, cell in enumerate(row):
            grid_row.append(cell)
            if cell == "S":
                start = (y, x)
            elif cell == "E":
                end = (y, x)
        grid.append(grid_row)

    dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]  ## right, up, left, down
    routes = []
    visited = {}

    queue = [(start, [start], 0, 0)]  ## position, history, score, direction
    while queue:
        (y, x), history, curr_score, curr_dir = queue.pop(0)

        if (y, x) == end:
            routes.append((history, curr_score))
            continue

        ## skip already visited tiles with better or equal score
        if ((y, x), curr_dir) in visited and visited[((y, x), curr_dir)] < curr_score:
            continue

        visited[((y, x), curr_dir)] = curr_score

        for _dir, (dy, dx) in enumerate(dirs):
            ## prevent 180 degree turns
            if (curr_dir + 2) % 4 == _dir:
                continue

            ny, nx = y + dy, x + dx
            if grid[ny][nx] != "#" and (ny, nx) not in history:
                if _dir == curr_dir:
                    queue.append(((ny, nx), history + [(ny, nx)], curr_score + 1, _dir))
                else: 
                    queue.append(((y, x), history, curr_score + 1000, _dir))

    return routes

routes = find_routes(data)
min_score = min(r[1] for r in routes)
print(min_score)
