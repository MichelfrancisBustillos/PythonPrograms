__author__ = 'Michelfrancis Bustillos'
import random
import string

def main():
	dataList = []
	movies = eval(input("How many movies would you like to create? "))
	
	with open('dataCreated.csv', 'w') as fout:
		for x in range(movies):
			
			fout.write(id_generator() + "," + str(random.randrange(0, 100)) + "\n")

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))
	
main()