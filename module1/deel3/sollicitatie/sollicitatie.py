print("Sollicitatie Circusdirecteur voor Circus HotelDeBotel")
naam = input("Wat is uw naam? ")
rijbewijs = input("Bent uw in bezit van een geldig Vrachtwagen rijbewijs? ").lower()
hooghoed = input("Bent uw in bezit van een hoge hoed? ")
gewicht = int(input("Hoe zwaar bent u? "))
lengte = int(input("Hoe lang (CM) bent u? "))
certificaat = input("Certificaat 'overleven met gevaarlijk personeel'? (J/N) ").lower()
print(" # Laat ook bij volgende vragen al heb je een van deze ervaringen of meer hoeveel jaar het is. # ")
ervaring1 = int(input("Hoeveel jaar praktijkervaring heeft u met dieren-dressuur? "))
ervaring2 = int(input("Hoeveel jaar praktijkervaring heeft u met jongleren? "))
ervaring3 = int(input("Hoeveel jaar praktijkervaring heeft u met acrobatiek? "))
min_gewicht = 90  
max_gewicht = 120 
min_lengte = 150  
max_lengte = 220


if ((lengte >= min_lengte and lengte <= max_lengte) and (gewicht >= min_gewicht and gewicht <= max_gewicht) and (rijbewijs == "ja") and (hooghoed == "ja") and (certificaat == "j") and (ervaring1 >= 4 or ervaring2 >= 5 or ervaring3 >= 3)):
    print("U bent geschikt, stuur snel mogelijk u cv..")
else :
    print("Helaas, we moeten u teleurstellen..")