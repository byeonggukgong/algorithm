# -*- coding: utf-8 -*-

from sys import stdout

if __name__ == '__main__':
    input = int(input())
    
    for x in range(input, 0, -1):
        for y in range(input - x):
            stdout.write(" ")
        for z in range((x * 2) - 1):
            stdout.write("*")

        print()
