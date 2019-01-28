# -*- coding: utf-8 -*-

import unittest

def suger_delivery(weight: int) -> int:
    count = weight // 5

    while count >= 0:
        remain = weight - (count * 5)

        if remain % 3 == 0:
            return count + (remain // 3)

        count -= 1

    return -1

class TestSugerDelivery(unittest.TestCase):
    def test_suger_delivery(self):
        for weight, expected in [
            [18, 4], [4, -1], [6, 2], [9, 3], [11, 3]
        ]:
            self.assertEqual(expected, suger_delivery(weight))

if __name__ == '__main__':
    unittest.main()
