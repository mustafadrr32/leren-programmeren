def fibonacci(n):
    getal, getal2 = 0, 1
    if n <= 0:
        print("Voer een positief getal in")
    elif n == 1:
        print(f"Fibonacci {n}: ")
        print(getal)
    else:
        print("Fibonacci: ")
        for _ in range(n):
            print(getal)
            getal, getal2 = getal2, getal + getal2

def functie():
    vraag = int(input("Voer een getal in: "))
    fibonacci(vraag)


functie()
