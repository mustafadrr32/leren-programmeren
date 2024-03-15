from functies import *

gegevenslijst = functie2()
for resultaat in gegevenslijst:
    print(f"Naam: {resultaat['name']}")
    print(f"Leeftijd: {resultaat['age']}")
    print(f"Woonplaats: {resultaat['city']}")
