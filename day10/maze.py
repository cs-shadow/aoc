import sys
from networkx import Graph

maze = Graph()
start = None
lines = []

# padding
for line in sys.stdin.readlines():
    lines.append(f".{line.strip()}.")
padding = ["." * len(lines[0])]
lines = padding + lines + padding

# nodes
for i, line in enumerate(lines):
    for j, _ in enumerate(line):
        maze.add_node(f"{i},{j}")

# edges
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        label = f"{i},{j}"
        if char == "S":
            start = label
        elif char == "|":
            if lines[i-1][j] in ("|", "F", "7", "S"):
                maze.add_edge(label, f"{i-1},{j}")
            if lines[i+1][j] in ("|", "J", "L", "S"):
                maze.add_edge(label, f"{i+1},{j}")
        elif char == "-":
            if lines[i][j-1] in ("-", "F", "L", "S"):
                maze.add_edge(label, f"{i},{j-1}")
            if lines[i][j+1] in ("-", "J", "7", "S"):
                maze.add_edge(label, f"{i},{j+1}")
        elif char == "L":
            if lines[i-1][j] in ("|", "F", "7", "S"):
                maze.add_edge(label, f"{i-1},{j}")
            if lines[i][j+1] in ("-", "J", "7", "S"):
                maze.add_edge(label, f"{i},{j+1}")
        elif char == "J":
            if lines[i-1][j] in ("|", "F", "7", "S"):
                maze.add_edge(label, f"{i-1},{j}")
            if lines[i][j-1] in ("-", "F", "L", "S"):
                maze.add_edge(label, f"{i},{j-1}")
        elif char == "7":
            if lines[i+1][j] in ("|", "J", "L", "S"):
                maze.add_edge(label, f"{i+1},{j}")
            if lines[i][j-1] in ("-", "F", "L", "S"):
                maze.add_edge(label, f"{i},{j-1}")
        elif char == "F":
            if lines[i+1][j] in ("|", "J", "L", "S"):
                maze.add_edge(label, f"{i+1},{j}")
            if lines[i][j+1] in ("-", "J", "7", "S"):
                maze.add_edge(label, f"{i},{j+1}")

# traverse
distances = {start: 0}
remaining = [start]
while remaining:
    current = remaining.pop(0)
    distance = distances[current] + 1
    for neighbor in maze.neighbors(current):
        if neighbor not in distances or distance < distances[neighbor]:
            remaining.append(neighbor)
            distances[neighbor] = distance

print(max(distances.values()))
