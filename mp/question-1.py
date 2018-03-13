# -*- coding: utf-8 -*-

""" 문제
정수 배열(int array)가 주어지면 가장 큰 이어지는 원소들의 합을 구하시오. 단, 시간복잡도는 O(n).
"""

""" 예제
Input: [-1, 3, -1, 5]
Output: 7 // 3 + (-1) + 5

Input: [-5, -3, -1]
Output: -1 // -1

Input: [2, 4, -2, -3, 8]
Output: 9 // 2 + 4 + (-2) + (-3) + 8
"""

if __name__ == "__main__":
	input = [int(num) for num in input().split()]
	current_sum = input[0]
	max_sum = input[0]
	
	for num in input[1:]:
		current_sum = max(current_sum + num, num)
		max_sum = max(current_sum, max_sum)
			
	print(max_sum)