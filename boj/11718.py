# -*- coding: utf-8 -*-

if __name__ == '__main__':
	while True:
		try:
			line = input()
			
			if not line:
				break
		
			print(line)
		except EOFError:
			break
