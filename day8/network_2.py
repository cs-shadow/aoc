import math
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

sources = [node for node in paths if node.endswith("A")]
dests = [node for node in paths if node.endswith("Z")]
length = len(navigation)
possies = []

# traverse the paths
for source in sources:
    count = 0
    while source not in dests:
        idx = count % length
        source = paths[source][navigation[idx]]
        count += 1
    possies.append(count)

print(math.lcm(*possies))
