from recipe_lib import *
from frittata_ingredients import *

# -------- TITLE --------
print('=============== Frittata recept ===============')
# -------- INPUT --------
# use recipe_lib for input of nr_persons
nr_persons = int(input("voer aantal personen in: ")) # replace this with better input

# ----- CALCULATIONS ----
# calculate factor 
factor = nr_persons / RECIPE_PERSONS

# calculate amount_eggs

amount_egg = AMOUNT_EGGS * factor
total_egg = round_piece(amount_egg)
print(TXT_EGGS)

# calculate amount_milk

amount_milk = AMOUNT_MILK * factor
total_milk = round_quarter(amount_milk)


# calculate amount_salt
amount_salt = AMOUNT_SALT * factor
total_salt = round_quarter(amount_salt)



# calculate amount_pepper
amount_pepper = AMOUNT_PEPPER * factor
total_pepper = round_quarter(amount_pepper)

# calculate amount_oil
amount_oil = AMOUNT_OIL * factor
total_oil = round_quarter(amount_oil)

# calculate amount_onions
amount_onions = AMOUNT_ONIONS * factor
total_onions = round_piece(amount_onions)

# calculate amount_garlics
amount_garlics = AMOUNT_GARLICS * factor
total_garlics = round_piece(amount_garlics)

# calculate amount_spinach
amount_spinach = AMOUNT_SPINACH * factor
total_spinach = round_quarter(amount_spinach)

# calculate amount_paprikas
amount_paprikas = AMOUNT_PAPRIKAS * factor
total_paprikas = round_piece(amount_paprikas)

# calculate amount_cheese
amount_cheese = AMOUNT_CHEESE * factor
total_cheese = round_quarter(amount_cheese)

# -------- OUTPUT -------
print('=============== Frittata recept ===============')
print(f'Ingrediënten voor {nr_persons} personen:')
print('-----------------------------------------------')
# print (formatted) all amounts and units combined with their ingrediënt descriptions
print("*", total_egg, TXT_EGGS)
print("*", total_milk, TXT_MILK)
print("*", total_salt, TXT_SALT)
print("*", total_pepper, TXT_PEPPER)
print("*", total_oil, TXT_OIL)
print("*", total_onions, TXT_ONIONS)
print("*", total_garlics, TXT_GARLICS)
print("*", total_paprikas, TXT_PAPRIKAS)
print("*", total_spinach, TXT_SPINACH)
print("*", total_cheese, TXT_CHEESE)

print('-----------------------------------------------')