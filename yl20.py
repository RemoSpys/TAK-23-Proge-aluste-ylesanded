# Küsime kasutajalt arvu
number = int(input("Sisesta arv: "))

# Prindime välja korrutustabeli esimesed 12 korrutist
print("Kordused: ")
for i in range(1, 13):
    result = number * i
    print(f"{number} x {i} = {result} ")