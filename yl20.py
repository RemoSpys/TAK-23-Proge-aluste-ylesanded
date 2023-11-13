number = int(input("Sisesta arv: "))

print("Kordused: ")
for i in range(1, 13):
    result = number * i
    print(f"{number} x {i} = {result} ")