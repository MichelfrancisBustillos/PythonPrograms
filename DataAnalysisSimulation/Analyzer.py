__author__ = 'Michelfrancis Bustillos'
import random

def main():
	original = ana('data.csv', 50)
	sims = ana('dataCreated.csv', original)
	print(str(original) + "% of movies have a rating of 50% or lower in orginal data.")
	print(str(sims) + "% of movies have a rating of 50% or lower in created data.")

def ana(fileName, cent):
	dataList = []
	counter = 0
	
	with open(fileName) as fin:
		for line in fin:
			data = line.split(',')
			data[1] = data[1].rstrip('\n')
			dataList.append(data)
			if data[1].isdigit():
				if  int(data[1]) <= float(cent):
					counter += 1
	
	longy = len(dataList)
		
	centage = (counter * 100) / longy
		
	return "{0:.2f}".format(round(centage,2))
main()