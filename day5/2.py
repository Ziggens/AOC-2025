example = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

ranges = []

with open ("input.txt") as f:
    input = f.read().strip()
    ranges, ids = example.split('\n\n')
    ranges, ids = input.split('\n\n')
    ranges = [line for line in ranges.split('\n')]
    range_list = []
    for rnge in ranges:
        a, b = rnge.split('-')
        range_list.append([int(a), int(b)])


    range_list.sort()
    new_list = [range_list[0]]
    for i in range(1, len(range_list)):
        if new_list[-1][1] >= range_list[i][0]:
            new_list[-1] = [new_list[-1][0], max(new_list[-1][1], range_list[i][1])]
        else:
            new_list.append(range_list[i])

    sum = 0
    for a, b in new_list:
        sum += b - a + 1

    print(sum)

