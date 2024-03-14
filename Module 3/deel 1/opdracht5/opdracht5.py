def functie():
    naam = input("naam? ")
    leeftijd = input("leeftijd? ")
    return {'name': naam, 'age': leeftijd}

resultaat = functie()
print(f"Naam: {resultaat['name']}")
print(f"Leeftijd: {resultaat['age']}")