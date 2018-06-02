# Donguler - For
# Bir başlangıc, bir bitiş noktası olan, bitiş noktasına gelene kadar hep aynı işlemleri yapan mekanizmalara denir.

myNames = list((2, 3, 4, 5, 6))
print(myNames)

for a in myNames:
    print(a)

for x in range(100):
    print(x)

for x in range(2, 90):
    print(x)

for x in range(1, 100, 5):
    print(x)

# Break : dongu calismaya devam ederken eger istediginiz bir kosul saglandıysa donguyu sonlandırarak kaynak yonetimini yapabilirsiniz.
# dongu gereksiz yere calismaya devam etmemiş olur.
for x in range(1, 100):
    if (x == 45):
        print("Aradıgımızı bulduk..")
        break
    print(x)


#Continue : donguyu belirli bir yerde durdurmus olabilirsiniz. bu anahtar kelime ile dongunun devam etmesini saglayabilirsiniz.
myTuple = ("hakan","ayhan","orhan","emre","kaan")
for name in myTuple:
    if name == "emre":
        continue
    print(name)