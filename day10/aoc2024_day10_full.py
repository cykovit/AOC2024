from collections import deque

with open('input_day10.txt') as f:
    lines = f.read().strip().split("\n")

top_map = {(row, col): int(height) for row, line in enumerate(lines) for col, height in enumerate(line)}

def find_trailheads(top_map):
    return [
        position for position, height in top_map.items() 
        if height == 0
    ]

def explore_trails(top_map, start, all_trails=False):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    stack = deque([(start, [start])])
    
    result = []
    unique_nines = set()
    
    while stack:
        current_position, trail = stack.pop()
        
        if top_map[current_position] == 9:
            if all_trails:
                result.append(trail)
            else:
                unique_nines.add(current_position)
            continue
        
        for dr, dc in directions:
            neighbor = (current_position[0] + dr, current_position[1] + dc)
            
            if (
                neighbor in top_map and 
                neighbor not in trail and 
                top_map[neighbor] == top_map[current_position] + 1
            ):
                stack.append((neighbor, trail + [neighbor]))
    
    return result if all_trails else list(unique_nines)

def solve(top_map):

    trailheads = find_trailheads(top_map)
    
    ## part 1
    trailhead_scores = [
        len(explore_trails(top_map, trailhead, all_trails=False)) 
        for trailhead in trailheads
    ]
    
    ## part 2
    trailhead_ratings = [
        len(explore_trails(top_map, trailhead, all_trails=True)) 
        for trailhead in trailheads
    ]
    
    return trailhead_scores, trailhead_ratings

trailhead_scores, trailhead_ratings = solve(top_map)
print("Part 1 - Sum of trailhead scores:", sum(trailhead_scores))
print("Part 2 - Sum of trailhead ratings:", sum(trailhead_ratings))
