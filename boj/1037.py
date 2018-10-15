# -*- coding: utf-8 -*-

import unittest


def divisor(n: int, divisors: list) -> int:
    divisors = sorted(divisors)

    return divisors[0] * divisors[-1]


class TestDivisor(unittest.TestCase):
    def test_divisor(self):
        for n, divisors, expected in [
            (2, [4, 2], 8), (4, [2, 3, 4, 6], 12),
            (3, [2, 4, 8], 16)
        ]:
            self.assertEqual(expected, divisor(n, divisors))


if __name__ == '__main__':
    unittest.main()
