# -*- coding: utf-8 -*-

if __name__ == '__main__':
    count = int(input())
    
    for x in range(count):
        case = input().split()
        output = str()
        
        for alphanumeric in case[1]:
            output += (alphanumeric * int(case[0]))
            
        print(output)
