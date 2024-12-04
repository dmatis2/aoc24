import re

data = ''
with open('03.in') as f:
    data = f.read()

def solve(is_part2 = False):
    steps = []

    for mul in re.finditer(r'mul\((\d{1,3}),(\d{1,3})\)', data):
        steps.append((mul.group(), mul.start(0)))

    for do in re.finditer(r'do\(\)', data):
        steps.append((do.group(), do.start(0)))

    for dont in re.finditer(r'don\'t\(\)', data):
        steps.append((dont.group(), dont.start(0)))

    steps.sort(key=lambda x: x[1])

    enabled = True
    total = 0

    for step in steps:
        if step[0].startswith('mul') and enabled:
            nums = re.match(r'mul\((\d{1,3}),(\d{1,3})\)', step[0]).groups()
            total += int(nums[0]) * int(nums[1])
        elif step[0].startswith('do(') and not enabled and is_part2:
            enabled = True
        elif step[0].startswith('don\'t') and enabled and is_part2:
            enabled = False

    return total

print(solve())
print(solve(True))