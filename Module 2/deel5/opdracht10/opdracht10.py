from fruitmand import fruitmand

sorted_weights = sorted(fruitmand, reverse=True, key=lambda x: x['weight'])

for item in sorted_weights:
    print(item['weight'])