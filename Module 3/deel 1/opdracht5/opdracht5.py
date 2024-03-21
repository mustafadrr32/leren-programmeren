def NaamLeeftijd() -> dict:
    naam = input("naam? ")
    leeftijd = input("leeftijd? ")
    return {'name': naam, 'age': leeftijd}

resultaat = NaamLeeftijd()
print(f"Naam: {resultaat['name']}")
print(f"Leeftijd: {resultaat['age']}")