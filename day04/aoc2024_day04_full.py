def find_xmas(grid):
    xmas_count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            for row, col in [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]:
                if all(0 <= r + i * row < len(grid) and 0 <= c + i * col < len(grid[0]) and 
                       grid[r + i * row][c + i * col] == "XMAS"[i] for i in range(4)):
                    xmas_count += 1
    return xmas_count

def find_mas(grid):
    mas_count = 0
    for r in range(1, len(grid) - 1): 
        for c in range(1, len(grid[0]) - 1): 
            try:
                mas1 = ''.join([grid[r - 1][c - 1], grid[r][c], grid[r + 1][c + 1]]) 
                mas2 = ''.join([grid[r + 1][c - 1], grid[r][c], grid[r - 1][c + 1]])  
                if mas1 in ["MAS", "SAM"] and mas2 in ["MAS", "SAM"]:
                    mas_count += 1
            except IndexError:
                continue
    return mas_count

with open(r'input_day04.txt') as file:
    grid = [list(line.strip()) for line in file]

print(f"Part 1 - XMAS count:", find_xmas(grid)) 
print(f"Part 2 - X-MAS count:", find_mas(grid))
