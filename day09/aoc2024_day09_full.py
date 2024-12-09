with open('input_day09.txt', 'r') as f:
    data = f.read()

## part 1
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
for i in range(len(compact_disk)):
    if i >= len(compact_disk):
        break
    if compact_disk[i] == -1:
        for j in range(len(compact_disk) - 1, -1, -1):
            if i >= len(compact_disk):
                break
            if compact_disk[j] >= 0:
                compact_disk[i] = compact_disk[j]
                compact_disk.pop()
                break
            compact_disk.pop()
part1_result = sum(i * value for i, value in enumerate(compact_disk))

## part 2
struct_disk = []
id = 0
for i, value in enumerate(disk_map):
    if i % 2 == 0:
        struct_disk.append([id] * value)
        id += 1
    elif value > 0:
        struct_disk.append([-1] * value)
for i in range(len(struct_disk)):
    if i >= len(struct_disk):
        break
    if struct_disk[i][0] == -1:
        for j in range(len(struct_disk) - 1, i, -1):
            if i >= len(struct_disk) or -1 not in struct_disk[i]:
                break
            if struct_disk[j][0] >= 0 and struct_disk[i].count(-1) >= len(struct_disk[j]):
                start = struct_disk[i].index(-1)
                struct_disk[i][start:start + len(struct_disk[j])] = struct_disk[j]
                struct_disk[j] = [-2] * len(struct_disk[j])
            if j == len(struct_disk) - 1 and struct_disk[j][0] == -1:
                struct_disk.pop()
compact_disk = [value for sublist in struct_disk for value in sublist]
part2_result = sum(i * max(value, 0) for i, value in enumerate(compact_disk))

print("Part 1 - Filesystem checksum:", part1_result)
print("Part 2 - New filesystem checksum:", part2_result)
