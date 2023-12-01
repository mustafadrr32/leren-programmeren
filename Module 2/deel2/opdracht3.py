import random
tuple = ['oranje', 'blauw', 'groen', 'bruin']
vraag = int(input("Hoeveel m&m's moet er toegevoegd worden?"))

x = [random.choice(tuple) for i in range(vraag)]

print(f"Aantal in de zak : {x}")

