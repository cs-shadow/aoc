import sys

lines = [line.strip() for line in sys.stdin.readlines() if line.strip()]
navigation_str = lines.pop(0).replace("L", "0").replace("R", "1")
navigation = [int(x) for x in navigation_str]

# parse paths
paths = {}
for line in lines:
    source, rest = line.split("=")
    source = source.strip()
    rest = rest.replace("(", "").replace(")", "").strip()
    left, right = rest.split(",")
    left = left.strip()
    right = right.strip()
    paths[source] = [left, right]

source = "AAA"
dest = "ZZZ"
count = 0
length = len(navigation)

# traverse the paths
while source != dest:
    idx = count % length
    source = paths[source][navigation[idx]]
    count += 1

print(count)
