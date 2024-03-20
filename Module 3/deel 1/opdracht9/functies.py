def functie():
    naam = input("Wat is je naam? ")
    leeftijd = input("Wat is je leeftijd? ")
    woonplaats = input("Wat is je woonplaats? ")
    return {'name': naam, 'age': leeftijd, 'city': woonplaats}

def functie2():
    gegevens = []
    while True:
        invoer = input("Toets enter om door te gaan of stop om te printen: ")
        if invoer.lower() == 'stop':
            break
        gegevens.append(functie())
    return gegevens