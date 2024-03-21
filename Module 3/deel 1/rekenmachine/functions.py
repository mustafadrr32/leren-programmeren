import sys

def exit_program():
    print("Exiting the program...")
    sys.exit(0)



def addition(number1, number2) -> float:
    return number1 + number2

def subtraction(number1, number2)-> float:
    return number1 - number2

def multiplication(number1, number2)-> float:
    return number1 * number2

def division(number1, number2)-> float:
    if number2 == 0:
        print("kan niet delen door 0")
        exit_program()
    else:
        return number1 / number2

def addition1(number1, number2)-> float:
    number2 = 1
    return number1 + number2

def subtraction1(number1, number2)-> float:
    number2 = 1
    return number1 - number2

def multiplication1(number1, number2)-> float:
    number2 = 2
    return number1 * number2

def division1 (number1, number2)-> float:
    number2 = 2
    return number1 / number2

def getInt(beschrijving:str) -> int:
    
    while True:
        try :
            return int(input(beschrijving))      
        except ValueError:
            print("foutmelding je moet een getal invoeren: ")
