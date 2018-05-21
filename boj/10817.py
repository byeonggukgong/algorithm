# -*- coding: utf-8 -*-

if __name__ == '__main__':
    x, y, z = [int(num) for num in input().split()]
    output = 0
    
    if x > y:
        if y > z:
            output = y
        else:
            if x > z:
                output = z
            else:
                output = x
    else:
        if x > z:
            output = x
        else:
            if y > z:
                output = z
            else:
                output = y

    print(output)
