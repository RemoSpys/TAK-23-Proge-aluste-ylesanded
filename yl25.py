# Loome sõnastiku 'person'
person = {
    "first_name": "Remo",
    "last_name": "Tammela",
    "birth_year": 2006,
    "location": "Mustjala",
    "favorite_dessert": "Sõõrikud",
}

print(person.get("location"))
print(person["location"])

# Muudame 'favorite_dessert' väärtust
person["favorite_dessert"] = "Moosipallid"

for key in person:
    print(key)

for value in person.values():
    print(value)

# Kontrollime, kas 'isikukood' võti eksisteerib sõnastikus
if "isikukood" in person:
    print("Isikukood on leitud ja olemas!")
else:
    print("Isikukoodi ei eksisteeri.")

print(len(person))

# Lisame uue võtme-väärtuse paari ja kustutame olemasoleva võtme
person["height"] = "192cm"
del person["birth_year"]

# Tühjendame sõnastiku
person.clear()