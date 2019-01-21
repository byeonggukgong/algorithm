# -*- coding: utf-8 -*-

import unittest

def turret(x1: int, y1: int, r1: int, x2: int, y2: int, r2: int):
    distance = (x1 - x2) ** 2 + (y1 - y2) ** 2

    if distance == 0:
        return -1 if r1 == r2 else 0
    else:
        if distance == (r1 + r2) ** 2 or distance == (r1 - r2) ** 2:
            return 1
        elif distance < (r1 + r2) ** 2 and distance > (r1 - r2) ** 2:
            return 2
        return 0


class TestTurret(unittest.TestCase):
    def test_turret(self):
        for x1, y1, r1, x2, y2, r2, expected in [
            [0, 0, 13, 40, 0, 37, 2],
            [0, 0, 3, 0, 7, 4, 1],
            [1, 1, 1, 1, 1, 5, 0],
            [1, 1, 1, 1, 1, 1, -1],
            [1, 1, 10, 2, 2, 3, 0],
            [0, 0, 1, 5, 5, 1, 0],
            [0, 0, 100, 142, 142, 100, 0]
        ]:
            self.assertEqual(
                expected, turret(x1, y1, r1, x2, y2, r2))

if __name__ == '__main__':
    unittest.main()
