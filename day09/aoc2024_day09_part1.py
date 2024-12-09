with open('input_day09.txt', 'r') as f:
    data = f.read()

disk_map = [int(value) for value in data[:-1]]
disk = []
id = 0
for i, value in enumerate(disk_map):
    if i % 2 == 0:
        disk.extend([id] * value)
        id += 1
    else:
        disk.extend([-1] * value)

compact_disk = disk.copy()
i = 0
while i < len(compact_disk):
    if compact_disk[i] == -1:
        j = len(compact_disk) - 1
        while j > i:
            if compact_disk[j] >= 0:
                compact_disk[i] = compact_disk[j]
                compact_disk.pop()
                break
            compact_disk.pop()
            j -= 1
    i += 1

solve = sum(i * value for i, value in enumerate(compact_disk))
print(solve)
