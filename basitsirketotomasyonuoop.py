import os
class Company:
    def __init__(self,ad):
        self.ad=ad
        self.calisma=True
    def program(self):
        while True:
            secim=self.menusecim()
            try:
                if secim==1:
                    self.calisanekle()
                elif secim==2:
                    self.calisanCikar()
                elif secim==3:
                    ayyılsecim=input("yıllık bazda görmek ister misiniz? (e/h)")
                    if ayyılsecim=="e":
                        self.verilecekmaasgoster(hesap="y")
                    else:
                        self.verilecekmaasgoster()
                elif secim==4:
                    self.maaslariVer()
                elif secim==5:
                    self.masrafgir()
                elif secim==6:
                    self.gelirgir()
                elif secim==7:
                    self.calisma=False
            except ValueError:
                print("Düzgün değer gir")
            
            
        
        
    if not os.path.isfile("butce.txt"):
        print("butce.txt geçerli dizinde bulunamıyor.Lütfen bütçenizi giriniz.")
        butceGiris=input("Bütçenizi giriniz: ")
        with open("butce.txt","w") as dosya:
            dosya.write(butceGiris)
        print("butce.txt Başarıyla oluşturuldu")
            
    
    def menusecim(self):
        secim=int(input(f"*** {self.ad} Otomasyonuna Hoş Geldiniz***\n\n1-Çalışan Ekle\n2-Çalışan Çıkar\n3-Verilecek Maaş Göster\n4-Maaşları Ver\n5-Masraf Gir\n6-Gelir Gir\n7-Programdan Çıkmak için 7\n\nSeçiminizi Giriniz: "))
        while secim<1 and secim>6:
            secim=int(input("Liütfen 1-6 arasında belirtilenler arasında bir sayı giriniz"))
        return secim
    
    def calisanekle(self):
        id=1
        ad=input("Çalışanın Adını giriniz: ")
        soyad=input("Çalışanın Soyadını giriniz: ")
        yas=input("Çalışanın Yaşını giriniz: ")
        cinsiyet=input("Çalışanın Cinsiyetini giriniz: ")
        maas=input("Çalışanın Maaşını giriniz: ")
        
        if not os.path.isfile("calisanlar.txt"):
            with open("calisanlar.txt","w") as dosya:
                pass
        
        with open("calisanlar.txt","r") as dosya:
            calisanlistesi=dosya.readlines()
        if len(calisanlistesi)==0:
            id=1
        else:
            id = int(calisanlistesi[-1].split(")")[0]) + 1
            
        with open("calisanlar.txt","r") as dosya:
            calisanlar=dosya.readlines()
        
        with open("calisanlar.txt","a") as dosya:
            dosya.write(f'{id}){ad}-{soyad}-{yas}-{cinsiyet}-{maas}\n')
            
        print(calisanlar)

    def calisanCikar(self):
        if not os.path.isfile("calisanlar.txt"):
            with open("calisanlar.txt","w") as dosya:
                pass
            
            
        with open("calisanlar.txt","r") as dosya:
            calisanlar=dosya.readlines()
            
        gcalisanlar=[]
            
        for calisan in calisanlar:
            gcalisanlar.append("".join(calisan[:-1]).split("-"))
            
        for workers in gcalisanlar:
            print(workers)
            
        if len(calisanlar) == 0:
            print("Çalışan yok!")
            return
            
        secim=int(input(f"Lütfen Çıkarmak istediğiniz çalışanın numarasını giriniz(1-{len(gcalisanlar)}): "))
        if secim < 1 or secim > len(gcalisanlar):
            print(f"Lütfen 1-{len(gcalisanlar)} arasında bir sayı giriniz.")
            return
        
        calisanlar.pop(secim-1)
        sayac=1
        
        dcalisanlar=[]
        
        for calisan in calisanlar:
            dcalisanlar.append(str(sayac) + ")" + calisan.split(")")[1]) 
            sayac+=1
            
        with open("calisanlar.txt","w") as dosya:
            dosya.writelines(dcalisanlar)

    
    def verilecekmaasgoster(self,hesap="a"): 
    #"""hesap:a ise aylık,y ise yıllık hesap"""
        with open("calisanlar.txt","r") as dosya:
            calisanlar=dosya.readlines()
            
            maaslar=[]
            
            for calisan in calisanlar:
                maaslar.append(int(calisan.split("-")[-1]))
            if hesap=="a":
                print(f"bu ay toplam vermeniz gereken maaş {sum(maaslar)}")
            else:
                print(f"bu yıl toplam vermeniz gereken maaş {sum(maaslar)*12}")
            
            
            
    
    
    def maaslariVer(self):
        with open("calisanlar.txt","r") as dosya:
            calisanlar=dosya.readlines()
            
        maaslar=[]
        
        for calisan in calisanlar:
            maaslar.append(int(calisan.split("-")[-1]))
        
        toplamMayıs=sum(maaslar)
        ###Bütceden maaş alma #####
        
        with open("butce.txt","r") as dosya:
            tbutce=int(dosya.readlines()[0])
            
            tbutce=tbutce-toplamMayıs
            
        with open("butce.txt","w") as dosya:
            dosya.write(str(tbutce))
        
        with open("butce.txt","r") as dosya:
            sonbutce=(int(dosya.readlines()[0]))
        print(f"{self.ad} Şirketinizin kalan bütcesi {sonbutce}")
            
    
    
    
    def masrafgir(self):
        masraflar=[]
        while True:
            masraf=input("Masraf giriniz (eğer masraf girmek istemiyorsanız ENTER tuşuna basınız): ")
            if not masraf:
                break
            try:
                masraf=int(masraf)
                masraflar.append(masraf)
            except ValueError:
                print("Geçersiz kullanım sayı gir lo")
            
        toplamMasraf=sum(masraflar)
        with open("butce.txt","r") as dosya:
            tbutce=int(dosya.readlines()[0])
            
            tbutce=tbutce-toplamMasraf
            
        with open("butce.txt","w") as dosya:
            dosya.write(str(tbutce))
            
        with open("butce.txt","r") as dosya:
            sonbutce=(int(dosya.readlines()[0]))
        print(f"Girdiğiniz Masraf {toplamMasraf}")
        print(f"{self.ad} Şirketinizin kalan butcesi {sonbutce}")  
        
              
    def gelirgir(self):
        gelirler=[]
        while True:
            gelir=input("Gelir giriniz (eğer Gelir girmek istemiyorsanız ENTER tuşuna basınız): ")
            if not gelir:
                break
            try:
                gelir=int(gelir)
                gelirler.append(gelir)
            except ValueError:
                print("Geçersiz kullanım sayı gir lo")
            
        toplamGelir=sum(gelirler)
        with open("butce.txt","r") as dosya:
            tbutce=int(dosya.readlines()[0])
            
            tbutce=tbutce+toplamGelir
            
        with open("butce.txt","w") as dosya:
            dosya.write(str(tbutce))
            
        with open("butce.txt","r") as dosya:
            sonbutce=(int(dosya.readlines()[0]))
        print(f"Girdiğiniz Gelir {toplamGelir}")
        print(f"{self.ad} Şirketinizin kalan butcesi {sonbutce}")        
  
ad=input("Şirketinizin adını giriniz: ")    
Company=Company(ad)

while Company.calisma:
    Company.program()
    
    