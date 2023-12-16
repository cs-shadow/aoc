import sys
from collections import defaultdict

def holiday_hash(string):
    value = 0
    for char in string:
        value += ord(char)
        value = (value * 17) % 256
    return value

def find_lens(lenses, label):
    for idx, lens in enumerate(lenses):
        if lens[0] == label:
            return idx
    return None

inputs = sys.stdin.readline().strip().split(",")
boxes = defaultdict(list)

# fill boxes
for step in inputs:
    if step.endswith("-"):
        label = step[:-1]
        box = holiday_hash(label)
        index = find_lens(boxes[box], label)
        if index is not None:
            boxes[box].pop(index)
    else:
        label, length = step.split("=")
        box = holiday_hash(label)
        length = int(length)
        index = find_lens(boxes[box], label)
        if index is not None:
            boxes[box][index][1] = length
        else:
            boxes[box].append([label, length])

# calculate answer
total = 0
for box, lenses in boxes.items():
    for idx, lens in enumerate(lenses):
        total += (box + 1) * (idx + 1) * lens[1]

print(total)
