# -*- coding: utf-8 -*-

import collections
import re
import unittest


def multiset(str1: str) -> list:
    multiset = list(map(lambda s1, s2: (s1 + s2).lower(), str1[:-1], str1[1:]))
    multiset = list(filter(lambda _: re.match('[a-zA-Z]{2}', _), multiset))

    return multiset


def jarccard_similarity(str1: str, str2: str) -> float:
    ms1 = collections.Counter(multiset(str1))
    ms2 = collections.Counter(multiset(str2))

    if not ms1 or not ms2:
        return 1

    return sum((ms1 & ms2).values()) / sum((ms1 | ms2).values())


def news_clustering(str1: str, str2: str) -> int:
    return int(jarccard_similarity(str1, str2) * 65536)


class TestNewsClustering(unittest.TestCase):
    def test_multiset(self):
        for str1, expected in [
            ('FRANCE', ['fr', 'ra', 'an', 'nc', 'ce']),
            ('french', ['fr', 're', 'en', 'nc', 'ch']),
            ('handshake', ['ha', 'an', 'nd', 'ds', 'sh', 'ha', 'ak', 'ke']),
            ('shake hands', ['sh', 'ha', 'ak', 'ke', 'ha', 'an', 'nd', 'ds']),
            ('aa1+aa2', ['aa', 'aa']),
            ('AAAA12', ['aa', 'aa', 'aa']),
            ('E=M*C^2', []),
            ('e=m*c^2', [])
        ]:
            self.assertEqual(expected, multiset(str1))

    def test_news_clustering(self):
        for str1, str2, expected in [
            ('FRANCE', 'french', 16384),
            ('handshake', 'shake hands', 65536),
            ('aa1+aa2', 'AAAA12', 43690),
            ('E=M*C^2', 'e=m*c^2', 65536)
        ]:
            self.assertEqual(expected, news_clustering(str1, str2))


if __name__ == '__main__':
    unittest.main()
