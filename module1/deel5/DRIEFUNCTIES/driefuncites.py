# import math

# from test_lib import test, report

# def calculate_cilinder_content(diameter, hoogte):

#     inhoud = (diameter / 2) ** 2 * math.pi * hoogte

#     inhoud = round(inhoud, 1)

#     return inhoud
# test_data = [

#     (8.0, 5.0, 251.3),

#     (11.0, 7.0, 665.2),

#     (18.0, 7.0, 1781.3),

#     (15.0, 2.0, 353.4),

#     (0.0, 6.0, 0.0)

# ]
# for diameter, hoogte, expect_content in test_data:
#     calculated_content = calculate_cilinder_content(diameter, hoogte)
#     name = f'test diameter: {diameter} height: {hoogte}'
#     test(name, expect_content, calculated_content)
#     report()


# OPDRACHT2

from test_lib import test, report

from decimal import Decimal, ROUND_HALF_UP
def round_to_stuivers(bedrag):

    bedrag = Decimal(str(bedrag))

    afgerond_bedrag = bedrag.quantize(Decimal('0.05'), rounding=ROUND_HALF_UP)

    return float(afgerond_bedrag)
test_data = [2.24, 13.01, 9.95, 4.78, 6.62]
for origineel_bedrag in test_data:

    afgerond_bedrag = round_to_stuivers(origineel_bedrag)

    name = f'test origineel bedrag: {origineel_bedrag}'

    test(name, afgerond_bedrag, origineel_bedrag)
report()


# from test_lib import test, report

 

# MONTH_DISCOUNT_PERC = 10

 

# def calc_discount(price: float, brand: str, month_discount_brands: str) -> float:

#     discount_brands = month_discount_brands.split(',')

#     if brand in discount_brands:

#         discount = round((price * MONTH_DISCOUNT_PERC) / 100, 2)

#         return discount

#     else:

#         return 0.0

   

# calc_discount_brands = 'Vespa,Kymco,Yamaha'

 

# test("korting vespa", 100.0, calc_discount(1000.0, 'Vespa', calc_discount_brands))

 

# test("korting honda", 0.0, calc_discount(800.0, 'Honda', calc_discount_brands))

 

# test("korting kymco", 50.05, calc_discount(500.5, 'Kymco', calc_discount_brands))

 

# test("korting Yamaha", 250.0, calc_discount(2500, 'Yamaha', calc_discount_brands))

 

# test("Korting ABC", 0.0, calc_discount(600.0, 'ABC', calc_discount_brands))

 

# report()

 