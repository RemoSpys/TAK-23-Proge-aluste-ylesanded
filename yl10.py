# Küsime kasutajalt nime
name = input("Sisesta oma nimi: ")
print("Tere", name)
# Küsime kasutajalt elukohta
location = input("Elukoht: ")
if  "saaremaa" in location.lower():
    print("See on hea koht kus elada! Oled vähemalt targem kui hiidlane ;)")
if  "hiiumaa" in location.lower():
    print("Mingi tross oled v?")
# Küsime kasutajalt vanust
age = input("Vanus: ")
# Teisendame vanuse tekstist täisarvuks
age = int(age)
# Kontrollime vanuse järgi ja väljastame vastava sõnumi
if age < 18:
    print("Sa väike poiss auto lähedale ei tohi minna isegi. Saa vanemaks...")
elif age == 18:
    print("Palju õnne täiskasvanuks saamise eest!")
else:
    print("Mis sõiduk sul perse all on siis kah?")