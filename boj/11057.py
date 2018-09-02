# -*- coding: utf-8 -*-

if __name__ == '__main__':
    digit = int(input())
    dp = [[0] * 10 for _ in range(digit)]

    for n in range(10):
        dp[0][n] = 1

    for x in range(1, digit):
        for y in range(10):
            for z in range(y, 10):
                dp[x][y] += dp[x - 1][z]

    total = sum(dp[digit - 1])

    print(total % 10007)
