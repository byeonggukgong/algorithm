# -*- coding: utf -*-

if __name__ == '__main__':
    input = int(input())
    output = [1, 2]
    
    for x in range(2, input):
        output.append(output[x - 2] + output[x - 1])
    
    print(output[input - 1] % 10007)
