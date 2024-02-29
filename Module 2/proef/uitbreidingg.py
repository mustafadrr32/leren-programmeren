import random
lijst = []
while len(lijst) < 3:
    naam = input("Voer een naam in: ")
    if not naam:
        print("Fout: Je hebt in een van de vragen niks ingevoerd.. probeer het opnieuw: ")
        continue
    lijst.append(naam)


while True:
    naam_vraag = input("Wil je nog een naam invoeren? ").lower()
    if naam_vraag == "ja":
        naam_if = input("Voer een naam in: ")
        if naam_if in lijst:
            print("Deze naam is dubbel ingevoerd: ")
        else:
            print("Goed")
            lijst.append(naam_if)
    elif naam_vraag == "nee":
        print(lijst)
        break


