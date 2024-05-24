from recipe_lib import *
from frittata_ingredients import *

# -------- TITLE --------
print('=============== Frittata recept ===============')

# -------- INPUT --------
# use recipe_lib for input of nr_persons
nr_persons = input_nr_persons("voer aantal personen in: ")

# ----- CALCULATIONS ----
# calculate factor 
factor = nr_persons / RECIPE_PERSONS

# calculate amount_eggs
amount_egg = AMOUNT_EGGS * factor
total_egg = round_piece(amount_egg)

# calculate amount_milk
amount_milk = AMOUNT_MILK * factor
total_milk_units = round_quarter(amount_milk)
total_milk_ml = unit2ml(total_milk_units, UNIT_CUPS)

# calculate amount_salt
amount_salt = AMOUNT_SALT * factor
total_salt_units = round_quarter(amount_salt)
total_salt_g = ml2gram(unit2ml(total_salt_units, UNIT_TEASPOONS), GRAM_PER_ML_SALT)

# calculate amount_pepper
amount_pepper = AMOUNT_PEPPER * factor
total_pepper_units = round_quarter(amount_pepper)
total_pepper_g = ml2gram(unit2ml(total_pepper_units, UNIT_TEASPOONS), GRAM_PER_ML_PEPPER)

# calculate amount_oil
amount_oil = AMOUNT_OIL * factor
total_oil_units = round_quarter(amount_oil)
total_oil_ml = unit2ml(total_oil_units, UNIT_SPOONS)

# calculate amount_onions
amount_onions = AMOUNT_ONIONS * factor
total_onions = round_piece(amount_onions)

# calculate amount_garlics
amount_garlics = AMOUNT_GARLICS * factor
total_garlics = round_piece(amount_garlics)

# calculate amount_spinach
amount_spinach = AMOUNT_SPINACH * factor
total_spinach_units = round_quarter(amount_spinach)
total_spinach_g = ml2gram(unit2ml(total_spinach_units, UNIT_CUPS), GRAM_PER_ML_SPINACH)

# calculate amount_paprikas
amount_paprikas = AMOUNT_PAPRIKAS * factor
total_paprikas = round_piece(amount_paprikas)

# calculate amount_cheese
amount_cheese = AMOUNT_CHEESE * factor
total_cheese_units = round_quarter(amount_cheese)
total_cheese_g = ml2gram(unit2ml(total_cheese_units, UNIT_CUPS), GRAM_PER_ML_CHEESE)

# -------- OUTPUT -------
print('=============== Frittata recept ===============')
print(f'Ingrediënten voor {nr_persons} personen:')
print('-----------------------------------------------')
# print (formatted) all amounts and units combined with their ingredient descriptions
print("*", total_egg, str_single_plural(total_egg, TXT_EGGS))
print("*", f"{str_amount_fraction(total_milk_units)} ({total_milk_ml:.1f} ml)" if total_milk_ml < 100 else f"{str_amount_fraction(total_milk_units)} ({total_milk_ml:.0f} ml)", "melk")
print("*", f"{str_amount_fraction(total_oil_units)} ({total_oil_ml:.1f} ml)" if total_oil_ml < 100 else f"{str_amount_fraction(total_oil_units)} ({total_oil_ml:.0f} ml)", "olijfolie")
print("*", f"{str_amount_fraction(total_salt_units)} ({total_salt_g:.1f} g)" if total_salt_g < 100 else f"{str_amount_fraction(total_salt_units)} ({total_salt_g:.0f} g)", "zout")
print("*", f"{str_amount_fraction(total_pepper_units)} ({total_pepper_g:.1f} g)" if total_pepper_g < 100 else f"{str_amount_fraction(total_pepper_units)} ({total_pepper_g:.0f} g)", "peper")
print("*", total_onions, str_single_plural(total_onions, TXT_ONIONS))
print("*", total_garlics, str_single_plural(total_garlics, TXT_GARLICS))
print("*", total_paprikas, str_single_plural(total_paprikas, TXT_PAPRIKAS))
print("*", f"{str_amount_fraction(total_spinach_units)} ({total_spinach_g:.1f} g)" if total_spinach_g < 100 else f"{str_amount_fraction(total_spinach_units)} ({total_spinach_g:.0f} g)", "spinazie")
print("*", f"{str_amount_fraction(total_cheese_units)} ({total_cheese_g:.1f} g)" if total_cheese_g < 100 else f"{str_amount_fraction(total_cheese_units)} ({total_cheese_g:.0f} g)", "kaas")
print('-----------------------------------------------')
