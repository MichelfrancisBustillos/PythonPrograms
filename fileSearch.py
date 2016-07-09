__author__ = 'AstridH20'
#Student Name: Michelfrancis Bustillos
#Class Section/Period: B1
#Date: 4/13/2016
#File Name: mySearchCode.py
#This program is designed to implement a search algorithm

import os.path
def main():
	done = False
	while not done:
		print("Hello! Welcome to my search program!")
		myList = GetFileContents()
		myNumber = int(GetValidNumber())
		
		choice = eval(input("Enter (1) for linear search or (2) for binary search. "))
		if choice == 1:
			yourList = linearSearch(myList, myNumber)
		else:
			yourList = binarySearch(myList, myNumber)

		found = yourList[0]
		numLooks = yourList[1]

		if found == True:
			print("The number ",myNumber , " was found after " , numLooks , "items were searched.")
		else:
			print("The number ", myNumber," was not found. The list was looked at ", numLooks , " times.")

		nextChoice = input("Input 1 to search again. Input anything else to quit the program. ")
		if nextChoice == '1' or (nextChoice.isnumeric() and nextChoice == 1):
			print("Closing current file.")
		else:
			print("Bye!")
			done = True

def GetFileContents():
	fileName = input("What is the name of your file? ")
	good = False
	listOfStuff = []
	while not good:#Keep asking until a valid file is given
		if(os.path.exists(fileName)):#Check if the file name given is valid
			file = open(fileName,"r")#Open the file
			for i in file:#Read through each line in the file
				i = i.rstrip('\n')
				if(i.isnumeric()):#This program only works with numbers
					listOfStuff.append(int(i))
			file.close()#Remember to always close your files!
			return listOfStuff#Return the list of everything inside the file
		else:
			fileName = input("Invalid File. Please try again.\nWhat is the name of your file? ")

def GetValidNumber():
	good = False
	myNumber = input("What number would you like to find? ")
	while not myNumber.isnumeric():
		print("That is not a number!")
		myNumber = input("What number would you like to find? ")
		
	return myNumber

def linearSearch(myList, myNumber):
	found = False
	numLooks = 0
	yourList = []
	
	for x in range(len(myList)):
		numLooks+=1
		if myList[x] == myNumber:
			found = True
			break
	
	#try:
	#	numLooks = myList.index(myNumber) + 1
	#	found = True
	#except ValueError:
	#	numLooks = len(myList)
	yourList.append(found)
	yourList.append(numLooks)
	return yourList
	
def binarySearch(myList, myNumber):
	#myList.sort()
	hi = len(myList)
	mid = 0
	low = 0
	found = False
	numLooks = 0
	yourList = []
	myNumber = int(myNumber)
	
	while low <= hi and not found:
		numLooks+=1
		mid = (hi + low) // 2
		if myList[mid] == myNumber:
			found = True
		elif myList[mid] > myNumber:
			hi = mid - 1
		else:
			low = mid + 1
	
	yourList.append(found)
	yourList.append(numLooks)
	return yourList
	
main()