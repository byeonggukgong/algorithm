# -*- coding: utf-8 -*-

import unittest


def z(n: int, r: int, c: int, num: int = 0) -> int:
    if n == 0:
        return num

    length = 2 ** n
    length_half = int(length / 2)
    area = length_half ** 2

    return 2 * area * int(r / length_half) + area * int(c / length_half) \
        + z(n - 1, r % length_half, c % length_half, num)


class TestZ(unittest.TestCase):
    def test_z(self):
        for n, r, c, expected in [
            (1, 0, 0, 0), (2, 0, 0, 0), (2, 3, 0, 10),
            (2, 3, 1, 11), (3, 7, 7, 63), (15, 0, 0, 0),
        ]:
            self.assertEqual(expected, z(n, r, c))


if __name__ == '__main__':
    unittest.main()
