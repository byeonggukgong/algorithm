# -*- coding: utf-8 -*-

if __name__ == '__main__':
    output = [1 for num in range(10000)]
    
    for num in range(1, 10001):
        num += sum([int(digit) for digit in str(num)])
        
        if num <= 10000:
            output[num - 1] = 0
    
    for num, flag in enumerate(output, 1):
        if flag:
            print(num)
