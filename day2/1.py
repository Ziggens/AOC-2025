example = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""

invalids = set()

with open("input.txt", 'r') as f:
    input = f.read()
    input = example
    for entry in input.split(','):
        start, end = entry.split('-')
        # print(entry)
        for i in range(int(start), int(end) + 1):
            s = str(i)
            if len(s) % 2 == 1:
                continue
            if s[:len(s) // 2] == s[len(s) // 2:]:
                invalids.add(i)


print(invalids)
print(sum(invalids))
