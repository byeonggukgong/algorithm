# -*- coding: utf-8 -*-

import unittest

def go_up_stairs(count: int, stairs: list) -> int:
    dp = [0 for _ in range(count)]

    dp[0] = stairs[0]
    dp[1] = max(stairs[0], stairs[0] + stairs[1])
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

    for idx in range(3, count):
        dp[idx] = max(dp[idx - 3] + stairs[idx - 1] + stairs[idx], dp[idx - 2] + stairs[idx])

    return dp[-1]

class TestGoUpStairs(unittest.TestCase):
    def test_go_up_stairs(self):
        for count, stairs, expected in [
            [6, [1, 1, 2, 2, 1, 1], 6],
            [6, [10, 20, 15, 25, 10, 20], 75]
        ]:
            self.assertEqual(expected, go_up_stairs(count, stairs))

if __name__ == '__main__':
    unittest.main()
