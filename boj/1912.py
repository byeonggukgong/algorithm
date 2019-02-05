# -*- coding: utf-8 -*-

import unittest


def continuous_sum(count: int, nums: list) -> int:
    dp = [0 for _ in range(count)]

    dp[0] = nums[0]

    for idx in range(1, count):
        if dp[idx - 1] + nums[idx] < nums[idx]:
            dp[idx] = nums[idx]
        else:
            dp[idx] = dp[idx - 1] + nums[idx]

    return max(dp)

class TestcontinuousSum(unittest.TestCase):
    def test_continuous_sum(self):
        for count, nums, expected in [
            [1, [-4], -4],
            [5, [-1, 100, -2, 90, 5], 193],
            [7, [-1, -2, -3, 4, 5, -2, 100], 107],
            [10, [10, -4, 3, 1, 5, 6, -35, 12, 21, -1], 33]
        ]:
            self.assertEqual(expected, continuous_sum(count, nums))

if __name__ == '__main__':
    unittest.main()
