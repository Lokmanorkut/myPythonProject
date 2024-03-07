##person classı için name yearOfBirth job ve calculateAge() bir method sena.calculateAGe()   
#
#class Person:
#    #class atribiutes
#    address="no info"
#
#    
#    
#    
#    #object atribute
#    #constructor(yapıcı metod)
#    def __init__(self,name,year):
#        self.name=name
#        self.year=year
#        print("init metodu çalışıp olup")
##instance method
#    def intro(self):
#        print("hello there"+" "+ self.name)
#    def calculateage(self):
#        return 2019-self.year
#        
#p1=Person("ali",1990)
#
#
##selfi değiştirebiliriz sadece değişkeni temsil ediyor
#p2=Person("yağmur",1995)
#print(p1.name)
#print(p2.year)
#p1.address="Konya"
#print(p1.address)
#p1.intro()
#print(f"yaşım"{p1.calc})
#

class circle:
    pi=3.14
    
    def __init__(self,yaricap=1):
        self.yaricap=yaricap
        
    def cevrehesap(self):
        return 2*self.pi +self.yaricap 
    
    def alanhesapla(self):
        return self.pi*self.yaricap**2
    
    
c1=circle(2)


print(f"c1 alanı = {c1.alanhesapla()} c1 çevre= {c1.cevrehesap()}")