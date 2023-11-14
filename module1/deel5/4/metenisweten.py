def vergelijk_getallen(getal1: int, getal2: int) -> str:
    if getal1 == getal2:
        return "even groot"
    elif getal1 > getal2:
        return f"Maximum: {getal1} en minimum: {getal2}"
    else:
        return f"Maximum: {getal2} en minimum: {getal1}"

a = int(input("Voer een heel getal in voor a: "))
b = int(input("Voer een heel getal in voor b: "))
resultaat = vergelijk_getallen(a, b)
print(resultaat)
