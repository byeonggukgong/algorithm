# -*- coding: utf-8 -*-

""" 문제
정수 n이 주어지면, n개의 여는 괄호 "("와 n개의 닫는 괄호 ")"로 만들 수 있는 괄호 조합을 모두 구하시오. (시간 복잡도 제한 없습니다).
"""

""" 예제
Input: 1
Output: ["()"]

Input: 2
Output: ["(())", "()()"]

Input: 3
Output: ["((()))", "(()())", "()(())", "(())()", "()()()"]
"""

def recurse(output, shape, open, close):
	if open == 0 and close == 0:
		output.append(shape)
		return
	
	if open > 0:
		recurse(output, shape + '(', open - 1, close)

	if open < close:
		recurse(output, shape + ')', open, close - 1)

if __name__ == "__main__":
	input = int(input())
	output = list()
	
	recurse(output, str(), input, input)
	
	print(output)
