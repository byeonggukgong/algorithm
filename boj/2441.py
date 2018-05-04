# -*- coding: utf-8 -*-

from sys import stdout

if __name__ == '__main__':
    input = int(input())

    for x in range(input):
        for y in range(x):
            stdout.write(" ")
        for z in range(input - x):
            stdout.write("*")
        print()
