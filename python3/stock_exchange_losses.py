import sys
import math
from functools import reduce

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

MAX_INT = 2 ** 31
l = []

n = int(input())
for i in input().split():
    v = int(i)
    l.append(v)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

def drop_ranges(l):
    ranges = []
    start = -1
    end = MAX_INT

    def calc_range(a, b):
        nonlocal start, end
        diff = b - a

        if diff < 0:
            if a > start:
                start = a
            if b < end:
                end = b
        else:
            if start != -1 and b > start:
                ranges.append((start, end))
                start = -1
                end = MAX_INT

        return b


    reduce(calc_range, l)

    if start != -1:
        ranges.append((start, end))

    return ranges


ranges = drop_ranges(l)

max_drop = 0
for start, end in ranges:
    drop = start - end
    if drop > max_drop:
        max_drop = drop

print(-max_drop)
