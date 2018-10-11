# -*- coding: utf-8 -*-

import unittest


def treasure(size: int, l1: list, l2: list) -> int:
    if len(l1) != size or len(l2) != size:
        raise IndexError

    l1 = sorted(l1)
    l2 = sorted(l2, reverse=True)

    return sum(list(map(lambda x, y: x * y, l1, l2)))


class Treasure(unittest.TestCase):
    def test_treasure(self):
        for size, l1, l2, expected in [
            (5, [1, 1, 1, 6, 0], [2, 7, 8, 3, 1], 18),
            (3, [0, 0, 1], [2, 7, 8], 2),
            (6, [10, 2, 3, 18, 2, 3], [2, 4, 0, 1, 3, 10], 53)
        ]:
            self.assertEqual(expected, treasure(size, l1, l2))


if __name__ == '__main__':
    unittest.main()
