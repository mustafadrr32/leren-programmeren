import random

# Verzamelen van namen en cadeautjes
lijst = []
cadeautjes = {}

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
        cadeautjes[naam] = [input(f"Voer cadeau {i+1} in voor {naam}: ") for i in range(3)]

while True:
    naam_vraag = input("Wil je nog een naam invoeren? (ja/nee) ").lower()
    if naam_vraag == "ja":
        naam_if = input("Voer een naam in: ").lower()
        if naam_if in lijst:
            print("Deze naam is dubbel ingevoerd: ")
        else:
            print("Goed")
            lijst.append(naam_if)
            cadeautjes[naam_if] = [input(f"Voer cadeau {i+1} in voor {naam_if}: ") for i in range(3)]
    elif naam_vraag == "nee":
        print(lijst)
        break

# Lootjes schudden en toewijzen
lootjes = lijst.copy()
random.shuffle(lootjes)

while True:
    if any(lootjes[x] == lijst[x] for x in range(len(lijst))):
        random.shuffle(lootjes)
    else:
        break

dict_lootjes = dict(zip(lijst, lootjes))

# Namen en bijbehorende lootjes opvragen
while True:
    zoek_naam = input("Voer je naam in (typ 'klaar' als je klaar bent): ").lower()
    if zoek_naam == "klaar":
        break
    if zoek_naam in dict_lootjes:
        getrokken_naam = dict_lootjes[zoek_naam]
        print(f"{zoek_naam} heeft lootje {getrokken_naam}")
        print(f"Cadeautjes voor {getrokken_naam}: {', '.join(cadeautjes[getrokken_naam])}")
    else:
        print("Naam zit er niet in")
