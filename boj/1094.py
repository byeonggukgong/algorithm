# -*- coding: utf-8 -*-

if __name__ == '__main__':
	input = int(input())
	stick_size = 64
	sticks = list()
	
	while True:
		stick_sum = sum(sticks)
		
		if input != stick_sum:
			if stick_sum + stick_size <= input:
				sticks.append(stick_size)
				
			stick_size /= 2
		else:
			break

	print(len(sticks))
	