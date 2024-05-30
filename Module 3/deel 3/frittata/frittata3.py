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
print("*",str_amount_fraction(total_egg), str_single_plural(total_egg, TXT_EGGS), f"({total_egg} g)" if total_egg < 100 else f"({total_egg:.0f} g)")
print("*",str_amount_fraction(total_milk_units), str_single_plural(total_milk_units, TXT_CUPS), "melk", f"({total_milk_ml:.1f} ml)" if total_milk_ml < 100 else f"({total_milk_ml:.0f} ml)")
print("*",str_amount_fraction(total_salt_units), str_single_plural(total_salt_units, TXT_TEASPOONS), "keukenzout", f"({total_salt_g:.1f} g)" if total_salt_g < 100 else f"({total_salt_g:.0f} g)")
print("*",str_amount_fraction(total_pepper_units), str_single_plural(total_pepper_units, TXT_TEASPOONS), "gemalen zwarte peper", f"({total_pepper_g:.1f} g)" if total_pepper_g < 100 else f"({total_pepper_g:.0f} g)")
print("*",str_amount_fraction(total_oil_units), str_single_plural(total_oil_units, TXT_SPOONS), "olijfolie", f"({total_oil_ml:.1f} ml)" if total_oil_ml < 100 else f"({total_oil_ml:.0f} ml)")
print("*",str_amount_fraction(total_onions), str_single_plural(total_onions, TXT_ONIONS), f"({total_onions} g)" if total_onions < 100 else f"({total_onions:.0f} g)")
print("*",str_amount_fraction(total_garlics), str_single_plural(total_garlics, TXT_GARLICS), f"({total_garlics} g)" if total_garlics < 100 else f"({total_garlics:.0f} g)")
print("*",str_amount_fraction(total_paprikas), str_single_plural(total_paprikas, TXT_PAPRIKAS), f"({total_paprikas} g)" if total_paprikas < 100 else f"({total_paprikas:.0f} g)")
print("*",str_amount_fraction(total_spinach_units),str_single_plural(total_spinach_units, TXT_CUPS), "spinazie", f"({total_spinach_g:.1f} g)" if total_spinach_g < 100 else f"({total_spinach_g:.0f} g)")
print("*",str_amount_fraction(total_cheese_units),str_single_plural(total_cheese_units, TXT_CUPS),  "geraspte cheddar kaas", f"({total_cheese_g:.1f} g)" if total_cheese_g < 100 else f"({total_cheese_g:.0f} g)")
print('-----------------------------------------------')
