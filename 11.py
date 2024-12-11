from collections import defaultdict

with open('11.in', 'r') as f:
    nums = defaultdict(int)
    for n in f.read().strip().split(' '):
        nums[int(n)] += 1

def blink(d):
    dd = defaultdict(int)
    for i, count in d.items():
        if i == 0:
            dd[1] += count
        elif len(str(i)) % 2 == 0:
            half = len(str(i)) // 2
            left, right = ''.join(list(str(i))[:half]), ''.join(list(str(i))[half:])
            dd[int(left)] += count
            dd[int(right)] += count
        else:
            dd[int(i) * 2024] += count
            
    return dd

def solve(is_part2 = False):
    tmp = nums.copy()
    for d in range(25 if not is_part2 else 75):
        tmp = blink(tmp)
    return sum(tmp.values())

print(solve())
print(solve(True))