with open('19.in') as f:
    towels, combinations = f.read().split('\n\n')
    towels = towels.split(', ')

seen = {}
def is_possible(towels, comb):
    if comb in seen:
        return seen[comb]
    num = 0
    if comb == '':
        num = 1
    for towel in towels:
        if comb.startswith(towel) and is_possible(towels, comb[len(towel):]):
            num += is_possible(towels, comb[len(towel):])
    seen[comb] = num
    return num

part1, part2 = 0, 0
for comb in combinations.split('\n'):
    pos = is_possible(towels, comb)
    part1 += 1 if pos > 0 else 0
    part2 += is_possible(towels, comb)

print(part1)
print(part2)