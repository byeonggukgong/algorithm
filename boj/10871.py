# -*- coding: utf-8 -*-

if __name__ == '__main__':
    inputs = [int(num) for num in input().split()]
    sequence = [int(num) for num in input().split()]
    output = list()
    
    for num in sequence:        
        if num < inputs[1]:
            output.append(str(num))
    
    print(" ".join(output))
