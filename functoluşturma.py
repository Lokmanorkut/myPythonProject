#my="hello"
#
#print(type(my))
#my.format
##pythonorg docs tutorial methodlardan bahsediyor
#
#

def say(name="user"):
    return "hello"+ name

say("Çınar")
say()
msg=say("çınar")
print(msg)

def total(num1,num2):
    return num1+num2
result=total(15,20)
print(result)

def yashesapla(dogumyili):
    return 2023-dogumyili

ageC=yashesapla(2143)
print(ageC)

def emekli(dogumyili,isim):

    """
    DOCSTRİNG:emekliliğinize kaç yıl kaldığını gösteriyor
    INPUT:doğum yılı,isim
    OUTPUT:hesaplanan yıl bilgisi
    """
    yas=yashesapla(dogumyili)
    emeklilik=65-yas
    
    if emeklilik>0:
        print(f"emekliliğinize {emeklilik} yıl kaldı")
    else:
        print("emeklilik yaşınız geldi de geçiyor")

emekli(1950,"Ali")

help(emekli)
help(list.append)

