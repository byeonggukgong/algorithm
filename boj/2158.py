# -*- coding: utf-8 -*-

import unittest

def wine_tasting(count: int, amount: list) -> int:
    dp = [0 for _ in range(count)]

    dp[0] = amount[0]

    if count > 1:
        dp[1] = dp[0] + amount[1]

    for idx in range(2, count):
        dp[idx] = max(
            dp[idx - 1],
            dp[idx - 2] + amount[idx],
            dp[idx - 3] + amount[idx - 1] + amount[idx])

    return dp[count - 1]

class TestWineTasing(unittest.TestCase):
    def test_wine_tasting(self):
        for count, amount, expected in [
            [1, [1], 1],
            [6, [6, 10, 13, 9, 8, 1], 33],
            [6, [1000, 900, 2, 1, 800, 700], 3400],
            [12, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0]
        ]:
            self.assertEqual(expected, wine_tasting(count, amount))

if __name__ == '__main__':
    unittest.main()
