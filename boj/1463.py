# -*- coding: utf -*-

if __name__ == '__main__':
    input = int(input())
    output = [0 for x in range(input)]
    
    for x in range(1, input):
        output[x] = output[x - 1] + 1
        
        if (x + 1) % 2 == 0:
            output[x] = min(output[x], output[int((x + 1) / 2) - 1] + 1)
            
        if (x + 1) % 3 == 0:
            output[x] = min(output[x], output[int((x + 1) / 3) - 1] + 1)

    print(output[input - 1])
