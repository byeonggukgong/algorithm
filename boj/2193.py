# -*- coding: utf-8 -*-

import unittest

def binary_number(digits: int) -> int:
    dp = [[0 for _ in range(digits)] for _ in range(2)]

    dp[0][0] = 0
    dp[1][0] = 1

    for idx in range(1, digits):
        dp[0][idx] = dp[0][idx - 1] + dp[1][idx - 1]
        dp[1][idx] = dp[0][idx - 1]

    return dp[0][digits - 1] + dp[1][digits - 1]

class TestBinaryNumber(unittest.TestCase):
    def test_binary_number(self):
        for digits, expected in [
            [3, 2], [4, 3], [5, 5]
        ]:
            self.assertEqual(expected, binary_number(digits))

if __name__ == '__main__':
    unittest.main()
