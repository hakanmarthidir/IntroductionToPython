# CONDITIONS
# Mantıksal operatorler ile desteklenir.
# İçerisinde bulundugumuz durumu kontrol edip buna gore uygulama akısını yonlendirmek için kullanılır.

# ==,  !=, <, >, <= , >=,

#sayı toplamını kontrol edelim...
number1 = input("Sayi 1 : ")
number2 = input("Sayi 2 : ")
total = number1 + number2

if total >= 100:
    print("100 veya 100den buyuk")
else:
    print("100den küçük")


#birden fazla durumu kontrol etmek
if number1 > number2:
    print("1, 2 den buyuk")
elif number2 > number1:
    print("2, 1 den buyuk")
else:
    print("esitler..")


#Aynı anda birden fazla kosulun saglanması gerekiyorsa : and
username = input("Kullanıcı adınız : ")
password = input("Sifreniz : ")
if username=="admin" and password=="12345":
    print("Hosgeldin Admin")
else:
    print("Yetkiniz bulunmamaktadır")


#Kosullardan herhangi biri saglanıyorsa : or
searchText = input("Aradıgınız ürünü yazınız : ")
if searchText == "mouse" or searchText == "klavye":
    print("5 nolu reyon")
elif searchText =="pc" or searchText=="laptop":
    print("6 nolu reyon")
else:
    print("Üzgünüz, aradıgınız ürün grubu bulunmamaktadır.")

