'''
The ranges are separated by commas (,); each range gives its first ID and last ID separated by a dash (-).

find the invalid IDs by looking for any ID which is made only of some sequence of digits repeated twice. So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs.

None of the numbers have leading zeroes; 0101 isn't an ID at all. (101 is a valid ID that you would ignore.)

Your job is to find all of the invalid IDs that appear in the given ranges.
Add up all of the invalid IDs and return value
'''

def part1(data: str) -> int:
    lines = data.strip().split(',')
    result = 0
    for line in lines:
        firstId, lastId = line.split('-')
        start, end = int(firstId), int(lastId)

        for num in range(start, end + 1):
            s = str(num)
            firstHalf = s[:len(s)//2]
            secondHalf = s[len(s)//2:]
            if firstHalf == secondHalf:
                result += num

    return result

def part2(data: str) -> int:
    lines = data.strip().split('\n')
    # Your solution here
    return 0
