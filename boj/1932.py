# -*- coding: utf-8 -*-

if __name__ == '__main__':
    width = int(input())
    output = [0 for num in range(width)]
    
    for x in range(width):
        height = [int(num) for num in input().split()]
        
        for y in range(x + 1):
            if y == 0:
                height[y] = output[y] + height[y]
            elif y == x:
                height[y] = output[y - 1] + height[y]
            else:
                height[y] = max(output[y - 1] + height[y], output[y] + height[y])

        output = height[:]

    print(max(output))
