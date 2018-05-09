# -*- coding: utf-8 -*-

if __name__ == '__main__':
    first = int(input())
    second = int(input())
    third = int(input())
    output = [0 for x in range(10)]
    multiply = str(first * second * third)
    
    for num in multiply:
        output[int(num)] += 1

    for num in output:
        print(num)
