import sys

def parse_map(lines):
    mapp = {}
    for line in lines:
        parts = [int(x) for x in line.split()]
        mapp[parts[1]] = (parts[2], parts[0])
    return mapp

def find_mapped_val(mapp, target):
    for key, vals in mapp.items():
        if target < key:
            continue
        if target <= key + vals[0]:
            idx = target - key
            return vals[1] + idx
    return target

# read/parse data
sections_raw = sys.stdin.read().split("\n\n")
seeds_str = sections_raw.pop(0)
seeds = [int(x) for x in seeds_str.split(":")[1].strip().split()]
sections = []
for section in sections_raw:
    section = section.strip().split("\n")
    section.pop(0)
    sections.append(parse_map(section))

values = []
# map all the maps
for seed in seeds:
    target = seed
    for section in sections:
        value = find_mapped_val(section, target)
        target = value
    values.append(value)

print(min(values))
