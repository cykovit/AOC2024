from collections import Counter

def process(og_stones):
    stones = og_stones.copy()
    
    for _ in range(1, 76):
        new_stones = Counter()
        
        for number, count in stones.items():
            if number == 0:
                new_stones[1] += count
                continue
            
            num_str = str(number)
            num_length = len(num_str)
            
            mid = num_length // 2
            
            if num_length % 2 == 1: 
                new_stones[2024 * number] += count
            else:  
                left_part = int(num_str[:mid])
                right_part = int(num_str[mid:])
                
                new_stones[left_part] += count
                new_stones[right_part] += count
        
        stones = new_stones
        
        if _ == 25:
            print("Part 1 - Total of stones after blinking 25 times:", sum(new_stones.values()))
        if _ == 75:
            print("Part 2 - Total of stones after blinking 75 times:", sum(new_stones.values()))
    
    return stones

with open('input_day11.txt') as f:
    og_stones = Counter(map(int, f.read().split()))

final_stones = process(og_stones)
