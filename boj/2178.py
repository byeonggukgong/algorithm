# -*- coding: utf-8 -*-

import unittest


def bfs(x: int, y: int, maze: list):
    queue = [(0, 0)]
    visited = [(0, 0)]
    minimum = [[0 for _ in range(y)] for _ in range(x)]

    minimum[0][0] = 1

    while queue:
        row, col = queue.pop(0)

        for r, c in list(zip([-1, 0, 1, 0], [0, 1, 0, -1])):
            square = (row + r, col + c)

            if 0 <= square[0] < x and 0 <= square[1] < y:
                existed = maze[square[0]][square[1]]

                if existed and not square in visited:
                    queue.append((square[0], square[1]))
                    visited.append((square[0], square[1]))
                    minimum[square[0]][square[1]] = minimum[row][col] + 1

    return minimum

def explore_maze(x: int, y: int, maze: list):
    minimum = bfs(x, y, maze)

    return minimum[x - 1][y - 1]

class TestExploreMaze(unittest.TestCase):
    def test_explore_maze(self):
        for x, y, maze, expected in [
            [4, 6, [
                [1, 0, 1, 1, 1, 1],
                [1, 0, 1, 0, 1, 0],
                [1, 0, 1, 0, 1, 1],
                [1, 1, 1, 0, 1, 1]], 15],
            [4, 6, [
                [1, 1, 0, 1, 1, 0],
                [1, 1, 0, 1, 1, 0],
                [1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 0, 1]], 9],
            [2, 25, [
                [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0,
                 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
                [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1,
                 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1]], 38],
            [7, 7, [
                [1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1]], 13]
        ]:
            self.assertEqual(expected, explore_maze(x, y, maze))

if __name__ == '__main__':
    unittest.main()
