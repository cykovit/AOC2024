from pathlib import Path
from collections import defaultdict
from typing import List, Tuple

MODULO = 16777216
ITERATIONS = 2000
SEQUENCE_LENGTH = 4

filename = 'input_day22.txt'
data = [int(line.strip()) for line in Path(filename).read_text().splitlines()]

def transform_number(number: int) -> int:
    number = ((number * 64) ^ number) % MODULO
    number = ((number // 32) ^ number) % MODULO
    number = ((number * 2048) ^ number) % MODULO
    return number

all_prices = []
for secret in data:
    prices = []
    for _ in range(ITERATIONS):
        secret = transform_number(secret)
        prices.append(secret % 10)
    all_prices.append(prices)

changes = []
for prices in all_prices:
    change = [b - a for a, b in zip(prices, prices[1:])]
    changes.append(change)

pattern_sums = defaultdict(int)
for buyer_idx, change in enumerate(changes):
    seen_patterns = set()
    
    for i in range(len(change) - SEQUENCE_LENGTH + 1):
        pattern = tuple(change[i:i + SEQUENCE_LENGTH])
        if pattern not in seen_patterns:
            pattern_sums[pattern] += all_prices[buyer_idx][i + SEQUENCE_LENGTH]
            seen_patterns.add(pattern)

result = max(pattern_sums.values())
print(result)
