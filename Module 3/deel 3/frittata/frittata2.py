from recipe_lib import *
from frittata_ingredients import *

# -------- TITLE --------
print('=============== Frittata recept ===============')
# -------- INPUT --------
# use recipe_lib for input of nr_persons
nr_persons = input_nr_persons("voer aantal personen in: ") # replace this with better input

# ----- CALCULATIONS ----
# calculate factor 
factor = nr_persons / RECIPE_PERSONS

# calculate amount_eggs
amount_egg = AMOUNT_EGGS * factor
total_egg = round_piece(amount_egg)

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
# print (formatted) all amounts and units combined with their ingredient descriptions
print("*", str_amount_fraction(total_egg), str_single_plural(total_egg, TXT_EGGS))
print("*", str_amount_fraction(total_milk), str_units(total_milk, TXT_CUPS))
print("*", str_amount_fraction(total_salt), str_units(total_salt, TXT_TEASPOONS))
print("*", str_amount_fraction(total_pepper), str_units(total_pepper, TXT_TEASPOONS))
print("*", str_amount_fraction(total_oil), str_units(total_oil, TXT_SPOONS))
print("*", str_amount_fraction(total_onions), str_single_plural(total_onions, TXT_ONIONS))
print("*", str_amount_fraction(total_garlics), str_single_plural(total_garlics, TXT_GARLICS))
print("*", str_amount_fraction(total_paprikas), str_single_plural(total_paprikas, TXT_PAPRIKAS))
print("*", str_amount_fraction(total_spinach), str_units(total_spinach, TXT_CUPS))
print("*", str_amount_fraction(total_cheese), str_units(total_cheese, TXT_CUPS))
print('-----------------------------------------------')
