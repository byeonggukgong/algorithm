# -*- coding: utf-8 -*-

""" 문제
피보나치 배열은 0과 1로 시작하며, 다음 피보나치 수는 바로 앞의 두 피보나치 수의 합이 된다. 정수 N이 주어지면, N보다 작은 모든 짝수 피보나치 수의 합을 구하여라.
"""

""" 예제
Input: N = 12
Output: 10 // 0, 1, 2, 3, 5, 8 중 짝수인 2 + 8 = 10.
"""

if __name__ == '__main__':
	input = int(input())
	fibonacci = [1, 1]
	even_sum = 0
	
	while(True):
		temp = fibonacci[-2] + fibonacci[-1]
		
		if temp < input:
			if temp % 2 == 0:
				even_sum += temp
				
			fibonacci.append(temp)
		else:
			break
	
	print(even_sum)