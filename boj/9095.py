# -*- coding: utf-8 -*-

def recursive(num):
	if num >= 0:
		if num == 0:
			return 1
		if num > 0:
			return recursive(num - 3) + recursive(num - 2) + recursive(num - 1)
	else:
		return 0
	
if __name__ == "__main__":
	for idx in range(int(input())):
		print(recursive(int(input())))