def increment(number):
    return number + 1

def decrement(number):
    return number - 1

def add(number1, number2):
    return number1 + number2

def substract(number1, number2):
    return number1 - number2

def multiply(number1, number2):
    return number1 * number2

def divide(number1, number2):
    try:
        result = number1 / number2
        return result
    except ZeroDivisionError:
        return None
