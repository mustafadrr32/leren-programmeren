from collections import Counter
import math, random
from opdracht2 import *

def analyseer_getallenlijst(getallen:list, controlegetal1:int, controlegetal2:int) -> dict:
    if not getallen:
        return {"Lijst is leeg, voer getallen in.":getallen}

    if not str(controlegetal1).isnumeric():
        return {"Eerste controlle getal incorrect.":controlegetal1}

    if not str(controlegetal2).isnumeric():
        return {"Tweede controlle getal incorrect.":controlegetal2}

    # Gemiddelde berekenen GEDAAN
    aantal = aantalGetallenInList(getallen)

    # Som van alle getallen in de lijst GEDAAN
    som = SomGetallenInList(getallen)

    # Gemiddelde berekenen GEDAAN
    gemiddelde = GemiddeldeBerekenen(getallen)

    # Het grootste getal in de lijst GEDAAN
    grootste_getal = GrootsteGetal(getallen)
    
    # Het kleinste getal in de lijst GEDAAN
    kleinste_getal = KleinsteGetallen(getallen)
    
    # Het eerste getal in de lijst GEDAAN
    eerste_getal = EersteGetal(getallen)
    
    # Het kleinste getal gedeeld door het eerste controle getal GEDAAN
    delen1 = Delen1(getallen, controlegetal1)

    # Het grootste getal gedeeld door het tweede controle getal
    delen2 = Delen2(getallen, controlegetal2)

    # alle unieke getallen
    unieke_getallen = UniekeGetallen(getallen)

    # Aantal unieke elementen in de lijst
    aantal_unieke_elementen = UniekeElementen(getallen)

    # Verschil tussen aantal unieke elementen en eerste controle getal
    verschil1 = Verschil(getallen, controlegetal1)
    
    # Sorteer de lijst van getallen
    gesorteerde_lijst = GesorteerdeLijst(getallen)

    # Sorteer de lijst van unieke getallen
    gesorteerde_lijst_uniek = GesorteerdeLijstUniek(getallen)

    # Tel het aantal keren dat elk uniek element voorkomt in de lijst
    
    telling_elementen = TelUniekeElementen(getallen)

    # Getallen die deelbaar zijn door het eerste controlle getal
    deelbaar1 = Deelbaar(getallen, controlegetal1, unieke_getallen)

    # Getallen die deelbaar zijn door het tweede controlle getal
    deelbaar2 = Deelbaar2(getallen, controlegetal2, unieke_getallen)

    # Controleer of een bepaald getallen in de lijst voorkomen
    komtvoor = KomtVoor(getallen, controlegetal1, controlegetal2)

    # Vindt de posities van heteerste controle getal
    posities = Posities(getallen, controlegetal1)

    # Standaardafwijking berekenen
    standaardafwijking = Staf(getallen, aantal, gemiddelde)

    # Shuffle de lijst
    shuffle = Shuffle(getallen)

    # Pak een random getal uit de lijst
    random_getal = getallen[random.randint(0,aantal-1)]

    # Verschil tussen twee getallen
    verschil2 = Verschil2(random_getal, controlegetal2)

    resultaten = {
        "Aantal getallen": aantal,
        "Gemiddelde": gemiddelde,
        "Som": som,
        "Grootste getal": grootste_getal,
        "Kleinste getal": kleinste_getal,
        "Eerste getal": eerste_getal,
        f"{kleinste_getal} / {controlegetal1}": delen1,
        f"{grootste_getal} / {controlegetal2}": delen2,
        "Aantal unieke elementen": aantal_unieke_elementen,
        f"Het verschil tussen {aantal_unieke_elementen} & {controlegetal1}": verschil1,
        "Gesorteerde lijst getallen": gesorteerde_lijst,
        "Gesorteerde lijst unieke getallen": gesorteerde_lijst_uniek,
        "Telling van elementen": telling_elementen,
        f"Deelbaar door {controlegetal1} (op volgorde)": deelbaar1,
        f"Deelbaar door {controlegetal2} (op volgorde)": deelbaar2,
        f"{controlegetal1} & {controlegetal2} komt wel voor in de lijst": komtvoor,
        f"{controlegetal1} komt voor op positie(s)": posities,
        "Standaardafwijking": standaardafwijking,
        "Geshufflede lijst": getallen,
        "Willekeurige getal uit de lijst": random_getal,
        f"Het verschil tussen {random_getal} & {controlegetal2}": verschil2,
    }

    return resultaten


# Voorbeeld van het gebruik van de functie:
getallenlijst = [16, 2, 5, 8, 12, 3, 9, 16, 5, 8, 64, 33]
controlegetal1 = 8
controlegetal2 = 3
analyse_resultaat = analyseer_getallenlijst(getallenlijst, controlegetal1, controlegetal2)
print("Analyse resultaten:")
for key, value in analyse_resultaat.items():
    print(f"{key}: {value}")