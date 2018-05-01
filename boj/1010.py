# -*- coding: utf-8 -*-

if __name__ == '__main__':
	case = int(input())
	
	for num in range(case):
		west_site, east_site = [int(num) for num in input().split()]
		dp = [[0 for x in range(east_site)] for y in range(west_site)]
		
		for row in range(west_site):
			for col in range(east_site):
				if row <= col:
					if row == 0:
						dp[row][col] = (row + 1) * (col + 1)
					else:
						dp[row][col] = dp[row][col - 1] + dp[row - 1][col - 1]
		
		print(dp[west_site - 1][east_site - 1])
