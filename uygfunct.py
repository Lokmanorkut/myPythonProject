#a=int(input("sayı gir"))
#b=int(input("2.sayıyı gir"))
#
#def asal(a,b):
#    for sayi in range(a,b+1):
#        if sayi>1:
#            for i in range(2,sayi):
#                if sayi%i==0:
#                    break
#                else:
#                    print(sayi)
#                    break
#
#
#asal(a,b)
        
sayi=int(input("sayıyı giriniz: "))
def tambol(sayi):
    liste=list()
    for i in range(1,sayi+1):
        if sayi % i==0:
            liste.append(i)
            liste.append(-i)
        
    print(liste)

tambol(sayi)