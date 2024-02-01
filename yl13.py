# Küsime kasutajalt faili
fail = input("Sisesta .ext fail: ")
# Kasutame split meetodit, et jagada failinimi
list = fail.split(".")
print(list[-1])