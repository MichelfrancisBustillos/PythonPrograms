__author__ = 'Michelfrancis Bustillos'
import random

def main():
	throws = 0
	greenHits = 0
	purpleHits = 0
	redHits = 0
	blueHits = 0
	global fin

	with open('results.csv') as fin:
		for line in fin:
			data = line.split(',')
			if len(data) == 3:
				throws+= 1
				result = data[2]
				if result == "1\n":
					greenHits += 1
				elif result == "2\n":
					purpleHits += 1
				elif result == "3\n":
					redHits += 1
				elif result == "4\n":
					blueHits += 1

	calcer("Green", greenHits, throws)
	calcer("Purple", purpleHits, throws)
	calcer("Red", redHits, throws)
	calcer("Blue", blueHits, throws)

def calcer(color, hits, throws):
	centage = (hits * 100) / throws 
	print(color + ":")
	print ("There were", str(hits), "hits.")
	print("That is a", str(centage), "% success rate.") 
	print()

main()