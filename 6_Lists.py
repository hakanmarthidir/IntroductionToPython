# LISTS
# birden fazla elemanı tek bir catı altında tutmak için kullanılan bir yapıdır.
# listelerdeki her bir elemanın sıra numarası vardır. buna index denir. ve indexler daima 0 dan baslar.
# ornegin listedeki ilk elemanı ogrenmek için 0. indexi kullanırsınız.
# son eleman için ise elemansayısı - 1 formulu işe yarayacaktır.

numberList = [2, 3, 4, 1, 5, 6, 7, 8, 9]
charList = list(("a", "b", "c"))

# ilk eleman, son eleman
print(numberList[0])
print(numberList[numberList.__len__() - 1])

# Listeye eleman eklemek için
numberList.append(10)

# pop : eleman atamasını yapar ve listeden cıkartır.
print(numberList.pop(0))
print(numberList[0])

# remove
charList.remove("a")
print(len(charList))
print(charList)


