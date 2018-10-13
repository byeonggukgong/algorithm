# -*- coding: utf-8 -*-

import unittest


def escape_rectangle(x: int, y: int, w: int, h: int) -> int:
    return min([x - 0, y - 0, w - x, h - y])


class EscapeRectangle(unittest.TestCase):
    def test_escape_rectangle(self):
        for x, y, w, h, expected in [
            (6, 2, 10, 3, 1),
            (2, 1, 150, 3, 1),
            (98, 98, 100, 100, 2),
            (10, 100, 100, 500, 10)
        ]:
            self.assertEqual(expected, escape_rectangle(x, y, w, h))


if __name__ == '__main__':
    unittest.main()
