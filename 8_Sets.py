#SETS
# sıralı degil, indexli degil
#her calistirildiginda farklı bir sıra ile yaratılır.

setList = {"jordan","kobe","lebron"}
print(setList)

mySet = set((23,33,45))
#eleman ekleme
mySet.add(32)
print(mySet)

#eleman silme
mySet.remove(45)
print(mySet)

#eleman sayısı
print(len(mySet))