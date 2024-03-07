def bitodec(bin):
    onluk=0
    us=0
    while bin>0:
        basamak=bin % 10
        onluk+=basamak*(2**us)
        binary //=10
        us+=1
    return onluk

def dectobi(onluk):
    bin=[]
    while onluk>0:
        kalan=onluk%2
        bin.append(str(kalan))
        onluk//=2
    bin.reverse()
    return "".join(bin) if bin else "0"


tercih = int(input("1- 2'lik Sayı Sisteminden Onluk Sayı Sistemine Çevirme:\n2- Onluk Sayı Sisteminden 2'lik Sayı Sistemine Çevirme:\nHangisini tercih ediyorsunuz: "))

if tercih == 1:
    binary_number = int(input("2'lik sayı sisteminden onluk sayı sistemine çevirmek için bir sayı girin: "))
    decimal_result = bitodec(binary_number)
    print(f"Sonuç: {decimal_result}")
elif tercih == 2:
    decimal_number = int(input("Onluk sayı sisteminden 2'lik sayı sistemine çevirmek için bir sayı girin: "))
    binary_result = dectobi(decimal_number)
    print(f"Sonuç: {binary_result}")
else:
    print("Geçersiz tercih! Lütfen 1 veya 2 seçeneğini girin.")

        
        

        
        
        
        
        
        
        