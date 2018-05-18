# -*- coding: utf-8 -*-

if __name__ == '__main__':
    input = int(input())
    output = 1
    
    for num in range(1, input + 1):
        output *= num
        
    print(output)
