import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

influences = []
graph = {}

n = int(input())  # the number of relationships of influence
for i in range(n):
    # x: a relationship of influence between two people (x influences y)
    x, y = [int(j) for j in input().split()]
    influences.append((x, y))
    dest_nodes = graph.get(x, [])
    dest_nodes.append(y)
    graph[x] = dest_nodes

# n = 3
# influences = [(1, 2), (1, 3), (3, 4)]
# graph = {1: [2, 3], 3: [4]}
# influences = [(1, 2), (1, 3), (3, 4), (2, 4), (2, 5), (10, 11), (10, 1), (10, 3)]
# graph = {1: [2, 3], 3: [4], 2: [4, 5], 10: [11, 1, 3]}

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

def traverse(node, length):
    if node in graph:
        dest_nodes = graph.get(node)
        dest_node_lengths = []

        for dest_node in dest_nodes:
            dest_node_length = traverse(dest_node, length + 1)
            dest_node_lengths.append(dest_node_length)

        return max(dest_node_lengths)
    else:
        return length

start_nodes = list(graph.keys())
node_lengths = []
for start_node in start_nodes:
    node_length = traverse(start_node, 1)
    node_lengths.append(node_length)

# The number of people involved in the longest succession of influences
print(max(node_lengths))
