#!/usr/bin/env python3

import sys

from itertools import groupby
from operator import itemgetter

SEP = "\t"

class Reducer(object):

	def __init__(self, infile=sys.stdin, separator=SEP):
		self.infile = infile
		self.sep = separator

	def emit(self, key, value):
		sys.stdout.write(f"*"*20+f"\nDestino mais visado:\n"+f"{key}{self.sep}{value}\n"+f"*"*20+"\n")

	def reduce(self):
		dict_destinos = {}
		for current, group in groupby(self, itemgetter(0)):
			count = 0
			for destinos in group:
				count += 1
			dict_destinos[current] = count
			
		mais_visado = max(dict_destinos, key = dict_destinos.get)
		self.emit(mais_visado, dict_destinos[mais_visado])

	def __iter__(self):
		for line in self.infile:
			try:
				parts = line.split(self.sep)
				yield parts[0], float(parts[1])
			except:
				continue

if __name__ == '__main__':
	reducer = Reducer(sys.stdin)
	reducer.reduce()
