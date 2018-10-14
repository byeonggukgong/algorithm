# -*- coding: utf-8 -*-

import unittest


def reassignment(n: int) -> int:
    return n - int(n / 2)


def tournament(n: int, jimin: int, hansu: int) -> int:
    count = 0

    while(jimin != hansu):
        jimin = reassignment(jimin)
        hansu = reassignment(hansu)

        count += 1

    return count


class Tournament(unittest.TestCase):
    def test_reassignment(self):
        for n, expected in [
            (1, 1), (2, 1),
            (3, 2), (4, 2),
            (7, 4), (8, 4),
            (10, 5), (11, 6)
        ]:
            self.assertEqual(expected, reassignment(n))

    def test_tournament(self):
        for n, jimin, hansu, expected in [
            (16, 8, 9, 4),
            (16, 7, 8, 1),
            (16, 2, 3, 2),
            (8, 5, 2, 3)
        ]:
            self.assertEqual(expected, tournament(n, jimin, hansu))


if __name__ == '__main__':
    unittest.main()
