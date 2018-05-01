# -*- coding: utf-8 -*-

if __name__ == '__main__':
	while True:
		try:
			line = input()
			print(line)
		except EOFError:
			break
