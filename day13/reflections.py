import sys
from pprint import pp

def reflect_horizontal(block):
    height = len(block)
    for idx in range(1, height):
        size = min(idx, height - idx)
        ups = block[idx-size:idx]
        downs = list(reversed(block[idx:idx+size]))
        if all([ups[i] == downs[i] for i in range(size)]):
            return idx
    return 0

def transpose(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        new_matrix.append(row)
    return new_matrix

total = 0
for section in sys.stdin.read().split("\n\n"):
    section = [list(line) for line in section.split()]
    horizontal = reflect_horizontal(section)
    vertical = reflect_horizontal(transpose(section))
    total += vertical + 100 * horizontal

print(total)
