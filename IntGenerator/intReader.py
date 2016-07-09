__author__ = 'Michelfrancis Bustillos'

def main():
	control = 0
	temp = 0
	counter = 0
	
	with open('myInts.txt', 'r') as fread:
		line = int(line.rstrip("\n"))
		counter += 1
		if line <= control:
			temp += 1
	
	centage = temp / counter
	print("Percent: ", str(centage))
main()
