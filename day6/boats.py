import sys

lines = sys.stdin.readlines()
times = lines[0].split(":")[-1].strip().split()
distances = lines[1].split(":")[-1].strip().split()

total = 1

for idx, time in enumerate(times):
    time = int(time)
    distance = int(distances[idx])
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

    total *= maxima - minima + 1

print(total)
