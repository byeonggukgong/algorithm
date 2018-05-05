#  -*- coding: utf-8 -*-

if __name__ == '__main__':
    count = int(input())
    input = str(input())
    output = 0
    
    for x in range(count):
        output += int(input[x])

    print(output)
