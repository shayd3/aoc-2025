'''
The ranges are separated by commas (,); each range gives its first ID and last ID separated by a dash (-).

find the invalid IDs by looking for any ID which is made only of some sequence of digits repeated twice. So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs.

None of the numbers have leading zeroes; 0101 isn't an ID at all. (101 is a valid ID that you would ignore.)

Your job is to find all of the invalid IDs that appear in the given ranges.
Add up all of the invalid IDs and return value
'''

from collections import Counter

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

def is_list_same(l: list) -> bool:
    return len(set(l)) <= 1  # 1 if all same, 0 if empty list

def has_repeating_pattern(s: str) -> bool:
    n = len(s)

    # Bruteforce babyyyy - try all possible chunk sizes from 1 to n//2
    for chunk_size in range(1, n//2+1):
        if n % chunk_size == 0: # only works if divides evenly
            chunks = [s[i:i+chunk_size] for i in range(0, n, chunk_size)]
            if is_list_same(chunks):
                return True
    return False

def part2(data: str) -> int:
    lines = data.strip().split(',')
    result = 0
    for line in lines:
        firstId, lastId = line.split('-')
        start, end = int(firstId), int(lastId)

        for num in range(start, end + 1):
            s = str(num)
            if has_repeating_pattern(s):
                result += num




    return result
