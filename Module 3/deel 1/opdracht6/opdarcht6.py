def functie1():
    naam = input("Wat is je naam? ")
    leeftijd = input("Wat is je leeftijd? ")
    return {'name': naam, 'age': leeftijd}

def functie2():
    gegevens = []
    while True:
        invoer = input("Toets enter om door te gaan of stop om te printen: ")
        if invoer.lower() == 'stop':
            break
        gegevens.append(functie1())
    return gegevens

gegevenslijst = functie2()
for resultaat in gegevenslijst:
    print(f"Naam: {resultaat['name']}")
    print(f"Leeftijd: {resultaat['age']}")
