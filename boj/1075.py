# -*- coding: utf-8 -*-

import unittest


def division(n: int, f: int) -> str:
    n = int(n / 100) * 100
    d = f - (n % f) if n % f != 0 else 0

    return f'{d:02}'


class TestDivision(unittest.TestCase):
    def test_division(self):
        for n, f, expected in [
            (1000, 3, '02'), (700, 7, '00'),
            (1021, 11, '01'), (275, 5, '00'),
            (11234, 88, '64'), (574, 100, '00'),
            (101, 2, '00'), (1100, 3, '01'),
            (1999999999, 3, '02'), (100, 1, '00')
        ]:
            self.assertEqual(expected, division(n, f))


if __name__ == '__main__':
    unittest.main()
