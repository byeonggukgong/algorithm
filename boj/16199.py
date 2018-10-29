# -*- coding: utf-8 -*-

import unittest


def calculate_age(birth, standard):
    b_y, b_m, b_d = birth
    s_y, s_m, s_d = standard

    m, s, y = 0, 0, 0

    y = s_y - b_y
    s = y + 1

    m = y if s_m - b_m > 0 or (s_m == b_m and s_d >= b_d) else y - 1

    return([m, s, y])


class TestCalculateAge(unittest.TestCase):
    def test_calculate_age(self):
        for birth, standard, expected in [
            ([2003, 3, 5], [2003, 3, 5], [0, 1, 0]),
            ([2003, 3, 5], [2003, 3, 6], [0, 1, 0]),
            ([2003, 3, 5], [2003, 4, 1], [0, 1, 0]),
            ([2003, 3, 5], [2003, 4, 5], [0, 1, 0]),
            ([2003, 3, 5], [2004, 1, 1], [0, 2, 1]),
            ([2003, 3, 5], [2004, 3, 4], [0, 2, 1]),
            ([2003, 3, 5], [2004, 3, 5], [1, 2, 1]),
            ([2005, 1, 1], [2007, 1, 1], [2, 3, 2]),
            ([2005, 1, 2], [2007, 1, 1], [1, 3, 2]),
            ([2005, 12, 31], [2007, 1, 1], [1, 3, 2]),
            ([2006, 1, 1], [2007, 1, 1], [1, 2, 1])
        ]:
            self.assertEqual(expected, calculate_age(birth, standard))


if __name__ == '__main__':
    unittest.main()
