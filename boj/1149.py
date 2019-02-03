# -*- coding: utf-8 -*-

import unittest

def rgb_street(count: int, values: list) -> int:
    dp = [[0 for _ in range(count)] for _ in range(3)]

    dp[0][0] = values[0][0]
    dp[1][0] = values[0][1]
    dp[2][0] = values[0][2]

    for idx in range(1, count):
        dp[0][idx] = min(dp[1][idx - 1], dp[2][idx - 1]) + values[idx][0]
        dp[1][idx] = min(dp[0][idx - 1], dp[2][idx - 1]) + values[idx][1]
        dp[2][idx] = min(dp[0][idx - 1], dp[1][idx - 1]) + values[idx][2]

    return min(dp[0][count - 1], dp[1][count - 1], dp[2][count - 1])

class TestRgbStreet(unittest.TestCase):
    def test_rgb_street(self):
        for count, values, expected in [
            [1, [[100, 99, 88]], 88],
            [3, [[26, 40, 83], [49, 60, 57], [13, 89, 99]], 96],
            [4, [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]], 4]
        ]:
            self.assertEqual(expected, rgb_street(count, values))

if __name__ == '__main__':
    unittest.main()
