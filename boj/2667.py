# -*- coding: utf-8 -*-

import unittest

def bfs(start: tuple, matrix: list) -> list:
    queue = [start]
    visited = [start]
    length = len(matrix)

    while queue:
        row, col = queue.pop(0)

        for r, c in list(zip([-1, 0, 1, 0], [0, 1, 0, -1])):
            if 0 <= row + r < length and 0 <= col + c < length:
                apartment = (row + r, col + c)
                existed = matrix[apartment[0]][apartment[1]]

                if existed and not apartment in visited:
                    queue.append(apartment)
                    visited.append(apartment)

    return visited

def numbering_apartment_complexes(matrix: list) -> list:
    apartment_complexes = []
    visited = []

    for row, cols in enumerate(matrix):
        for col, existed in enumerate(cols):
            apartment = (row, col)

            if existed and not apartment in visited:
                apartments = bfs((row, col), matrix)

                apartment_complexes.append(apartments)
                visited.extend(apartments)

    apartment_count = list(map(
        lambda apartment_complexe: len(apartment_complexe),
        apartment_complexes))

    apartment_count.sort()

    return [len(apartment_complexes)] + apartment_count


class TestNumberingApartmentComplexes(unittest.TestCase):
    def test_numbering_apartment_complexes(self):
        for matrix, expected in [
            [
                [
                    [0, 1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0, 1],
                    [1, 1, 1, 0, 1, 0, 1], [0, 0, 0, 0, 1, 1, 1],
                    [0, 1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0],
                    [0, 1, 1, 1, 0, 0, 0]
                ], [3, 7, 8, 9]
            ]
        ]:
            self.assertEqual(expected, numbering_apartment_complexes(matrix))


if __name__ == '__main__':
    unittest.main()
