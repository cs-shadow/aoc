import sys

matrix = []
for line in sys.stdin.readlines():
    matrix.append(f".{line.strip()}.")

height = width = len(matrix[0])
dummy_row = ["." * width]
matrix = dummy_row + matrix + dummy_row

def symbol_neighbors(i, j):
    neighbors = [matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1], matrix[i+1][j+1], matrix[i+1][j], matrix[i][j+1], matrix[i-1][j+1], matrix[i+1][j-1]]
    for x in neighbors:
        if not x.isdigit() and x != ".":
            return True
    return False

total = 0

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
                total += int(number)
            number, close = "", False

print (total)
