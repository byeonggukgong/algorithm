# -*- coding: utf-8 -*-

if __name__ == '__main__':
    sum = 0
    
    for x in range(5):
        num = int(input())
        sum += num if num >= 40 else 40
            
    print(int(sum / 5))
