# -*- coding: utf-8 -*-

import enum
import unittest


def week(month: int, day: int) -> str:
    total = day
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for d in days[:month - 1]:
        total += d

    return Day(total % 7).name

class Day(enum.Enum):
    SUN = 0
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6

class TestWhatDay(unittest.TestCase):
    def test_what_day(self):
        for month, day, expected in [
            [1, 1, 'MON'], [3, 14, 'WED'], [9, 2, 'SUN'],
            [12, 25, 'TUE']
        ]:
            self.assertEqual(expected, week(month, day))

if __name__ == '__main__':
    unittest.main()
