'''
A dial is numbered 0-99
It round robins (if you go past 99, you restart at 0 and vice versa)

Each line in input starts with either L or R, indicating which direction to go on the dial.
L decreases the number
R increases the number

return the count how many times you hit 0 after turning the dial
'''

def part1(data: str) -> int:
    lines = data.strip().split('\n')
    position = 50
    zero_count = 0

    for line in lines:
        direction = line[0]
        clicks = int(line[1:])

        # % 100 will round robin
        if direction == 'L':
            position = (position - clicks) % 100
        else: # direction R
            position = (position + clicks) % 100

        if position == 0:
            zero_count += 1
    return zero_count

def part2(data: str) -> int:
    lines = data.strip().split('\n')
    position = 50
    zero_count = 0

    for line in lines:
        direction = line[0]
        clicks = int(line[1:])

        # Move 1 click instead
        for _ in range(clicks):
            if direction == 'L':
                position = (position - 1) % 100
            else: # direction R
                position = (position + 1) % 100

            if position == 0:
                zero_count += 1
    return zero_count
