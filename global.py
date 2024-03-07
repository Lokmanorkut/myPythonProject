x="global x"

def funct():
    x="local x"
    print(x)

funct()
print(x)


#####################

name="çınar"

def chang(newname):
    name=newname
    print(name)

chang("ada")
print(name)

name="glob"
#kümeler gibi ab
#global name
#global x funct içinde böyle tanımlıyoruz