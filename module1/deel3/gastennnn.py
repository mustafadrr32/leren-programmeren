gastheer = input("wie is de gastheer? ").lower
gasten = int(input("Hoeveel gasten zijn er? "))
drank = True
chips = True

if gastheer == "mustafa" or (drank and gasten >= 4 and gasten <= 20 and gastheer != ""):
    print("Start the party")
elif gastheer == "wilfred" or (gasten > 20):
    print("No party")
else:
    print("No party") 