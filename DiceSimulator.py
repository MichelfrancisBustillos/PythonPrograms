__author__ = 'Michelfrancis Bustillos'

import random
import os

def main():
    dice = eval(input("How many dice? "))
    rolls = eval(input("How many rolls? "))
    sides = eval(input("How many sides per die? "))
    total = 0
    l = []
    os.system('cls')

    for c in range(rolls):
        number = roll(sides,dice)
        l.append(number)

    fout = open("results.csv", "w")
    for x in range(len(l)):
        fout.write("%s\n" % str(l[x]))
    fout.close()
    
    choice = eval(input("Print roll results(1) or result counts(2)? "))
    if choice == 1:
        for c in range(len(l)):
            print("Roll", str(c + 1), ":", l[c])
    elif choice == 2:
        for c in range(sides, (sides*dice)):
            print(str(c) +"'s:", str(l.count(c)))
    else:
        print("Error!! Invalid choice.")

def roll(sides, dice):
    total = 0
    for x in range(dice):
        total = total + random.randint(1, sides)
    return total

main()
