from fruitmand import fruitmand
import random
vraag1 = int(input("Voer een aantal in: "))
for x in range(vraag1):
    fruitnaam = random.choice(fruitmand)['name']
    print(fruitnaam)