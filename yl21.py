import random
# Genereerime juhusliku arvu vahemikus 0 kuni 99
n=random.randrange(0, 100)
# Küsime kasutajalt arvatava arvu
g = int(input("Sisesta oma arvatav: "))
# Algab while-tsükkel, mis jätkub seni, kuni kasutaja arvab õige arvu
while n!= g:
    # Kontrollime, kas kasutaja arvatav arv on väiksem kui genereeritud arv
    if g < n:
        print("Paku kõrgemale")
        g = int(input("Sisesta arvatav uuesti: "))
    # Kontrollime, kas kasutaja arvatav arv on suurem kui genereeritud arv
    elif g > n:
        print("Paku vähem")
        g = int(input("Sisesta arvatav uuesti: "))
    # Jõuame siia ainult juhul, kui kasutaja on arvanud õige arvu, katkestame tsükli
    else:
        break
print("Õige!")