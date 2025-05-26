def addition():
    x = int(input("Enter a value for the first digit: "))
    y = int(input("Enter a value for the second digit: "))
    print("The sum of the values you entered is : " + str(x + y))


def subtraction():
    x = int(input("Enter a value for the first digit: "))
    y = int(input("Enter a value for the second digit: "))
    print("The difference of the values you entered is : " + str(x - y))


def doRecursMultiplication(x, y):
    totalScore = 0
    if y != 1:
        totalScore += doRecursMultiplication(x, y - 1)
    return totalScore + x


def multiplication():
    x = int(input("Enter a value for the multiplicand: "))
    y = int(input("Enter a value for the multiplier: "))
    if x and y < 0:
        product = doRecursMultiplication(x, y)
    else:
        product = 0
    print("The product of your 2 value is: " + str(product))


def doRecursDivision(x, y):
    global remainder
    toReturn = 0
    if x > y:
        toReturn += doRecursDivision(x - y, y)
    # if x != 0:
    #     remainder = x
    return toReturn + 1


def division():
    x = int(input("enter a value for dividend : "))
    y = int(input("enter a value for divisor : "))
    quotient = doRecursDivision(x, y)
    print("The quotient of your 2 value is: " + str(quotient))
