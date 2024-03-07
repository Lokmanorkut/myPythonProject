import math
m=0.436
r=0.0025
g=9.81
x=2
cap=0.026
momentTheo=0.000984
flag=True

def anamenu(*args):
    global secim
    try:
        secim=int(input("""*****Ana Menüye Hoş Geldiniz*****\n1-Tablo-1\n2-Tablo-2\n3-Tablo-3    """))
        if secim==1:
            table1()
        elif secim==2:
            tablo2()
        elif secim==3:
            table3()
    except ValueError:
        print("doğru şeyler gir")
        
    
def deadoralive(secim):
    global flag
    while True:
        try:
            flag=input("buradadan işlem yapmaya devam etmek  için 'y' tuşunu tuşlayın çıkmak istiyorsanız 'n' tuşunu tuşlayın: ")
            if flag=="y":
                table1()
            elif flag=="n":
                anamenu()
            else:
                print("lütfen n yada y değerinden birini giriniz")
        except ValueError:
            
            print("Lütfen doğru giriş sağlayınız")
        finally:
            flag=input("Tablo 1 den işlem yapmaya devam etmek için 'y' yi tuşlayın çıkmak istiyorsanız 'n' tuşunu tuşlayınız:")
    

def table1(*args):
    global hız
    global moment
    global dt
    while flag:  
        try:
            dt=float(input("lütfen dt yi giriniz: "))
            s=float(input("Lütfen s yi giriniz: "))
        except ZeroDivisionError:
            print("dt veya s 0 olamaz!!")
        except ValueError:
            print("lütfen sayı giriniz")   
        finally:  
            moment=m*math.pow(r,2)*((2*g*s)/math.pow(hız,2)-1)
            hız=float(cap/dt)
            print(f"hızınızın değeri: {hız} m/s")
            print(f"eylemsizlik momentinin değeri {moment} kg.m²")
            deadoralive()


def tablo2(*args):
    global acisalhiz
    while flag:
        try:
                s=float(input("lütfen s değerini giriniz: "))
                acisalhiz=float(hız/r)
                potan=float(m*g*s)
                kinetikT=float(0.5*m*math.pow(hız,2))
                kinetikR=float((0.5*momentTheo)*(math.pow(acisalhiz,2)))
                kinetikToplam=float(kinetikT+kinetikR)
                print(f"potansiyel enerji: {potan} ")
                print(f"Ekt(Öteleme Kinetik): {kinetikT} ")
                print(f"Ekr(Dönme Kinetik): {kinetikR}  ")
                print(f"Ektot(Toplam Kinetik): {kinetikToplam}")
        except ValueError:
            print("lütfen doğru bir değer giriniz")
        finally:
            deadoralive()
            
            
            
def table3(*args):
    global t
    while flag:
        try:
            s=float(input("Lütfen s değerini giriniz: "))
            t=float(input("Lütfen t değerini giriniz: "))
        except ValueError:
            print("Lütfen doğru dürüst hakkaniyetli bir değer giriniz: ")
        finally:
                hız2=float((m*g*t)/((m*math.pow(r,2)+momentTheo)/math.pow(r,2)))
                potan=float(m*g*s)
                kinetikT=float(0.5*m*math.pow(hız,2))
                kinetikR=float((0.5*momentTheo)*(math.pow(acisalhiz,2)))
                kinetikToplam=float(kinetikT+kinetikR)
                print(f"hızınızın değeri:  {hız2} ")
                print(f"potansiyel değeri: {potan} ")
                print(f"Ekt(öteleme kinetik) değeri: {kinetikT} ")
                print(f"Ekr(Dönme kinetik): {kinetikR} ")
                print(f"Ektot(Toplam kinetik): {kinetikToplam} ")
                
                deadoralive()

while flag:
    anamenu()