

#while True:

#if x>5:
##    raise Exception as e:
#
##    def checkpassword(psw):
#        if len(psw)<8:
#            raise Exception("parola en az 7 karakter olmalı")
#        elif not re.search("[a-z]",psw):
#            raise Exception("parola küçük harf içermelidir")
#        elif not re.search("[A-Z]",psw):
#            raise Exception("parola büyük harf içermelidir")
#        elif not re.search("[1-9]",psw):
#            raise Exception("parola rakamiçermelidir")
#        elif not re.search("[-@$]",psw):
#            raise Exception("parola alpha numeric içermelidir")
#        else:
#            print("geçerli parola")
#        
#    password="123456"
#
#    try:
#        checkpassword(password)
#    except Exception as ex:
#        print(ex)
#    else:
#        print("geçerli parola")
#    finally:
#        print("validation tamamlandı")
#    


#class Person:
#    def __init__(self,name,year):
#        if len(name)>10:
#            raise Exception("name alanı fazla karakter içeriyor ")
#        else:
#            self.name=name
#            
#            
#
#
#p=Person("Alşaqxöpaaaaaaaaaaa",12912)

#liste=["1","2","5a","10b","abc","10","50"]#
#

##bosListe=[]
##
##for x in liste:
##    try:
##        result=int(x)
#        print(result)
#    except ValueError:
#        continue

##while True:
#    sayi=input("sayı: ")
#    if sayi=="q":
#        break
#
#    
#    try:
#        result=float(sayi)
#        print("girdiğiniz sayı: ",result)
#    except ValueError:
#        print("geçersiz sayı")
#        continue
#        
turkce_karakterler="şçiğüöİ"



#def chechkPassword(parola):    
#    parola=input("parola: ")
#    for i in parola:
#        if i in turkce_karakterler:
#            raise TypeError("türkçe karakter girmemelisiniz")
#        else:
#            pass
#    print("geçerli parola")
#
#parola=input("parola: ")
#
#try:
#    chechkPassword(parola)
#except TypeError as err:
#    print(err)
#try kısmında hata alınacak yeri yazıyoruz except kısmında beklenen yapılması gereknei yazıyoruz 


# def faktoriyel(x):
#     x=int(x)
    
#     if x<0:
#         raise ValueError("Negatif değer")
    
#     result=1
    
#     for i in range(1,x+1):
#         result*=i
    
#     return result

# for x in[5,10,20,"5a",-3]:
#     try:
#         y=faktoriyel(x)
#     except ValueError as err:
#         print(err)
#         continue
    
#     print(y)
# try:
#     x=int(input("bir sayı"))
#     try:
#         result=10/x
#         print("Sonuç",result)
#     except ZeroDivisionError:
#         print("sıfıra bölme hatası ")
#     except ValueError:
#         print("geçersiz sayı")
    
# tuple=(1,2,3,4)
def findDivisors (n1, n2):
    divisors = [] #the empty list
    for i in range(1, min (n1, n2) + 1):
        if n1%i == 0 and n2%i == 0:
            divisors = divisors + [i]
    for i in divisors:
        print(i)

divisors = findDivisors(20, 100)
print(divisors)

total = 0
for d in divisors:
    total += d
print(total)