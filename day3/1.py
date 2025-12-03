example = """987654321111111
811111111111119
234234234234278
818181911112111"""


with open("input.txt", 'r') as f:
    input = f.read().strip()
    # input = example
    maxes = []

    for bank in input.split('\n'):
        l = max(bank[:-1])
        i = bank.index(l)
        r = max(bank[i + 1:])
        maxes.append(int(l + r))

# print(maxes)
print(sum(maxes))
