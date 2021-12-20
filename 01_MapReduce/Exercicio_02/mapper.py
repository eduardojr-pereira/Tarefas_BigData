#!/usr/bin/env python3

import csv
import sys

SEP = "\t"

class Mapper(object):

	def __init__(self, infile=sys.stdin, separator=SEP):
		self.infile = infile
		self.sep = separator

	def emit(self, key, value):
		sys.stdout.write(f"{key}{self.sep}{value}")

	def map(self):
		for line in self:
			current_line = 1
			words = []
			for word in line:
				word = ''.join(x for x in word if x.isalnum()).lower()
				if word not in words:
					words.append(word)
					self.emit(word, current_line)
					current_line +=1
				

	def __iter__(self):
		for line in self.infile:
			yield line.split(self.sep, 1)


if __name__ == '__main__':
 	mapper = Mapper()
 	mapper.map()
