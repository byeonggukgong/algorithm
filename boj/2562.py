# -*- coding: utf-8 -*-

import unittest

def maximum_value(numbers: list) -> list:
    result = [0, 0]

    for index, value in enumerate(numbers, 1):
        if result[0] < value:
            result[0] = value
            result[1] = index

    return result


class TestMaximum_value(unittest.TestCase):
    def test_maximum_value(self):
        for numbers, expected in [
            [[3, 29, 38, 12, 57, 74, 40, 85, 61], [85, 8]],
            [[99, 1, 45, 22, 57, 109, 2, 18, 33], [109, 6]],
            [[99, 1, 45, 22, 57, 109, 2, 18, 200], [200, 9]]
        ]:
            self.assertEqual(expected, maximum_value(numbers))


if __name__ == '__main__':
    unittest.main()
