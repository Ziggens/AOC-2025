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
    # ranges, ids = example.split('\n\n')
    ranges, ids = input.split('\n\n')
    ranges = [line for line in ranges.split('\n')]
    range_list = []
    for range in ranges:
        a, b = range.split('-')
        range_list.append((int(a), int(b)))

    res = []
    ids = [int(id) for id in ids.split('\n')]
    for id in ids:
        for range in range_list:
            if id >= range[0] and id <= range[1]:
                res.append(id)
                break

    print(len(res))



