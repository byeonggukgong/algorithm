# -*- coding: utf-8 -*-

import re
import unittest


def dart_game(result: str) -> int:
    acc = list(map(lambda _: 0, range(3)))

    pows_dict = {'S': 1, 'D': 2, 'T': 3}
    prizes_dict = {'#': -1, '*': 2}

    scores = re.findall('\d+', result)
    options = re.findall('\D+', result)

    for r in range(3):
        acc[r] = pow(int(scores[r]), pows_dict[options[r][0]])

        if options[r][1:] in prizes_dict.keys():
            if options[r][1] == '#':
                acc[r] *= -1

            if options[r][1] == '*':
                acc[r] *= 2

                if r != 0:
                    acc[r - 1] *= 2

    return sum(acc)


class TestDartGame(unittest.TestCase):

    def test_dart_game(self):
        for result, expected in [
            ('1S2D*3T', 37), ('1D2S#10S', 9),
            ('1D2S0T', 3), ('1S*2T*3S', 23),
            ('1D#2S*3S', 5), ('1T2D3D#', -4),
            ('1D2S3T*', 59)
        ]:
            self.assertEqual(expected, dart_game(result))


if __name__ == '__main__':
    unittest.main()
