# -*- coding: utf-8 -*-

if __name__ == '__main__':
    cases = int(input())

    for case in range(cases):
        prisons = int(input())
        result = 0

        for prison in range(1, prisons + 1):
            open = 0

            for num in range(1, prison + 1):
                if prison % num == 0:
                    open += 1

            if open % 2 != 0:
                result += 1

        print(result)
