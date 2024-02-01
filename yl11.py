# Loome listi "fruitlist" kolme viljaga
fruitlist = ["apple", "pear", "cherry"]
print(fruitlist[0])
# Lisame listi ühe vilja ("pear")
fruitlist.append("pear")
print(fruitlist)
print(fruitlist[-1])
#fruitlist(1) = (black)
print (fruitlist)
if "apple" in fruitlist:
    print ("apple, is on the list")

    print(len(fruitlist))
    fruitlist.pop(1)
    print (fruitlist)
    fruitlist.remove