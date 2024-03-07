#miras alma 
#küme tarzı kardeş
#çok iyi la

class Person:
    def __init__(self,Fname,Lname):
        self.firstname=Fname
        self.Lastname=Lname
        print("person created ")
    def whoAmI(self):
        print("I am a person")
        
    def eat(self):
        print("ı am eating right now")
        
        
        
class student(Person):
    def __init__(self, Fname, Lname,number):
        Person.__init__(self,Fname, Lname)
        self.studentnumber=number
    #override
    def whoAmI(self):
        print("ı am a student")
        
    def sayhello(self):
        print("Hello ı am a student")
        
class teacher(Person):
    def __init__(self, Fname, Lname,brans):
        Person.__init__(Fname, Lname,brans)
        self.brans=brans
    
    def whoAmI(self):
        print(f"ı am {self.brans} a teacher")
        

p1=Person("ali","veli")
s1=student("49","50",1256)    

print(p1.firstname+" "+p1.Lastname)
print(s1.firstname+" "+s1.Lastname+" "+str(s1.studentnumber))
p1.whoAmI()
s1.whoAmI()

s1.eat()
s1.sayhello()
t1=teacher("serkan","yılmaz","Math")

t1.whoAmI()