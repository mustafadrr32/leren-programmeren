totaal = 0
current_number = 20
iteration = 3

while totaal <= 2000:
        totaal += current_number
        print(f"{iteration}. {'+'.join(map(str, range(36, current_number + 3)))} = {totaal}")
        current_number += 3
        iteration += 36