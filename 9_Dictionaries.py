# DICTIONARIES
# değiştirilebilir, unordered ve indexlenmiş durumdadır.
# key ve value prensibine gore calisir.

myDict = {"car": "araba",
          "home": "ev",
          "apple": "elma"}

print(myDict)

players = dict(goalkeeper="Muslera",
               defence="Maicon",
               middleField="Fernando",
               forvet="Gomis")

print(players)

# Eleman Ekleme veya Güncelleme- olmayan bir kayıt girilirse ekler, varolanı gunceller.
myDict["red"] = "kırmızı"
myDict["home"] = "konut"
print(myDict)

# Eleman Silme
del (myDict["apple"])
print(myDict)

# eleman sayısı
print(len(players))


