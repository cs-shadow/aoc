import sys

total = 0

cards = []

for line in sys.stdin.readlines():
    index_str, rest = line.split(":")
    winners_str, ours_str = rest.split("|")
    winners = winners_str.strip().split(" ")
    ours = ours_str.strip().split()

    count = 0
    for num in ours:
        if num in winners:
            count += 1

    if count:
        total += pow(2, count - 1)

print(total)
