import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

def str_to_binary(s):
    str_list = []
    for c in s:
        ascii_code = ord(c)
        binary_string = '{0:07b}'.format(ascii_code)
        str_list.append(binary_string)

    return ''.join(str_list)


def binary_string_to_pairs(binary_string):
    prev = int(binary_string[0][0])
    count = 0
    pairs = []
    for bit in binary_string:
        bit_n = int(bit)
        if bit_n == prev:
            count = count + 1
        else:
            pairs.append((prev, count))
            prev = bit_n
            count = 1

    pairs.append((prev, count))

    return pairs


def encode_pairs(p):
    str_list = []
    for n, count in p:
        if n == 1:
            str_list.append('0')
        else:
            str_list.append('00')

        count_list = []
        for i in range(count):
            count_list.append('0')

        str_list.append(''.join(count_list))

    return ' '.join(str_list)


def run(str):
    bs = str_to_binary(str)
    pairs = binary_string_to_pairs(bs)
    result = encode_pairs(pairs)
    return result


print(run(message))
