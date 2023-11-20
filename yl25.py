person = {
    "first_name": "Remo",
    "last_name": "Tammela",
    "birth_year": 2006,
    "location": "Mustjala",
    "favorite_dessert": "Sõõrikud",
}

print(person.get("location"))
print(person["location"])

person["favorite_dessert"] = "Moosipallid"

for key in person:
    print(key)

for value in person.values():
    print(value)

if "isikukood" in person:
    print("Isikukood on leitud ja olemas!")
else:
    print("Isikukoodi ei eksisteeri.")

print(len(person))

person["height"] = "191cm"
del person["birth_year"]

person.clear()