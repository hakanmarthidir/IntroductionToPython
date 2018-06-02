# Functions
# Fonksiyon tanımlamak için en onemli kural def anahtar kelimesini kullanmaktır.
# Kod tekrarını engellemek ve bir tanım catısı altında bunları ayrıstırmak için kullanılır.
# Bu sayede bu kodlar uzerinde yapılacak olan bir duzenleme ile kullanıldıgı her yeri guncellemiş olursunuz.
# Kodlarınızı iş bazlı ayrıstırarak daha duzenli bloklar olusturabilirsiniz.
# Dısarıdan calisabilmesi için gerekli parametreleri alarak generic bir yapıya burunebilir.

def FirstMethod():
    print("İlk Methodumuz")

def CreateEmailFormat(name, surname):
    print(name+"."+surname+"@deneme.com.tr")

def Divider(number1,number2):
    return number1 / number2


FirstMethod()
CreateEmailFormat("hakan","hidir")
CreateEmailFormat("tugay","hidir")

result = Divider(2,1)
print(result)