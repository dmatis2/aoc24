data = []
with open('02.in', 'r') as f:
    data = f.read().strip().split('\n')

def is_safe(nums):
    a_nums = sorted(nums)
    d_nums = sorted(nums, reverse=True)

    if nums == a_nums:
            for i in range(len(nums) - 1):
                diff = nums[i+1] - nums[i]
                if diff < 1 or diff > 3:
                    return False
            return True
    elif nums == d_nums:
        for i in range(len(nums) - 1):
            diff = nums[i] - nums[i+1]
            if diff < 1 or diff > 3:
                return False
        return True
    return False

def solve(data, is_part2 = False):
    safe_reports = 0
    for line in data:
        nums = list(map(int, line.strip().split(' ')))
        if is_safe(nums):
            safe_reports += 1
        elif is_part2:
            for i in range(len(nums)):
                nnums = nums[:i] + nums[i+1:]
                if is_safe(nnums):
                    safe_reports += 1
                    break

    return safe_reports

print(solve(data))
print(solve(data, True))