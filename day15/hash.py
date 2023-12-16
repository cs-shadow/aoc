import sys

def holiday_hash(string):
    value = 0
    for char in string:
        value += ord(char)
        value = (value * 17) % 256
    return value

inputs = sys.stdin.readline().strip().split(",")
print(sum([holiday_hash(string) for string in inputs]))
