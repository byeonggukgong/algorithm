# -*- coding: utf-8 -*-

if __name__ == '__main__':
	sentence = input()
	
	words = [word for word in sentence.split(' ') if not word == '']
	count = len(words)
	
	print(count)
