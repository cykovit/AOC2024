def find_xmas(grid):
    xmas_count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            for row, col in [(0,1),(1,0),(1,1),(1,-1),(0,-1),(-1,0),(-1,-1),(-1,1)]:
                if all(0 <= r+i*row < len(grid) and 0 <= c+i*col < len(grid[0]) and 
                       grid[r+i*row][c+i*col] == "XMAS"[i] for i in range(4)):
                    xmas_count += 1
    return xmas_count

with open(r'input_day04.txt') as file:
    grid = [list(line.strip()) for line in file]

print(find_xmas(grid))
