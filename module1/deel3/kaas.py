vraagkaas = input("is de kaas geel? ")

# LINKS
# is de kaas geel?
if vraagkaas == "Ja":
    vraagg = input("Zitten er gaten in? ") # Zitten er gaten in
    if vraagg == "Ja":
        vraagd = input("Is de kaas belachelijk duur? ") # Is de kaas belachelijk duur?
        if vraagd == "Ja":
            print("Emmenthaler")
        elif vraagd == "Nee":
            print("Leerdammer")


    elif vraagg == "Nee":
        vraagh = input("Is de kaas hard als steen? ") #Is de kaas hard als steen?
        if vraagh == "Ja":
            print("Parmigiano Reggiano")
        elif vraagh == "Nee":
            print("Goudse kaas")
        

# RECHTS
if vraagkaas == "Nee":
    vraagg = input("Heeft de kaas blauwe schimmel? ") # Heeft de kaas blauwe schimmel?
    if vraagg == "Ja":
        vraagd = input("Heeft de kaas korst?  ") # Heeft de kaas korst? 
        if vraagd == "Ja":
            print("Blue de Rochbaron")
        elif vraagd == "Nee":
            print("Foume d'ambert ")


    elif vraagg == "Nee":
        vraagh = input("Heeft de kaas korst? ") #Heeft de kaas korst?
        if vraagh == "Ja":
            print("Camembert")
        elif vraagh == "Nee":
            print("Mozzarella")