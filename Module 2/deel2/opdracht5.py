import random
kleur = ['rood', 'blauw', 'groen', 'geel', 'bruin']
aantal = int(input("Hoeveel M&M's moeten er toegevoegd worden aan de zak?"))
zak = {}

for i in range(aantal):
    random_kleur = random.choice(kleur)
    if random_kleur in zak:
        zak[random_kleur] += 1

    else:
        zak[random_kleur] = 1

print(zak)