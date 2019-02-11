# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    cnt = int(sys.stdin.readline().rstrip())

    for _ in range(cnt):
        nums = sys.stdin.readline().rstrip().split()
        sys.stdout.write(str(int(nums[0]) + int(nums[1])) + '\n')
