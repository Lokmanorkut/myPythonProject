def changename(n):
    n="ada"

name="yiğit"

changename(name)

print(name)
#üst taraf valuetype
#def change(n):
#    n[0]="istanbul"
#
#
#sehirler=["ankara","konya"]
#
#
#n=sehirler[:]
#n[0]="istanbul"#aynı bok
#print(sehirler)
#print(n)

#def add(*params):
#    sum=0
#
#    for n in params:
#        sum=sum+n
#    return sum#return yapmazsan none döner
#print(add(10,20,201,123))
#

#dict objelerinde 2 yıldız(**) kullanılır
def displayuser(**args):
    for key,value in args.items():
        print("{} is {}".format(key,value))
displayuser(name="Çınar",age=2,city="istablue")
displayuser(name="ce",age=12,city="is",phone=2454131,emil="qqsfqlösqs@gmail.com")
displayuser(name="ada",age=21,city="istlue",phone=134156232)

def myfunct(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

myfunct(10,20,304,40,2014,40,key1="value1",key2="value2")


