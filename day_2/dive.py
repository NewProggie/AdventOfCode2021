#!/usr/bin/env python3
# Copyright (c) 2021, Kai Wolf
# For the licensing terms see LICENSE file in the root directory. For the
# list of contributors see the AUTHORS file in the same directory.i

from collections import defaultdict


def main():
    with open('input.txt') as infile:
        input = infile.read()
        dives = list(zip(input.split()[::2], map(int, input.split()[1::2])))

    d = defaultdict(list)
    for k, v in dives: d[k].append(v)
    hpos = sum(d['forward'])
    depth = sum(d['down']) - sum(d['up'])
    print(hpos * depth)

    aim, depth = 0, 0
    for cmd, val in dives:
        if cmd == 'forward': depth += val * aim
        elif cmd == 'down': aim += val
        elif cmd == 'up': aim -= val
    print(hpos * depth)


if __name__ == "__main__":
    main()
