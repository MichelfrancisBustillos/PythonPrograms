__author__ = 'Michelfrancis Bustillos'

import random

def main():
	ints = 500
	
	with open('myInts.txt', 'w') as fwrite:
		for x in range(ints):
			fwrite.write(str(random.randint(1, 100)) + "\n")

main()
