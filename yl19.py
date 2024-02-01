# Määratleme täishäälikute järjendi
letters="a", "e", "i", "o", "u", "õ", "ä", "ö", "ü"
# Küsime kasutajalt sõna
a=input("Sisesta sõna: ")
# Loendame täishäälikute arvu sõnas
b=a.count("a") +a.count("e") +a.count("i") +a.count("o") +a.count("u") +a.count("õ") +a.count("ä") +a.count("ö") +a.count("ü")
print(b)