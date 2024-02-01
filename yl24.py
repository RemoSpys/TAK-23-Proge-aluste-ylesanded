def upc_check_digit(upc):
    check_sum = 0

    # Summeerime kõik paaritu indeksiga arvud koodis
    for i in range (1, 12, 2):
        check_sum += int(upc[i-1])  

    # Korrutame summa 3-ga  
    check_sum *= 3

    # Summeerime kõik paaris indeksiga arvud koodis
    for i in range (2, 11, 2):
        check_sum += int(upc[i-1])

    # Leiame summa jäägi 10-ga jagamisel
    reminder = check_sum % 10

    # Kui jääk ei ole 0, arvutame kontrollnumbri
    if ( reminder != 0 ):
        check_sum = 10 - reminder
    else :
        check_sum = 0

    print(check_sum)

# Testime funktsiooni kahe näitekoodiga
upc_check_digit("042100005264")
upc_check_digit("036000291452")