vraagkaas = input("is de kaas geel? ").lower()

# LINKS
# is de kaas geel?
if vraagkaas == "ja":
    vraagg = input("Zitten er gaten in? ") # Zitten er gaten in
    if vraagg == "ja":
        vraagd = input("Is de kaas belachelijk duur? ") # Is de kaas belachelijk duur?
        if vraagd == "ja":
            print("Emmenthaler")
        elif vraagd == "nee":
            print("Leerdammer")


    elif vraagg == "nee":
        vraagh = input("Is de kaas hard als steen? ") #Is de kaas hard als steen?
        if vraagh == "ja":
            print("Parmigiano Reggiano")
        elif vraagh == "nee":
            print("Goudse kaas")
        

# RECHTS
if vraagkaas == "nee":
    vraagg = input("Heeft de kaas blauwe schimmel? ") # Heeft de kaas blauwe schimmel?
    if vraagg == "ja":
        vraagd = input("Heeft de kaas korst?  ") # Heeft de kaas korst? 
        if vraagd == "ja":
            print("Blue de Rochbaron")
        elif vraagd == "nee":
            print("Foume d'ambert ")


    elif vraagg == "nee":
        vraagh = input("Heeft de kaas korst? ") #Heeft de kaas korst?
        if vraagh == "ja":
            print("Camembert")
        elif vraagh == "nee":
            print("Mozzarella")