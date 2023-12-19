import sys
from copy import deepcopy

def count_springs(springs_in, numbers_in):
    springs, numbers = deepcopy(springs_in), deepcopy(numbers_in)

    # base condition pt 1
    if not springs:
        return 1 if not numbers else 0

    # dots are useless
    if springs[0] == ".":
        return count_springs(springs[1:], numbers)

    # hashes
    if springs[0] == "#":
        # base condition pt 2
        if not numbers:
            return 0

        number = numbers.pop(0)
        length = len(springs)
        if number > length:
            return 0
        if any([springs[x] == "." for x in range(number)]):
            return 0
        springs = springs[number:]
        if springs:
            if springs[0] == "#":
                return 0
            springs[0] = "."
        # next must be dot
        return count_springs(springs, numbers)

    springs.pop(0)
    # unknown
    count_dot = count_springs(springs, numbers)
    count_hash = count_springs(["#"] + springs, numbers)
    return count_dot + count_hash

total = 0
for line in sys.stdin.readlines():
    springs, numbers = line.strip().split()
    numbers = [int(x) for x in numbers.split(",")]
    total += count_springs(list(springs), numbers)

print(total)
