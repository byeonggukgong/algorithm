# -*- coding: utf-8 -*-

if __name__ == '__main__':
    case = int(input())

    for x in range(case):
        output = [float(num) for num in input().split()]
        average = sum(output[1:]) / float(output[0])
        count = sum(1 for num in output[1:] if float(num) > float(average))
        percent = round(count / output[0] * 100, 3)

        print("{:0.3f}%".format(percent))
