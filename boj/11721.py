# -*- coding: utf-8 -*-

import unittest


def main():
    string = input()

    for line in split_10th(string):
        print(line)

def split_10th(string: str) -> list:
    return [string[idx:idx + 10] for idx in range(0, len(string), 10)]

class TestSplit10th(unittest.TestCase):
    def test_split_10th(self):
        for line, expected in [
            ['BaekjoonOnlineJudge', ['BaekjoonOn', 'lineJudge']],
            ['OneTwoThreeFourFiveSixSevenEightNineTen', [
                'OneTwoThre', 'eFourFiveS', 'ixSevenEig', 'htNineTen'
            ]]
        ]:
            self.assertEqual(expected, split_10th(line))

if __name__ == '__main__':
    main()
