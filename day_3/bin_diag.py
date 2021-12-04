#!/usr/bin/env python3
# Copyright (c) 2021, Kai Wolf
# For the licensing terms see LICENSE file in the root directory. For the
# list of contributors see the AUTHORS file in the same directory.i

from statistics import mode, multimode


def main():
    with open('input.txt') as infile:
        input = infile.read()

    gamma = "".join(list(map(mode, list(map(list, zip(*input.split()))))))
    eps = "".join(['0' if x == '1' else '1' for x in gamma])
    power = int(gamma, 2) * int(eps, 2)
    print(power)

    oxy = co2 = input.split()
    bit = 0
    while True:
        if len(oxy) == 1 and len(co2) == 1: break
        m1 = max(multimode(list(map(list, zip(*oxy)))[bit]))
        m2 = max(multimode(list(map(list, zip(*co2)))[bit]))
        if len(oxy) > 1: oxy = list(filter(lambda x: x[bit] == m1, oxy))
        if len(co2) > 1: co2 = list(filter(lambda x: x[bit] != m2, co2))
        bit += 1
    lsr = int(oxy[0], 2) * int(co2[0], 2)
    print(lsr)


if __name__ == "__main__":
    main()
