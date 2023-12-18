totaal = 0
current_number = 50
iteration = 1

while totaal <= 1000:
        totaal += current_number
        print(f"{iteration}. {'+'.join(map(str, range(50, current_number + 1)))} = {totaal}")
        current_number += 1
        iteration += 1

