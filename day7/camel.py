import sys
from collections import Counter

# five of a kind    : 10
# four of a kind    : 9
# full house        : 8
# three of a kind   : 7
# two pair          : 6
# one pair          : 5
# high card         : 1

def calc_value(hand):
    count = Counter()
    for card in hand:
        count[card] += 1

    # five of a kind    : 10
    if count.most_common()[0][1] == 5:
        return 10

    # four of a kind    : 9
    # full house        : 8
    if len(count) == 2:
        if count.most_common()[0][1] == 4:
            return 9
        return 8

    # three of a kind   : 7
    if count.most_common()[0][1] == 3:
        return 7

    # two pair          : 6
    if len(count) == 3:
        return 6

    # one pair          : 5
    if count.most_common()[0][1] == 2:
        return 5

    # high card         : 1
    return 1

class Hand:
    def __init__(self, hand, bet):
        # A -> Z
        # K -> Y
        # Q -> X
        # J -> W
        # T -> T
        self.hand = hand.replace("A", "Z").replace("K", "Y").replace("Q", "X").replace("J", "W")
        self.bet = bet
        self.value = calc_value(self.hand)

hands = []
for line in sys.stdin.readlines():
    hand, bet = line.strip().split()
    bet = int(bet)
    hands.append(Hand(hand, bet))

total = 0
for idx, hand in enumerate(sorted(hands, key=lambda x: (x.value, x.hand))):
    total += hand.bet * (idx + 1)

print(total)
