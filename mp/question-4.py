# -*- coding: utf-8 -*-

""" 문제
정수(int)가 주어지면, 팰린드롬(palindrome)인지 알아내시오. 팰린드롬이란, 앞에서부터 읽으나 뒤에서부터 읽으나 같은 단어를 말합니다. 단, 정수를 문자열로 바꾸면 안됩니다.
"""

""" 예제
Input: 12345
Output: False

Input: -101
Output: False

Input: 11111
Output: True

Input: 12421
Output: True
"""

if __name__ == "__main__":
	input = int(input())
	output = bool()
	
	if input < 0 or (input % 10 == 0 and input != 0):
		output = False
	else:
		reverse = 0

		while input > reverse:
			reverse = reverse * 10 + input % 10
			input = int(input / 10)

		output = True if input == reverse or input == int(reverse / 10) else False
				

	print(output)
