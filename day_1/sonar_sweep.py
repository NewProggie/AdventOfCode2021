#!/usr/bin/env python3
# Copyright (c) 2021, Kai Wolf
# For the licensing terms see LICENSE file in the root directory. For the
# list of contributors see the AUTHORS file in the same directory.


def main():
    with open('input.txt') as infile:
        depths = list(map(int, infile.read().split()))

    count = lambda s: sum([1 for idx, x in enumerate(s[:-1]) if x < s[idx + 1]])
    print(count(depths))
    threes = [sum(depths[idx:idx + 3]) for idx, _ in enumerate(depths[:-2])]
    print(count(threes))


if __name__ == "__main__":
    main()
