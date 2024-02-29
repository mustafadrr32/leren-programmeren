import random

mensen = []

print('Je gaat min. 3 namen invoeren. ')
while True:
    naam = input("Voer de naam of typ klaar als je klaar bent: ").lower()
    if naam == "klaar":
        break
    if naam:
        if naam not in mensen:
            mensen.append(naam)
        else:
            print("Voer een andere naam. Dit is al ingevoerd. ")
    else:
        print("Voer een naam! ")

if len(mensen) < 3:
    print("Niet genoeg mensen.. Einde")
else:
    lootjes = mensen.copy()
    random.shuffle(lootjes)
    while any(deelnemer == lootje for deelnemer, lootje in zip(mensen, lootjes)):
        random.shuffle(lootjes)
    print("Lootjes:")
    for deelnemer, lootje in zip(mensen, lootjes):
        print(f"{deelnemer}: {lootje}")