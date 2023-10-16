# MUSTAFA DURUR OPDRACHT PIZZACALCULATOR


try:
    print("Keuze uit: Small, Medium, Large")
    print("Small: 7,99 euro")
    print("Medium: 9,99 euro")
    print("Large: 11,99 euro")

    smallprijs = 7.99
    mediumprijs = 9.99
    largeprijs = 11.99

    smallpizza = int(input("Hoeveel small pizza's?"))
    mediumpizza = int(input("Hoeveel medium pizza's?"))
    largepizza = int(input("Hoeveel large pizza's?"))

    aantalpizzas = smallpizza + mediumpizza + largepizza
    smalltotaal = smallprijs * smallpizza
    mediumtotaal = mediumprijs * mediumpizza
    largetotaal = largeprijs * largepizza

    print("                                          ")
    print("-----------------------------------------")
    print("                                          ")
    print("                                          ")
    print(f"Aantal bestelde pizza's: {aantalpizzas}")
    print(f"Aantal small pizza's: {smallpizza}")
    print(f"Aantal medium pizza's: {mediumpizza}")
    print(f"Aantal large pizza's: {largepizza}")
    print("-----------------------------------------")
    print(f"Prijs small pizza: {smalltotaal}")
    print(f"Prijs medium pizza: {mediumtotaal}")
    print(f"Prijs large pizza: {largetotaal}")

    print(f"TOTAAL: {smalltotaal + mediumtotaal + largetotaal}")

    print("                                          ")
    print("-----------------------------------------")
except ValueError:
    print("Ongeldige invoer. Voer een geheel getal in voor het aantal pizza's.")
