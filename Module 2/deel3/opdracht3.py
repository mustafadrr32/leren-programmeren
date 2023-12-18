y = 0
while True:
    y += 1
    x = input("?")
    if x != "quit":
       print("opnieuw")
    else:
        print("done")
        print(f"hoe vaak? : {y}")
        break