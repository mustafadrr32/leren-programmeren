a = int(input("Voer een hele getal in voor a: "))
b = int(input("Voer een hele getal in voor b: "))

if a > b: #if statement
    Max = a
    print(f"a is het grootste getal: {Max}")
    Min = b
elif a < b: #elif statement
    Min = a
    Max = b
    print(f"a is het kleinste getal: {Min}")
#else statement
else:
    print("a is gelijk aan b")
    Min = b

print("Het minimum is:", Min)
print("Het maximum is:", Max)
