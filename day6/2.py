from functools import reduce

example = """123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +  """


def parse_ceph_numbers(nums):
    for col in range(len(nums[0])):
        for row in range(len(nums)):
            if nums[row][col] != ' ':
                ceph_nums[col] += nums[row][col]

    parsed_nums = []
    temp = []
    for item in ceph_nums:
        if item == '':
            parsed_nums.append(temp)
            temp = []
        else:
            temp.append(item)

    parsed_nums.append(temp)
    return parsed_nums

with open("input.txt") as f:
    # input = example.split('\n')
    input = f.read().strip().split('\n')
    nums, ops = input[:-1], input[-1].split()
    longest = max([len(line) for line in nums])
    nums = [line.ljust(longest, ' ') for line in nums]

    ceph_nums = [''] * len(nums[0])
    splits = [i for i, c in enumerate(input[-1]) if c in ['*', '+']]

    parsed_nums = parse_ceph_numbers(nums)
    total = 0

    for i, op in enumerate(ops):
        sum = 0
        prod = 1
        for num in parsed_nums[i]:
            if op == '+':
                sum += int(num)
            elif op == '*':
                prod *= int(num)

        if sum == 0:
            total += prod
        else:
            total += sum

    print(total)
