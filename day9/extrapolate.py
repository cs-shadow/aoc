import sys

def find_next(elements):
    if all([x == 0 for x in elements]):
        return 0
    diff_list = [elements[x] - elements[x-1] for x in range(1, len(elements))]
    return find_next(diff_list) + elements[-1]

total = 0
for line in sys.stdin.readlines():
    elements = [int(element) for element in line.strip().split()]
    total += find_next(elements)

print(total)
