# -*- coding: utf-8 -*-

if __name__ == '__main__':
    input = [int(num) for num in input().split()]
    
    print((input[0] + input[1]) % input[2])
    print(((input[0] % input[2]) + (input[1] % input[2])) % input[2])
    print((input[0] * input[1]) % input[2])
    print(((input[0] % input[2]) * (input[1] % input[2])) % input[2])
