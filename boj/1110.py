# -*- coding: utf-8 -*-

if __name__ == '__main__':
    input = int(input())
    output = 0
    temp = input
    
    while True:
        temp = temp % 10 * 10 + (int(temp / 10) + temp % 10) % 10
        output += 1
        
        if input == temp:
            break
            
    print(output)
