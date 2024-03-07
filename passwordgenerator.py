
import random


with open("karakterlistesi.txt","r") as dosya:
    karakterlisteleri=dosya.readlines()
    

secim=str(input("Hangi karakter listesini kullanmak istiyorsunuz (1veya2): "))

if secim=="1":
    karakterlist=karakterlisteleri[0]
else:
    karakterlist=karakterlisteleri[1]
    
Lenght=int(input("Parolanın uzunluğunu giriniz: "))

parola=""
for i in range(Lenght):
    parola+=random.choice(karakterlist)
    
print(f"oluşturulan parola:{parola}")
