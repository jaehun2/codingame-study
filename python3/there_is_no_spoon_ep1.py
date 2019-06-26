import sys
import math
import itertools

# Don't let the machines win. You are humanity's last hope...

# nodes = []
#
# width = int(input())  # the number of cells on the X axis
# height = int(input())  # the number of cells on the Y axis
# for i in range(height):
#     line = input()  # width characters, each either 0 or .
#     nodes.append(list(line))

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

not_found = [-1, -1]

nodes = [['0', '0', '.'], ['0', '.', '.'], ['0', '0', '0']]
width = 3
height = 3

def get_neighbor_nodes(x, y):
    def find_right(ix):
        if ix > width - 1:
            return not_found
        node = nodes[y][ix]
        if node == '0':
            return [ix, y]
        else:
            return find_right(ix + 1)

    def find_bottom(iy):
        if iy > height - 1:
            return not_found
        node = nodes[iy][x]
        if node == '0':
            return [x, iy]
        else:
            return find_bottom(iy + 1)

    return [find_right(x + 1), find_bottom(y + 1)]


# Three coordinates: a node, its right neighbor, its bottom neighbor
# print("0 0 1 0 0 1")

results = []
for y in range(height):
    for x in range(width):
        if nodes[y][x] == '0':
            result = get_neighbor_nodes(x, y)
            result.insert(0, [x, y])
            results.append(list(itertools.chain.from_iterable(result)))

for result in results:
    print(" ".join(map(str, result)))
