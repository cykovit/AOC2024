from pathlib import Path
from typing import List

MODULO = 16777216
ITERATIONS = 2000

filename = 'input_day22.txt'
data = [int(line.strip()) for line in Path(filename).read_text().splitlines()]

def _transform_number(number: int) -> int:
    number = ((number * 64) ^ number) % MODULO
    number = ((number // 32) ^ number) % MODULO
    number = ((number * 2048) ^ number) % MODULO
    return number

results = []
for secret in data:
    for _ in range(ITERATIONS):
        secret = _transform_number(secret)
    results.append(secret)

result = sum(results)
print(result)
