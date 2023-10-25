from test_lib import test, report
from math import floor, ceil

nr = 5.65499901
expected = 5.65
calculated = round(nr, 2)
test('example', expected, calculated)

nr = 13
expected = 13.0
calculated = float(nr)  # Gebruik de 'float' functie om een float-waarde te verkrijgen
test('to-the-point', expected, calculated)

nr = -45.372
expected = 45.372
calculated = abs(nr)  # Gebruik de 'abs' functie om de absolute waarde te verkrijgen
test('optimistic', expected, calculated)

nr = -45.372
expected = -45.4
calculated = round(nr, 1)  # Gebruik 'round' om het aantal decimalen te beperken
test('approximately', expected, calculated)

nr = 45.372
expected = -45.372
calculated = -nr  # Gebruik het negatieve teken om de negatieve waarde te krijgen
test('pessimistic', expected, calculated)

nr = -2.3
expected = floor(-3)
calculated = floor(nr)  # Gebruik 'floor' om naar beneden af te ronden
test('depressed', expected, calculated)

nr = -7.25
expected = int(-7)
calculated = int(nr)  # Gebruik 'int' om naar een geheel getal af te ronden
test('pointless', expected, calculated)

nr = 15.11
expected = 16
calculated = ceil(nr)  # Gebruik 'ceil' om naar boven af te ronden
test('sky-is-the-limit', expected, calculated)

report()
