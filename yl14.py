# Küsime kasutajalt infot
a = input("Sisesta string: ").strip()

# Kontrollime, kas stringi pikkus on vähemalt 7 tähemärki
if len(a)>= 7:
# Kontrollime, kas stringi pikkus on paarisarv
    if (len(a) % 2) == 0:
        print("Sobib!")
    else:
        print("Ei sobi")

print(a[len(a)//2-1:len(a)//2+2])