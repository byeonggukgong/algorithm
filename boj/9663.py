# -*- coding: utf-8 -*-

import unittest

count = 0

def is_promised(queens: list, n: int) -> bool:
    for c in range(n):
        if queens[n] == queens[c] or abs(queens[n] - queens[c]) == abs(n - c):
            return False
    return True

def back_tracking(queens: list, length: int, current: int):
    if current == length:
        global count
        count += 1
        return

    for c in range(length):
        queens[current] = c

        if is_promised(queens, current):
            back_tracking(queens, length, current + 1)

    return

def n_queen(length: int) -> int:
    queens = [-1 for _ in range(length)]

    back_tracking(queens, length, 0)

    return count

class TestNQueen(unittest.TestCase):
    def test_n_queen(self):
        for length, expected in [
            [4, 2], [8, 92]
        ]:
            global count
            count = 0

            self.assertEqual(expected, n_queen(length))

if __name__ == '__main__':
    unittest.main()
