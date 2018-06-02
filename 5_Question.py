# Dışarıdan girilen iki sayıya ihtiyacımız var.
# birincisinin 3. kuvveti ile,
# ikincisinin 2e bolumunden kalanı toplayınız ve ekranda sonucu asagidaki formatta gosteriniz.
# Sonuç =>  2


# DEBUGGING:
# Etkin bir hata yakalama ve uygulamanın davranıslarını basamak basamak izleme yontemidir.
# Degiskenler hangi degeri aldı, yapılan hesaplamalardan sonra ortaya nasıl bir sonuc cıktı gibi tum stepleri takip edebilirsiniz.
# Bunun için yapılması gereken izlemek istediginiz kod blogu sol tarafına kırmızı bir debug simgesi yerlestirmek. kodun sol tarafındaki gri alana tıklyarak bunu cıkartabilrisiniz.
# daha sonra debug modda uygulamayı start etmek yeterli. kodların sırası belirlediginiz yere gelince uygulama duracak ve yonetimi siz ele alacaksınız.
# f7 ile step step manual olarak ilerleyebilirsiniz.


#TRY - EXCEPTION
#Uygulamalarımız her zaman istedigimiz gibi calismayabilir. Kullanıcıdan alınarak ilerleyen bir uygulamamız olabilir ve dısarıdan istedigimiz formatta bir bilgi gelmeyebilir.
#aradıgımız bir dosya silinmis olabilir. bu gibi durumlarda uygulamamız hata verecektir ve ekranda hata mesajını gostererek yoluna devam edemeyecektir.
#buna benzer durumlarda uygulamanın patlamasını engelleyebilir ve hata anlarını handle edebilirsiniz. bunun yontemlerinden biri de try-exceptiondır
#try blogu altında normalde calismasını istedigimiz kodları yazarız.
#exception ise yukarıdaki kodlar calisirken ortaya cıkan istisnai durumlarda neler yapılacagını temsil eder.

try:
    n1 = input("Sayi 1 : ")
    n2 = input("Sayi 2 : ")

    numberP = float(n1) ** 3
    numberD = float(n2) % 2
    result = numberP + numberD
    print("Sonuç => " + str(result))

except Exception as e:
    print("Bir hata meydana geldi.")
