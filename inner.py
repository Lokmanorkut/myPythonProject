#def usalma(number):
#    
#    
#    def inner(power):
#        return number**power
#    
#    return inner
#two=usalma(2)
#
#three=usalma(3)
#print(two(3))
#print(three(4))

#def yetkiSorgula(page):
#    def inner(role):
#        if role =="admin":
#            return f"{role} rolü {page} sayfasına ulaşabilir"
#        else:
#            return f"{role} rolü {page} sayfasına ulaşamaz"
#        
#    return inner
#
#
#x=input("Please give a the page what talk about: ")
#y=input("What is your authority?: ")
#adminUser=yetkiSorgula(x)
#
#print(adminUser(y))
#            

def islem(islemadi):
    def toplam(*args):
        toplam=0
        for i in args:
            toplam+=i
            
        return toplam
    def carpma(*args):
        çarpma=1
        for i in args:
            toplam*=i
        return carpma
    
        