# Küsime kasutajalt lemmiklooma
pet = input("Sisesta oma lemmikloom: ")
# Väljastame lemmiklooma nime esimese tähe
print(pet[0])
# Loome olemasolevate lemmikloomade listi
pets = ["Koer", "Kass", "Karu"] 
# Lisame kasutaja sisestatud lemmiklooma listi
pets.append(pet)
print(pets)