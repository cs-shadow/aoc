import sys

lines = sys.stdin.readlines()
time = int(lines[0].split(":")[-1].strip().replace(" ", ""))
distance = int(lines[1].split(":")[-1].strip().replace(" ", ""))

minima, maxima = None, None

for x in range(1, time):
    possy = x * (time - x)
    if possy > distance:
        minima = x
        break

for x in range(time - 1, 0, -1):
    possy = x * (time - x)
    if possy > distance:
        maxima = x
        break

print(maxima - minima + 1)
