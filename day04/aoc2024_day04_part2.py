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

print(find_mas(grid))
