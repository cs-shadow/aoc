import sys
from collections import defaultdict

matrix = []
for line in sys.stdin.readlines():
    matrix.append(list(f".{line.strip()}."))

height = width = len(matrix[0])
dummy_row = [["."] * width]
matrix = dummy_row + matrix + dummy_row

part_numbers = {}
part_number_values = {}
gear_counter = defaultdict(set)

def symbol_neighbors(i, j):
    neighbors = [matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1], matrix[i+1][j+1], matrix[i+1][j], matrix[i][j+1], matrix[i-1][j+1], matrix[i+1][j-1]]
    for x in neighbors:
        if not x.isdigit() and x != ".":
            return True
    return False

def mark_part_neighbors(row, col):
    part_number = part_numbers[(row, col)]
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if matrix[i][j] == "*":
                gear_counter[(i, j)].add(part_number)

# find part numbers
for i in range(width):
    number, close = "", False
    for j in range(height):
        char = matrix[i][j]
        if char.isdigit():
            number += char
            if symbol_neighbors(i, j):
                close = True
        else:
            if number and close:
                for x in range(len(number)):
                    part_numbers[(i, j - x - 1)] = (i, j - 1)
                part_number_values[(i, j - 1)] = int(number)
            number, close = "", False

# remove non-part numbers
for i in range(width):
    for j in range(height):
        if (i, j) not in part_numbers and matrix[i][j] != "*":
            matrix[i][j] = "."

# count gear neighbors
for i in range(width):
    for j in range(height):
        if matrix[i][j].isdigit():
            mark_part_neighbors(i, j)

# finally...
total = 0
for gear, numbers in gear_counter.items():
    numbers = list(numbers)
    if len(numbers) == 2:
        total += part_number_values[numbers[0]] *  part_number_values[numbers[1]]

print(total)
