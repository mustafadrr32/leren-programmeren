from fruitmand import fruitmand
import random


while True:
    try:
        vraag1 = int(input("Voer een aantal in: "))
        break
    except:
        print("Voer aub een hele getal in.. ")

for x in range(vraag1):
    fruitnaam = random.choice(fruitmand)['name']
    print(fruitnaam)
