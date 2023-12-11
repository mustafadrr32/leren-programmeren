vertaal = {

"in" : "bij",
"het" : "de",
"hart" : "ingang",
"schubben" : "teennagels",
"vurige" : "waterende",
"draak" : "geit",
"vlammenzee" : "golf",
"die" : "van",
"hen" : "water",
"schild" : "zwemvliezen",
"magie" : "plastic"



}

zin = input("voer in:")

woorden = zin.split()
vertaling = ""
for woord in woorden:
    vertaald_woord = vertaal.get(woord.lower(), woord)
    vertaling += vertaald_woord + " "

print(vertaling)