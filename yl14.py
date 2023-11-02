a = input("Sisesta string: ").strip()

if len(a)>= 7:
    if (len(a) % 2) == 0:
        print("Sobib!")
    else:
        print("Ei sobi")

print(a[len(a)//2-1:len(a)//2+2])