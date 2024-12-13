from z3 import *
import re

with open('13.in') as f:
    lines = [l.split('\n') for l in f.read().split('\n\n')]

def solve(is_part2 = False):
    total = 0
    for a, b, prize in lines:
        a_nums = [int(x) for x in re.search(r'Button A: X\+([0-9]+), Y\+([0-9]+)', a).groups()]
        b_nums = [int(x) for x in re.search(r'Button B: X\+([0-9]+), Y\+([0-9]+)', b).groups()]
        prize_nums = [int(x) for x in re.search(r'Prize: X=([0-9]+), Y=([0-9]+)', prize).groups()]
        if is_part2:
            prize_nums = list(map(lambda x: x + 10000000000000, prize_nums))

        push_a, push_b = Ints('a b')
        s = Solver()
        s.add(push_a > 0)
        s.add(push_b > 0)
        if not is_part2:
            s.add(push_a <= 100)
            s.add(push_b <= 100)
        s.add(push_a*a_nums[0]+push_b*b_nums[0]==prize_nums[0])
        s.add(push_a*a_nums[1]+push_b*b_nums[1]==prize_nums[1])

        if s.check() == sat:
            m = s.model()
            total += m[push_a].as_long() * 3 + m[push_b].as_long()
    return total

print(solve())
print(solve(True))