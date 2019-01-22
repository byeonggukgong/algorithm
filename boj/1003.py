# -*- coding: utf-8 -*-

import unittest

def fibonacci(number: int):
    dp = [[0, 0] for _ in range(41)]

    dp[0][0] = 1
    dp[1][1] = 1

    for n in range(2, number + 1):
        dp[n][0] = dp[n - 2][0] + dp[n - 1][0]
        dp[n][1] = dp[n - 2][1] + dp[n - 1][1]

    return [dp[number][0], dp[number][1]]


class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        for number, expected in [
            [0, [1, 0]],
            [1, [0, 1]],
            [3, [1, 2]],
            [4, [2, 3]],
            [30,[514229, 832040]],
            [39, [39088169, 63245986]],
            [40, [63245986, 102334155]]
        ]:
            self.assertEqual(expected, fibonacci(number))


if __name__ == '__main__':
    unittest.main()
