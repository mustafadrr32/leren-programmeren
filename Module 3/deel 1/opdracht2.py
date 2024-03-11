from collections import Counter
import math, random

def aantalGetallenInList(getallen:list) -> int:
    
    return len(getallen)

def SomGetallenInList(getallen:list) -> int:
    
    return sum(getallen)

def GemiddeldeBerekenen(getallen:list) -> int:
    return sum(getallen) / len(getallen)

def GrootsteGetal(getallen:list) -> int:
    return max(getallen)

def KleinsteGetallen(getallen:list) -> int:
    return min(getallen)

def EersteGetal(getallen:list) -> int:
    return getallen[0]

def Delen1(getallen:list, controlegetal1:list) -> int:
    return min(getallen) / (controlegetal1)

def Delen2(getallen:list, controlegetal2:list) -> int:
    return max(getallen) / (controlegetal2)

def UniekeGetallen(getallen:list) -> int:
    return list(set(getallen))

def UniekeElementen(getallen:list) -> int:
    return len(list(set(getallen)))

def Verschil(getallen:list, controlegetal1:list) -> int:
    return abs(len(list(set(getallen)))) - (controlegetal1)

def GesorteerdeLijst(getallen:list) -> int:
    return sorted(getallen)

def GesorteerdeLijstUniek(getallen:list) -> int:
    return sorted(list(set(getallen)))

def TelUniekeElementen(getallen:list) -> int:
    telling_elementen = {}
    for getal in getallen:
        aantalkeer = telling_elementen[getal]+1 if getal in telling_elementen else 1
        telling_elementen[getal] = aantalkeer
    return telling_elementen

def Deelbaar(getallen:list, controlegetal1:list, unieke_getallen) -> int:
    deelbaar1 = []
    for getal in unieke_getallen:
        if getal % controlegetal1 == 0:
            deelbaar1.append(getal)
    deelbaar1 = sorted(deelbaar1)
    return unieke_getallen

def Deelbaar2(getallen:list, controlegetal2:list, unieke_getallen) -> int:
    deelbaar2 = []
    for getal in unieke_getallen:
        if getal % controlegetal2 == 0:
            deelbaar2.append(getal)
    deelbaar2 = sorted(deelbaar2)
    return unieke_getallen

def KomtVoor(getallen:list, controlegetal1:list, controlegetal2:list) -> int:
    controlegetal1 in getallen and controlegetal2 in getallen
    return controlegetal1

def Posities(getallen:list, controlegetal1:list) -> int:
    posities = []
    for index, num in enumerate(getallen):
        if num == controlegetal1:
            posities.append(index)
    return posities

def Shuffle(getallen):
    random.shuffle(getallen)

def Verschil2(random_getal, controlegetal2) -> int:
    return abs(random_getal - controlegetal2)

def Staf(getallen:list, aantal, gemiddelde) -> int:
    verschil_kwadraat = sum((x - gemiddelde) ** 2 for x in getallen)
    variantie = verschil_kwadraat / aantal
    standaardafwijking = math.sqrt(variantie)
    return standaardafwijking