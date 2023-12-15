import sys


# prepare our cheatsheet
possible_digits = {}
for i in range(1, 10):
    possible_digits[str(i)] = i
for idx, x in enumerate(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
    possible_digits[x] = idx + 1

def find_digits(line):
    digits = []
    for start in range(len(line)):
        for end in range(start + 1, len(line)):
            possy = line[start:end]
            if possy in possible_digits:
                digits.append(possible_digits[possy])
    return digits

total = 0

for line in sys.stdin.readlines():
    digits = find_digits(line)
    total += digits[0] * 10 + digits[-1]

print(total)
