from logics import *


def calculatorWindow():
    print("What operation would you like to perform?")
    print("1. Addition!")
    print("2. Subtraction!")
    print("3. Multiplication!")
    print("4. Division")
    print("5. Exit")
    chosenOperation = int(input("Enter the corresponding number of your choice!\n"))
    return chosenOperation


while True:
    choice = calculatorWindow()
    if choice == 1:
        addition()
    elif choice == 2:
        subtraction()
    elif choice == 3:
        multiplication()
    elif choice == 4:
        division()
    elif choice == 5:
        print("Thank you for using this calculator!")
        break
    else:
        print("You have given an invalid input program is now closing!")
