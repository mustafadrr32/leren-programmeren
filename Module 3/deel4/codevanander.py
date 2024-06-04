import time
import sys

def slow_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
    print("")

def kies_karakter():
    slow_print("Kies een karakter:")
    slow_print("1. Spiderman")
    slow_print("2. Donald Duck")
    slow_print("3. Barbie")
    slow_print("4. Peter Pan")
    keuze = input("> ")
    if keuze == "1":
        return "Spiderman"
    elif keuze == "2":
        return "Donald Duck"
    elif keuze == "3":
        return "Barbie"
    elif keuze == "4":
        return "Peter Pan"
    else:
        slow_print("Ongeldige keuze, probeer het opnieuw.")
        return None

gekozen_karakter = kies_karakter()

if gekozen_karakter is not None:
    slow_print(f"Je hebt {gekozen_karakter} gekozen.")

slow_print("We gaan nu beginnen met het spel dus maak je klaar.")
slow_print("Goeiedag, jij bent een echte avonturier. Dit bos is levensgevaarlijk en er komen weinig mensen levend uit. Om uit het bos te ontsnappen moet je 10 vragen goed beantwoorden, anders kan het nog slecht met je aflopen. Veel Geluk.")

vragen = [
    ("Je ziet een aparte vrouw die je snoepjes aanbied en wil dat je meegaat naar haar huis, wat doe je?", ["a. je neemt de snoepjes aan en gaat met haar mee", "b. je wijst haar vriendelijk af", "c. je berooft de vrouw van haar snoepjes en gaat weg"], "b"),
    ("Je hoort geritsel in de struiken. Wat doe je?", ["a. erin springen", "b. in de fik steken", "c. negeren en doorlopen"], "c"),
    ("Een oude brug komt tevoorschijn. Wat doe je?", ["a. Oversteken", "b. vliegen", "c. opblazen"], "b"),
    ("Je ziet een vreemde figuur in de verte. Wat is je reactie?", ["a. je gaat erheen en vraagt om een selfie", "b. Verstoppen", "c. uitschelden"], "b"),
    ("Het begint te regenen. Wat doe je?", ["a. Een schuilplaats zoeken", "b. Doorgaan in de regen", "c. Een paraplu maken"], "a"),
    ("Je vindt een mysterieuze sleutel op de grond. Wat doe je?", ["a. Meenemen", "b. Negeren", "c. in het water gooien"], "a"),
    ("Een hongerige wolf blokkeert je pad. Hoe ga je ermee om?", ["a. je blijft rustig en stil", "b. Vechten", "c. wegrennen"], "b"),
    ("Je ziet een oud ma     nuscript op de grond liggen. Wat doe je?", ["a. Lezen", "b. negeren", "c. Verbranden"], "a"),
    ("Een reuze spinnenweb blokkeert de doorgang. Wat is je reactie?", ["a. Verwijderen", "b. je schiet het open waardoor je door kan", "c. je loopt om"], "b"),
    ("Je hoort een vreemd geluid achter je. Wat doe je?", ["a. Omkeren en kijken", "b. Doorgaan en gaan rennen", "c. Roepen"], "b"),
]

score = 0
for vraag, opties, correct_antwoord in vragen:
    slow_print(vraag)
    for optie in opties:
        slow_print(optie)
    antwoord = input("> ")
    if antwoord == correct_antwoord:
        score += 1
    else:
        slow_print("Helaas, dat was het verkeerde antwoord.")
        break

if score == len(vragen):
    slow_print("Gefeliciteerd, je hebt het spel gewonnen!")