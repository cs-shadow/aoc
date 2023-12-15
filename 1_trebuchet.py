import sys

total = 0

for line in sys.stdin.readlines():
    digits = [int(char) for char in line if char.isdigit()]
    total += digits[0] * 10 + digits[-1]

print(total)
