import sys

class Pick:
    def __init__(self, red, green, blue):
        self.red = red
        self.blue = blue
        self.green = green

    def max(self, other):
        return Pick(max(self.red, other.red), max(self.green, other.green), max(self.blue, other.blue))

    def power(self):
        return self.red * self.green * self.blue

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

total = 0

for line in sys.stdin.readlines():
    cube_limit = Pick(0, 0, 0)
    input_str = line.split(":")[1]
    for pick_str in input_str.split(";"):
        pick = find_pick(pick_str)
        cube_limit = pick.max(cube_limit)
    total += cube_limit.power()

print(total)
