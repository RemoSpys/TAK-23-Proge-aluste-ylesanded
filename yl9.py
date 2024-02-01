# Küsime kasutajalt kolm küljepikkust ja teisendame need (float´i)
a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))

# Kontrollime, kas küljepikkused moodustavad kolmnurga
if a >= b + c or b >= a + c or c >= a + b:
    print("Sellist kolmanurka pole olemas!")
elif a == b and b==c:
    print("Võrdkülgne kolmnurk")
elif a == b and b != c or a == c and a != b or b == c and b != a:
    print("Võrdhaarne")
else:
    print("Erikülgne kolmnurk")