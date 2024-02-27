from fruitmand import fruitmand

kleur_vertaling = {
    'geel': 'yellow',
    'groen': 'green',
    'oranje': 'orange',
    'rood': 'red',
    'bruin': 'brown'
}

# Zoek het fruit met de langste naam
langste_naam_fruit = max(fruitmand, key=lambda x: len(x['name']))

# Vertaal de kleur
kleur = kleur_vertaling.get(langste_naam_fruit['color'], langste_naam_fruit['color'])

# Print de gegevens van het fruit met de langste naam
print("Fruit met de langste naam:")
print("Naam:", langste_naam_fruit['name'])
print("Gewicht:", langste_naam_fruit['weight'], "gram")
print("Kleur:", kleur)
print(f"Lengte van de naam: {len(langste_naam_fruit['name'])}")