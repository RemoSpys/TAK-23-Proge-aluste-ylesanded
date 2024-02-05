# Müügitulu andmed kohviku ja joogitüüpide kaupa, {} on andmestruktuur, mis võimaldab seostada võtmeid konkreetsete väärtustega.
revenue = {
    "Johnver": {
        "Tea": 190,
        "Coffee": 325,
        "Water": 682,
        "Milk": 829
    },
    "Vanston": {
        "Tea": 140,
        "Coffee": 19,
        "Water": 14,
        "Milk": 140
    },
    "Danbree": {
        "Tea": 1926,
        "Coffee": 293,
        "Water": 852,
        "Milk": 609
    },
    "Vansey": {
        "Tea": 14,
        "Coffee": 1491,
        "Water": 56,
        "Milk": 120
    },
    "Mundyke": {
        "Tea": 143,
        "Coffee": 162,
        "Water": 659,
        "Milk": 87
    },
}

# Kulude andmed kohviku ja joogitüüpide kaupa
expenses = {
    "Johnver": {
        "Tea": 120,
        "Coffee": 300,
        "Water": 50,
        "Milk": 67
    },
    "Vanston": {
        "Tea": 65,
        "Coffee": 10,
        "Water": 299,
        "Milk": 254
    },
    "Danbree": {
        "Tea": 890,
        "Coffee": 23,
        "Water": 1290,
        "Milk": 89
    },
    "Vansey": {
        "Tea": 54,
        "Coffee": 802,
        "Water": 12,
        "Milk": 129
    },
    "Mundyke": {
        "Tea": 430,
        "Coffee": 235,
        "Water": 145,
        "Milk": 76
    },
}

# Välimine tsükkel käib läbi igasugused kohvikud, "for key in revenue" käib kood läbi igasugused kohvikud, kus "key" vastab konkreetsele kohviku nimele (nagu "Johnver", "Vanston" jne).
for key in revenue:
    # Algatame iga kohviku jaoks kogukasumi nullist
    total_profit = 0
    # Sisemine tsükkel käib läbi joogitüübid iga kohviku jaoks
    for drink in revenue[key]:
        # Iga joogi kasum leitakse müügitulust miinus kulud
        profit = revenue[key][drink] - expenses[key][drink]

        # Kui kasum on positiivne, siis lisatakse see kogukasumile
        if profit > 0:
            total_profit += profit

    # Prinditakse välja kohviku nimi ja ümardatud kogukasum (6.2% kasumimarginaaliga)
    print(key, round(total_profit * 0.062))
