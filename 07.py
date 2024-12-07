from time import time
from itertools import product
start = time()

with open('07.in', 'r') as f:
    data = [l.split(": ") for l in f.read().splitlines()]
    valid = set()
    for left, right in data:
        left = int(left)
        right = [int(r) for r in right.split(" ")]

        p = list(product(*(['+*|'] )* (len(right) - 1)))

        for c in p:
            s = ''
            total = right[0]
            idx = 1
            queue = list(c)
            while queue:
                op = queue.pop(0)
                if op == '+':
                    total += right[idx]
                elif op == '*':
                    total *= right[idx]
                elif op == '|':
                    total = int(f'{total}{right[idx]}')
                idx += 1
            if total == left:
                valid.add(left)

print(sum(valid))
print(f"Time: {(time() - start) * 1000:.4f} sec")
