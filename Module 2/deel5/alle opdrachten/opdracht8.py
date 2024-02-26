from fruitmand import fruitmand

fruitmand.append({
    'name': 'watermelon',
    'weight': 2500,
    'color': 'green',
    'round': True
})

total_weight = sum(fruit['weight'] for fruit in fruitmand)
print("Total weight of fruits in the fruit basket:", total_weight)
