dial = 50
password = 0

def parse(line):
    return (line[0:1], int(line[1:]))

with open("input.txt", 'r') as f:
    input = f.read().strip().split('\n')
    for line in input:
        direction, amount = parse(line)
        if direction == "L":
            dial = (dial - amount) % 100
        else:
            dial = (dial + amount) % 100

        if dial == 0:
            password += 1

print(password)
