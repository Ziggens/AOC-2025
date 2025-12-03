example = """987654321111111
811111111111119
234234234234278
818181911112111"""

maxes = []

with open("input.txt", 'r') as f:
    input = f.read().strip()
    # input = example

    for bank in input.split('\n'):
        temp = []
        l = 0
        for i in range(12):
            cur_max = max(bank[l:len(bank) - 11 + i])
            l = bank[l:].index(cur_max) + l + 1
            temp.append(cur_max)
        maxes.append(int(''.join(temp)))

# print(maxes)
print(sum(maxes))
