#STRING OPERATIONS
# Degiskenlerin kendilerine ozgu ozellikleri vardır.
# bu ozelliklere . denilerek erişilebilir.
# tum harfleri kucuk yapma, buyuk yapma, harf sayısını ogrenme,
# tum karakterler sayı mı diye kontrol etme vs.


import sys

myName = "hAKan"
myLowerName = myName.lower()
print(myLowerName)

digitInfo = myName.isdigit()
print(digitInfo)

yourname = input("adın nedir: ")
myLen = yourname.__len__()
print(yourname)
print(myLen)