import sys

def parse_map(lines):
    mapp = {}
    for line in lines:
        parts = [int(x) for x in line.split()]
        mapp[parts[0]] = (parts[2], parts[1])
    return mapp

def find_mapped_val(mapp, target):
    for key, vals in mapp.items():
        if target < key:
            continue
        if target <= key + vals[0]:
            idx = target - key
            return vals[1] + idx
    return target

# read/parse data ... but in reverse
sections_raw = sys.stdin.read().split("\n\n")
seeds_str = sections_raw.pop(0)
seeds = [int(x) for x in seeds_str.split(":")[1].strip().split()]
sections = []
for section in sections_raw:
    section = section.strip().split("\n")
    section.pop(0)
    sections.insert(0, parse_map(section))

# redo seeds
new_seeds = []
length = int(len(seeds) / 2)
for i in range(length):
    start = seeds[i * 2]
    new_seeds.append((start, seeds[i * 2 + 1]))

def is_seed(value):
    for start, length in new_seeds:
        if target < start:
            continue
        if target <= start + length:
            return True
    return False

# map all the maps ... also in reverse
for location in range(0, 9999999999999999999):
    target = location
    for section in sections:
        value = find_mapped_val(section, target)
        target = value
    if is_seed(value):
        print(location)
        break
