aantalCroissant = int(input("Voer aantal crossiant in: "))
aantalStokbroden = int(input("Aantal stokbroden: "))
aantalKortingsbonnen = int(input("Aantal kb: "))
croissantPrijs = aantalCroissant * float(0.39)
stokbrodenPrijs = aantalStokbroden * float(2.78)
kortingsbonnenPrijs = aantalKortingsbonnen * float(0.50)

Intotaal = ((croissantPrijs + stokbrodenPrijs) - kortingsbonnenPrijs)

print(f"De feestlunch kost je bij de bakker {Intotaal} euro voor de {aantalCroissant} croissantjes en de {aantalStokbroden} stokbroden als de {aantalKortingsbonnen} kortingsbonnen nog geldig zijn!")