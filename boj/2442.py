# -*- coding: utf-8 -*-

from sys import stdout

if __name__ == '__main__':
    input = int(input())
    
    for x in range(1, input + 1):
        for y in range(input - x):
            stdout.write(" ")
        for z in range((2 * x) - 1):
            stdout.write("*")
        
        print()
