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

x = input("")
words = x.split()
vertaling = ""
for word in words:
    vertaald = vertaal.get(word.lower(), word)
    vertaling += vertaald + " "

print("Vertaald: ")
print(vertaald)
    



#In het hart van de grot zagen ze Draganthor, met zijn glinsterende schubben en vurige ogen. De draak brulde en spuwde een vlammenzee die hen bedreigde, maar Rurik beschermde hen met een krachtig schild van magie.
#Bij de ingang van de grot zagen ze Draganthor, met zijn glinsterende teennagels en waterende ogen. De geit brulde en spuwde een golf van water die hen bedreigde, maar Rurik beschermde hen met een krachtig zwemvliezen van plastic.

