getal1 = int(input("voer een getal in"))

if getal1 > 5 and getal1 < 10 :

    print("getal tussen 5-10")

elif getal1 < 4 or getal1 > 10:

    print("Kleiner dan 4 of groter dan 10")
    if getal1 > 10:
        print("groter dan 10")

elif getal1 == 10:
    print("gelijk aan 10")
