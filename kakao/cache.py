# -*- coding: utf-8 -*-

import unittest


def cache(cache_size: int, cities: list) -> int:
    cache = list()
    cache_dict = {'hit': 1, 'miss': 5}
    cities_lower = list(map(lambda _: _.lower(), cities))

    runtime = 0

    for city in cities_lower:
        if city in cache:
            cache.remove(city)
            cache.append(city)

            runtime += cache_dict['hit']
        else:
            if cache_size != 0:
                if cache_size == len(cache):
                    cache.pop(0)

                cache.append(city)

            runtime += cache_dict['miss']

    return runtime


class TestCache(unittest.TestCase):
    def test_cache(self):
        for cache_size, cities, expected in [
            (3, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA',
                 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA'], 50),
            (3, ['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo',
                 'Seoul', 'Jeju', 'Pangyo', 'Seoul'], 21),
            (2, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA',
                 'SanFrancisco', 'Seoul', 'Rome', 'Paris',
                 'Jeju', 'NewYork', 'Rome'], 60),
            (5, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA',
                 'SanFrancisco', 'Seoul', 'Rome', 'Paris',
                 'Jeju', 'NewYork', 'Rome'], 52),
            (2, ['Jeju', 'Pangyo', 'NewYork', 'newyork'], 16),
            (0, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA'], 25)
        ]:
            self.assertEqual(expected, cache(cache_size, cities))


if __name__ == '__main__':
    unittest.main()
