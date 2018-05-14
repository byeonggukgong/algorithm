# -*- coding: utf-8 -*-

from sys import stdout

if __name__ == '__main__':
    input = int(input())
    
    for x in range(1, input + 1):
        for y in range(x):
            stdout.write("*")

        print()
    
    for x in range(input - 1, 0, -1):
        for y in range(x):
            stdout.write("*")
            
        print()
