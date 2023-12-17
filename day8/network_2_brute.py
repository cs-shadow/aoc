import sys
from collections import defaultdict

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
count = 0
length = len(navigation)

# traverse the paths
while not all([node.endswith("Z") for node in sources]):
    idx = count % length
    for sid, source in enumerate(sources):
        sources[sid] = paths[source][navigation[idx]]
    count += 1

# well that turned out to be horrifically slow, there's gotta be a better way
print(count)
