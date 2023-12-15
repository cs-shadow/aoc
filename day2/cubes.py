import sys

class Pick:
    def __init__(self, red, green, blue):
        self.red = red
        self.blue = blue
        self.green = green

    def __repr__(self):
        return f"{self.red} Red, {self.green} Green, {self.blue} Blue"

    def __gt__(self, other):
        return self.red > other.red or self.green > other.green or self.blue > other.blue

def find_pick(line):
    red, green, blue = 0, 0, 0
    for pick in [x.strip() for x in line.split(",")]:
        num, color = pick.split(" ")
        if color == "red":
            red = int(num)
        if color == "green":
            green = int(num)
        if color == "blue":
            blue = int(num)
    return Pick(red=red, green=green, blue=blue)

cube_limit = Pick(red=12, green=13, blue=14)
total = 0

for line in sys.stdin.readlines():
    index_str, input_str = line.split(":")
    index = int(index_str.replace("Game", "").strip())
    for pick_str in input_str.split(";"):
        pick = find_pick(pick_str)
        if pick > cube_limit:
            break
    else:
        total += index

print(total)
