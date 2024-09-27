def adding(num1,num2):
    return num1 + num2

def subtracting(num1, num2):
    return num1 - num2

def multiplying(num1, num2):
    return num1 * num2

def dividing(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("The division by zero is not allowed")
    return num1 / num2
