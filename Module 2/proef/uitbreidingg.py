import random
lijst = []
while len(lijst) < 3:
    naam = input("Voer een naam in: ").lower()
    if not naam:
        print("Fout: Je hebt in een van de vragen niks ingevoerd.. probeer het opnieuw: ")
        continue
    if naam in lijst:
            print("Deze naam is dubbel ingevoerd: ")
    else:
        print("Goed")
        lijst.append(naam)


while True:
    naam_vraag = input("Wil je nog een naam invoeren? ").lower()
    if naam_vraag == "ja":
        naam_if = input("Voer een naam in: ").lower()
        if naam_if in lijst:
            print("Deze naam is dubbel ingevoerd: ")
        else:
            print("Goed")
            lijst.append(naam_if)
    elif naam_vraag == "nee":
        print(lijst)
        break
lootjes = lijst.copy()
random.shuffle(lootjes)

while True:
    if any(lootjes[x] == lijst[x] for x in range(len(lijst))):
        random.shuffle(lootjes)
    else:
        break

dict_lootjes = dict(zip(lijst, lootjes))
while True:
    zoek_naam = input("voer je naam in (typ klaar als je klaar bent)").lower()
    if zoek_naam == "klaar":
        break
    if zoek_naam in dict_lootjes:
        print(f"{zoek_naam} heeft lootje {dict_lootjes[zoek_naam]}")

    else: 
        print("zit er niet in")


