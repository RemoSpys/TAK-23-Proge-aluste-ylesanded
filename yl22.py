import random

# lõpmatu tsükkel
while True:
    # Küsime kasutajalt valikut (Kivi, Paber, Käärid)
    user_action = input("Vali (Kivi, Paber, Käärid): ")
    # Võimalikud arvuti valikud
    possible_actions = ["Kivi", "Paber", "Käärid"]
    # Arvuti valib juhuslikult ühe võimaluse
    computer_action = random.choice(possible_actions)
    print(f"\nSa valisid: {user_action}, arvuti valis {computer_action}.\n")

    # Kontrollime, kes võitis või kas oli viik
    if user_action == computer_action:
        print(f"Mõlemad mängijad valisid {user_action}. See on viik!")
    elif user_action == "Kivi":
        if computer_action == "Käärid":
            print("Kivi tapab käärid! Sa võidad!")
        else:
            print("Paber tapab kivi! Sa kaotad.")
    elif user_action == "Paber":
        if computer_action == "Kivi":
            print("Paber tapab kivi! Sa võidad!")
        else:
            print("Käärid tapab paberi! Sa kaotad.")
    elif user_action == "Käärid":
        if computer_action == "Paber":
            print("Käärid tapab paberi! Sa võidad!")
        else:
            print("Kivi tapab käärid! Sa kaotad.")

    # Küsime kasutajalt, kas nad soovivad veel mängida
    play_again = input("Tahad veel mängida? (JAH/EI): ")
    # Kui kasutaja vastus ei ole "jah", siis katkestame tsükli
    if play_again.lower() != "jah":
        break