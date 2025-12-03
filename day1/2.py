dial = 50
password = 0

def parse(line):
    return (line[0:1], int(line[1:]))

with open("input.txt", 'r') as f:
    input = f.read().strip().split('\n')
    for line in input:
        old = dial
        direction, amount = parse(line)

        if direction == "L":
            total = (100 - dial) % 100 + amount
            passes = total // 100
            dial = (dial - amount) % 100
        else:
            total = dial + amount
            passes = total // 100
            dial = (dial + amount) % 100

        password += passes

print(password)
