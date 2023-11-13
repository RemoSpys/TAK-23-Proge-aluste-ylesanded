import random

options = ["kivi", "paber", "käärid"]
r = random.choice(options)

while True
    a = input("Sisesta kivi, paber või käärid (lõpetamiseks x): ")

    if a == "kivi" and r == "käärid" or a == "paber" and r == "kivi" or a == 
        print("Sinu võit!")
        elif a == "kivi" and r == "paber" or a == "paber" and r == "käärid" or 