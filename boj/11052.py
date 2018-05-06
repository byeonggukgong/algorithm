# -*- coding: utf-8 -*-

if __name__ == '__main__':
    count  = int(input())
    prices = [int(price) for price in input().split()]
    maximum = [0 for price in prices]

    for x in range(count):
        for y in range(x + 1):
            if x == y:
                maximum[x] = max(prices[y], maximum[x])
            else:
                maximum[x] = max(maximum[x - (y + 1)] + prices[y], maximum[x])

    print(maximum[count - 1])
