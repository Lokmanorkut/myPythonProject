# # # # # # # # # #dosya açmak ve oluşturmak için open() fonksiyonu kullanılır open(dosyaadı,dosya erişme moud)
# # # # # # # # # # "w" yazma oluşturma
# # # # # # # # # #"a" ekleme 
# # # # # # # # # #"x" dosya ztn varsa hata verir
# # # # # # # # # #"r" okuma yoksa hata verir
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # #file=open("newfile.txt","w")
# # # # # # # # # #file.close()
# # # # # # # # # #

# # # # # # # # # #file=open("C:/users/Lokman/desktop/newfile.txt","w",encoding="utf-8")
# # # # # # # # # #file.write(" ")
# # # # # # # # # #file.close(  )
# # # # # # # # # #

# # # # # # # try:
# # # # # # #      file=open("newfile.txt3","r",encoding="utf-8")
# # # # # # #      print(file)
# # # # # # # except NameError:
# # # # # # #      print("dosya okuma hatası")
# # # # # # # finally:
# # # # # # #      file.close()


# # # # # # for i in file:
# # # # # #     print(i, end="")
    
# # # # # # file.close()
# # # #read fonksiyonu

# # # content1=file.read()
# # # print("içerik 1 ")
# # # print(content1)
# # # content2=file.read()
# # # print("içerik 2")
# # # print(content2)
# # # file.close()

# # # content=file.read(5)
# # # content=file.read(6)
# # # print(content)
# # # file.close() 
# # #print(file.readline())
# # # readline
# # #
# # #file.close()"
# # # with open("newfile.txt","r",encoding="utf-8") as file:
# # #     icerik=file.read(25)
# # #     print(icerik)
# # #     file.seek(25)#imleci () konuma gönderir gönderir 
# # #     print(file.tell())


# # # with open("newfile.txt","r+",encoding="utf-8") as file:
# # #     file.seek(25)
# # #     file.write("deneme-")

# # # with open("newfile.txt","r",encoding="utf-8") as file:
# # #     print(file.read())
    

# # with open("newfile.txt","a",encoding="utf-8") as file:
# #     file.write("\n Emel turan")
    
# # with open("newfile.txt","r",encoding="utf-8") as file:
# #     file.read()

            
# with open("newfile.txt","r+",encoding="utf-8") as file:
#     liste=file.readlines()
#     liste.insert(1,"ali veli 49 59")
#     file.seek(0)
#     file.writelines(liste)

# with open("newfile.txt","r+",encoding="utf-8") as file:
#     print(file.read())

#### Bİtirme projesi #####
def nothesapla(satir):
    satir=satir[:-1]
    liste=satir.split(":")
    ogrenciAdı=liste[0]
    notlar=liste[1].split(",")
    
    not1=int(notlar[0])
    not2=int(notlar[1])
    not3=int(notlar[2])
    
    Ortalama=(not1+not2+not3)/3
    
    if Ortalama>=90 and Ortalama<=100:
        harf="AA"
    elif Ortalama>=85 and Ortalama<=89:
        harf="BA"
    elif Ortalama>=65:
        harf="CC"
    else:
        harf="FF"
        
    return ogrenciAdı+ ":" + harf + "\n"
    



def ortalamalariOku():
    with open("sınavnotları.txt","r",encoding="utf-8") as file:
        for satir in file:
           print(nothesapla(satir))
        
def notGir():
    ad=input("öğrenci adı: ")
    soyad=input("öğrenci soyadı: ")
    not1=input("öğrenci not1:")
    not2=input("öğrenci not2:")
    not3=input("öğrenci adı: ")
    with open("sınavnotları.txt","a",encoding="utf-8") as file:
        file.write(ad+" "+soyad+":"+not1+","+not2+","+not3+"\n")
        
def notlarıKayıtet():
    with open("sınavnotları.txt","r",encoding="utf-8") as file:
        liste=[]
        
        for c in file:
            liste.append(nothesapla(c))
            
            with open("sonuclar.txt","w",encoding="utf-8") as file2:
                for i in liste:
                    file2.write(i)
                    
                    
                    
            
        



while True:
    islem=input("1-notları oku\n2-Not gir\n3-Notları kayıt et\n4-Çıkış: ")

    if islem=="1":
        ortalamalariOku()
    elif islem=="2":
        notGir()
    elif islem=="3":
        notlarıKayıtet()
    else:
        break  
    
    
    len