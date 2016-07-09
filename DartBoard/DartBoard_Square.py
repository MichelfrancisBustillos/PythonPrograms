__author__ = 'Michelfrancis Bustillos'
import random

def main():
	global INNER_X_MIN
	global INNER_Y_MIN
	global INNER_X_MAX
	global INNER_Y_MAX
	global MIDDLER_X_MIN
	global MIDDLER_Y_MIN
	global MIDDLER_X_MAX
	global MIDDLER_Y_MAX
	global EXOR_X_MIN
	global EXOR_Y_MIN
	global EXOR_X_MAX
	global EXOR_Y_MAX
	global EXTREMER_X_MIN
	global EXTREMER_Y_MIN
	global EXTREMER_X_MAX
	global EXTREMER_Y_MAX
	INNER_X_MIN = 0.375
	INNER_Y_MIN = 0.375
	INNER_X_MAX = 0.625
	INNER_Y_MAX = 0.625
	MIDDLER_X_MIN = 0.25
	MIDDLER_Y_MIN = 0.25
	MIDDLER_X_MAX = 0.75
	MIDDLER_Y_MAX = 0.625
	EXOR_X_MIN = 0.125
	EXOR_Y_MIN = 0.125
	EXOR_X_MAX = 0.875
	EXOR_Y_MAX = 0.875
	EXTREMER_X_MIN = 0
	EXTREMER_Y_MIN = 0
	EXTREMER_X_MAX = 1
	EXTREMER_Y_MAX = 1
	
	greenHits = 0
	purpleHits = 0
	redHits = 0
	blueHits = 0
	
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
			elif result == 4:
				blueHits += 1
			
	calcer("Green", greenHits, throws)
	calcer("Purple", purpleHits, throws)
	calcer("Red", redHits, throws)
	calcer("Blue", blueHits, throws)
	
def throw():
	x = random.random()
	y = random.random()
	printString = str(x) + ',' + str(y) + ','
	fout.write(printString)
	if INNER_X_MIN <= x <= INNER_X_MAX and INNER_Y_MIN <= y <= INNER_Y_MAX: #inner
		return 1
	elif MIDDLER_X_MIN <= x <= MIDDLER_X_MAX and MIDDLER_Y_MIN <= y <= MIDDLER_Y_MAX: #middle
		return 2
	elif EXOR_X_MIN <= x <= EXOR_X_MAX and EXOR_Y_MIN <= y <= EXOR_Y_MAX: #extreme
		return 3
	elif EXTREMER_X_MIN <= x <= EXTREMER_X_MAX and EXTREMER_Y_MIN <= y <= EXTREMER_Y_MAX: #evenMoreExtreme
		return 4
	return 0
	
def calcer(color, hits, throws):
	centage = (hits * 100) / throws 
	print(color + ":")
	print ("There were", str(hits), "hits.")
	print("That is a", str(centage), "% success rate.") 
	print()

main()