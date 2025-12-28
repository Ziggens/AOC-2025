from functools import reduce

example = """123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +  """

with open("input.txt") as f:
    # input = example.split('\n')
    input = f.read().strip().split('\n')
    nums, ops = input[:-1], input[-1].split()
    nums = [map(lambda x: int(x), line.split()) for line in nums]

    n2 = [[] for _ in ops]

    for line in nums:
        for i, num in enumerate(line):
            n2[i].append(num)

    res = [0] * len(ops)

    for i, op in enumerate(ops):
        if op == '+':
            res[i] = sum(n2[i])
        elif op == '*':
            res[i] = reduce(lambda a, b: a * b, n2[i])

    # print(res)
    print(sum(res))


