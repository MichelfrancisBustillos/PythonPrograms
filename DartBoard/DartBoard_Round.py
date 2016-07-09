__author__ = 'Michelfrancis Bustillos'
import random

def main():
	global greenRadius
	global purpleRadius
	global redRadius
	greenRadius = 1
	purpleRadius = 2
	redRadius = 3
	greenHits = 0
	purpleHits = 0
	redHits = 0
	missHits = 0
	
	throws = eval(input("How many darts would you like to throw? "))
	global fout
	
	with open('results.csv', 'w') as fout:
		for x in range(throws):
			result = throw()
			fout.write(str(result) + "\n")
			if result == 1:
				greenHits += 1
			elif result == 2:
				purpleHits += 1
			elif result == 3:
				redHits += 1
			else:
				missHits += 1
			
	calcer("Green", greenHits, throws)
	calcer("Purple", purpleHits, throws)
	calcer("Red", redHits, throws)
	calcer("Miss", missHits, throws)
	
def throw():
	x = random.randrange(0,4)
	y = random.randrange(0,4)
	printString = str(x) + ',' + str(y) + ','
	fout.write(printString)
	if ((x - 0) * (x - 0)) + ((y - 0) * (y - 0)) < (greenRadius * greenRadius): #inner
		return 1
	elif ((x - 0) * (x - 0)) + ((y - 0) * (y - 0)) < (purpleRadius * purpleRadius): #middle
		return 2
	elif ((x - 0) * (x - 0)) + ((y - 0) * (y - 0)) < (redRadius * redRadius): #extreme
		return 3
	return 0
	
def calcer(color, hits, throws):
	centage = (hits * 100) / throws 
	print(color + ":")
	print ("There were", str(hits), "hits.")
	print("That is a", str(centage), "% success rate.") 
	print()

main()