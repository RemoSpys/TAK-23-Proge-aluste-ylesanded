import random
n=random.randrange(0, 100)
g = int(input("Sisesta oma arvatav: "))
while n!= g:
    if g < n:
        print("Paku kõrgemale")
        g = int(input("Sisesta arvatav uuesti: "))
    elif g > n:
        print("Paku vähem")
        g = int(input("Sisesta arvatav uuesti: "))
    else:
        break
print("Õige!")