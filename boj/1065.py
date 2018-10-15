# -*- coding: utf-8 -*-

import unittest


def is_hansu(n: int) -> bool:
    if n < 100:
        return True
    else:
        d = list()

        while(n >= 10):
            t = n % 10
            n = int(n / 10)
            d.append(t - (n % 10))

        if len(set(d)) == 1:
            return True

    return False


def hansu(n: int) -> int:
    count = 0

    for _ in range(1, n + 1):
        if is_hansu(_):
            count += 1

    return count


class TestHansu(unittest.TestCase):
    def test_is_hansu(self):
        for n, expected in [
            (1, True), (2, True), (110, False),
            (111, True), (246, True), (530, False),
            (531, True), (556, False), (1000, False)
        ]:
            self.assertEqual(expected, is_hansu(n))

    def test_hansu(self):
        for n, expected in [
            (110, 99), (531, 120), (530, 119),
            (1000, 144)
        ]:
            self.assertEqual(expected, hansu(n))


if __name__ == '__main__':
    unittest.main()
