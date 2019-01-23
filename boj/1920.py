# -*- coding: utf-8 -*-

import unittest

def binary_search(sorted_list: list, first: int, last: int, target: int) -> int:

    mid = int((first + last) / 2)

    if first > last:
        return 0
    elif target == sorted_list[mid]:
        return 1
    else:
        if target > sorted_list[mid]:
            return binary_search(sorted_list, mid + 1, last, target)
        else:
            return binary_search(sorted_list, first, mid - 1, target)

def find_number(n: list, m: list) -> list:
    result = []

    n.sort()

    for number in m:
        result.append(binary_search(n, 0, len(n) - 1, number))

    return result


class TestFindNumber(unittest.TestCase):
    def test_find_number(self):
        for n, m, expected in [
            [
                [4, 1, 5, 2, 3],
                [1, 3, 7, 9, 3],
                [1, 1, 0, 0, 1]
            ],
            [
                [1, 4, 99, 3, 2, 6, 7],
                [5, 4, 3, 2, 1, 6, 7, 10, 20, 60, 70],
                [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]
            ]
        ]:
            self.assertEqual(expected, find_number(n, m))


if __name__ == '__main__':
    unittest.main()
