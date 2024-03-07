sayi=int(input("Hocam sayı gir: "))
bolen=[]
for i in range(1,sayi+1):
    if sayi%i==0:
        bolen.append(i)
        print(i)
        
if len(bolen)==2:
    print("girdiğiniz sayı asaldır")
else:
    print("girdiğiniz sayı asal masal değildir ")
        
