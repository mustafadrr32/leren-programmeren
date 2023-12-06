import random
kleur = ['harten', 'klaveren', 'schoppen', 'ruiten']
kaarten = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'boer', 'vrouw', 'heer', 'aas']
joker = 2
deck = []
for i in range(len(kleur)):
    for kaart in kaarten:
        deck.append(kleur[i] + " " + kaart)
for i in range(joker):
    deck.append("joker")
for i in range(1, 8):
    random.shuffle(deck)
    print(f"kaart {i}: {deck.pop(0)}")
print(f"deck ({len(deck)} kaarten):{deck}")





    