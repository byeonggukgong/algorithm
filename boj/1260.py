# -*- coding: utf-8 -*-

import unittest

def bfs(start: int, matrix: list) -> list:
    queue = [start]
    visited = [start]

    while queue:
        print(queue)
        current = queue.pop(0)

        for vertex, linked in enumerate(matrix[current - 1], 1):
            if linked and not vertex in visited:
                queue.append(vertex)
                visited.append(vertex)

    return visited

def dfs(start: int, matrix: list) -> list:
    stack = [start]
    visited = [start]

    while stack:
        current = stack[-1]
        visitable = False

        print(stack, visitable)

        for vertex, linked in enumerate(matrix[current - 1], 1):
            if linked and not vertex in visited:
                stack.append(vertex)
                visited.append(vertex)
                visitable = True

                break

        if not visitable:
            stack.pop()

    return visited

def dfs_and_bfs(info: list, edges: list) -> list:
    vertex_count = info[0]
    start = info[2]

    matrix = [[0 for _ in range(vertex_count)] for _ in range(vertex_count)]

    for edge in edges:
        matrix[edge[0] - 1][edge[1] - 1] = 1
        matrix[edge[1] - 1][edge[0] - 1] = 1

    return [dfs(start, matrix), bfs(start, matrix)]


class TestDfsAndBfs(unittest.TestCase):
    def test_dfs_and_bfs(self):
        for info, lines, expected in [
            [
                [ 4, 5, 1 ], [[1, 2], [1, 3], [1, 4], [2, 4], [3, 4]],
                [[1, 2, 4, 3], [1, 2, 3, 4]]
            ],
            [
                [ 4, 5, 2 ], [[1, 2], [1, 3], [1, 4], [2, 4], [3, 4]],
                [[2, 1, 3, 4], [2, 1, 4, 3]]
            ]
        ]:
            self.assertEqual(expected, dfs_and_bfs(info, lines))

if __name__ == '__main__':
    unittest.main()
