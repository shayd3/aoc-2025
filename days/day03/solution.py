'''
Input: Each line of digits in input corresponds to a single bank of batteries.

We need to turn on exactly k batteries within a bank of batteries.

Return the sum of the maximum joltage from each bank.
'''

def get_max_joltage(s, amount) -> int:
    '''
    Given a string of digits s, find the maximum number that can be formed
    by selecting `amount` digits from s in order.
    '''
    result = ''
    for skip in range(amount - 1, -1, -1):
        idx = max(range(len(s) - skip), key=lambda i: s[i])
        result += s[idx]
        s = s[idx + 1:]
    return int(result)


def solve():
    try:
        with open('input[1].txt', 'r') as f:
            data = f.read()
    except FileNotFoundError:
        print("Error: input[1].txt not found.")
        return

    # Part 1
    p1 = part1(data)
    print(f"Part 1 Total Output Joltage: {p1}")

    # Part 2
    p2 = part2(data)
    print(f"Part 2 Total Output Joltage: {p2}")


def part1(data: str) -> int:
    lines = data.strip().split('\n')
    return sum(get_max_joltage(line, 2) for line in lines)


def part2(data: str) -> int:
    lines = data.strip().split('\n')
    return sum(get_max_joltage(line, 12) for line in lines)


if __name__ == '__main__':
    solve()
