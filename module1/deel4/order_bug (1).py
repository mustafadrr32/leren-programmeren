def vraag_getal(aantal):
    antwoord = input("Voer het "+ getal +" getal in: ")
    getal = int(aantal)
    return getal


getal_1 = int(input("eerste"))
getal_2 = int(input("tweede"))

def deel_getallen(a, b):
    antwoord = a / b
    return antwoord
    


if getal_2 == 0:
    print("Kan niet delen door 0")
else:
    resultaat = deel_getallen(getal_1, getal_2)
    print ("{} gedeeld door {} is gelijk aan {}".format(getal_1, getal_2, resultaat))
    

