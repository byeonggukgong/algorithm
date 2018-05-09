# -*- coding: utf-8 -*-

if __name__ == '__main__':
    input = [str(num) for num in input().split()]
    
    x = int(input[0][::-1])
    y = int(input[1][::-1])
    
    print(x) if x > y else print(y)
