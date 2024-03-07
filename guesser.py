import random
hak=int(input("kaç hakka sahip olmak istersiniz: "))
sayac=0
x=random.randint(1,100)
while True:
    tahmin=int(input("sayı tahmininiz nedir: "))
    sayac=sayac+1
    hak=hak-1
    if 0<hak:
        if x<tahmin:
            print("lütfen tahmin değerinizi azaltınız ")
        elif x>tahmin:
            print("lütfen tahmin değerinizi artırınız")
        else:
            puan=100-(100/(sayac)*(sayac-1))
            print(f"tahmin doğru puanınız {puan} tahmin sayınız {sayac}")
            break
    elif hak==0:
        if x==tahmin:
            puan=100-(100/(sayac)*(sayac-1))
            print(f"son hakkınızda bildiniz tahmin doğru puanınız {puan} tahmin sayınız {sayac}")
        else:
            print(f"hakkınız bitti tutulan sayı {x} ")
            break



