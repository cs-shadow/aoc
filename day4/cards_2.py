import sys

total = 0

card_values = []

for line in sys.stdin.readlines():
    index_str, rest = line.split(":")
    winners_str, ours_str = rest.split("|")
    winners = winners_str.strip().split(" ")
    ours = ours_str.strip().split()

    count = 0
    for num in ours:
        if num in winners:
            count += 1

    card_values.append(count)

card_counts = [1] * len(card_values)

for idx, count in enumerate(card_values):
    for match in range(count):
        card_counts[idx + match + 1] += card_counts[idx]

print(sum(card_counts))
