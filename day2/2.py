example = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""

invalids = set()

def check_dup(s):
    for i in range(1, len(s)//2 + 1):
        if all([s[j:j + i] == s[:i] for j in range(0, len(s), i)]):
            return True

with open("input.txt", 'r') as f:
    input = f.read()
    # input = example
    for entry in input.split(','):
        start, end = entry.split('-')
        for i in range(int(start), int(end) + 1):
            s = str(i)
            if check_dup(s):
                invalids.add(i)

# print(sorted(list(invalids)))
print(sum(invalids))
