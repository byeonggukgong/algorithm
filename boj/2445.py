# -*- coding: utf-8 -*-

from sys import stdout

if __name__ == '__main__':
    input = int(input())
    
    for w in range(input, 0, -1):
        for x in range(input - w + 1):
            stdout.write("*")
        for y in range((2 * w) - 2):
            stdout.write(" ")
        for z in range(input - w + 1):
            stdout.write("*")

        print()

    for w in range(1, input):
        for x in range(input - w):
            stdout.write("*")
        for y in range(2 * w):
            stdout.write(" ")
        for z in range(input - w):
            stdout.write("*")

        print()
