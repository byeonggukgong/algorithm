# -*- coding: utf-8 -*-

if __name__ == "__main__":
	row, col = [int(num) for num in input().split()]
	dp = [[0 for x in range(col)] for y in range(row)]
	
	for x in range(row):
		for y in range(col):
			if x == 0 and y > 0:
				dp[x][y] = dp[x][y - 1] + 1
			if y == 0 and x > 0:
				dp[x][y] = dp[x - 1][y] + 1
			if x > 0 and y > 0:
				dp[x][y] = min(dp[x][y - 1] + x + 1, dp[x - 1][y] + y + 1)
				
	print(dp[row - 1][col - 1])