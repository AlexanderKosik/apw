import random
import copy
l = [" " for _ in range(400)]
l[200] = "#"

# Rule 30
lookup = {
    "###": " ",
    "## ": "#",
    "# #": "#",
    "#  ": " ",
    " ##": "#",
    " # ": "#",
    "  #": "#",
    "   ": " "
}

# Rule 90
lookup = {
    "###": " ",
    "## ": "#",
    "# #": " ",
    "#  ": "#",
    " ##": "#",
    " # ": " ",
    "  #": "#",
    "   ": " "
}


def window(data, pos):
    return "".join(str(x) for x in data[pos-1:pos+2])

def update(l):
    new_l = copy.deepcopy(l)
    for pos in range(len(l)):
        new_l[pos] = lookup.get(window(l, pos), " ")
    return new_l

def draw(l):
    print("".join(l), end="")

while True:
    draw(l)
    input()
    l = update(l)


