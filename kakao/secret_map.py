# -*- coding: utf-8 -*-

import unittest


def secret_map(n: int, arr1: list, arr2: list) -> list:
    output_bin = list(map(
        lambda x, y: f'{x | y:0{n}b}', arr1, arr2))
    output = list(map(
        lambda _: _.replace('0', ' ').replace('1', '#'), output_bin))

    return output


class TestSecretMap(unittest.TestCase):

    def test_secret_map(self):
        for n, arr1, arr2, expected in [
            (5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28],
                ['#####', '# # #', '### #', '#  ##', '#####']),
            (6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10],
                ['######', '###  #', '##  ##', ' #### ', ' #####', '### # '])
        ]:
            self.assertEqual(expected, secret_map(n, arr1, arr2))


if __name__ == '__main__':
    unittest.main()
