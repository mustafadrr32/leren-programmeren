aantalCroissant = 25
aantalStokbroden = 6
aantalKortingsbonnen = 5
croissantPrijs = aantal_croissant *0.39
stokbrodenPrijs = aantal_stokbroden * 2.78
kortingsbonnenPrijs = aantal_kortingsbonnen * 0.50

Intotaal = ((croissantPrijs + stokbrodenPrijs) - kortingsbonnenPrijs)

print(f"De feestlunch kost je bij de bakker {Intotaal} euro voor de {aantalCroissant} croissantjes en de {aantalStokbroden} stokbroden als de {aantalKortingsbonnen} kortingsbonnen nog geldig zijn!")