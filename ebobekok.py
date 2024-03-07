x = int(input("Birinci sayıyı girin: "))
y = int(input("İkinci sayıyı girin: "))

ebob_listesi = []

for i in range(1, min(x, y) + 1):
    if x % i == 0 and y % i == 0:
        ebob_listesi.append(i)

ebob_listesi.sort()

# En büyük ortak bölen (EBOB), listenin son elemanıdır.
ebob = ebob_listesi[-1]

print(f"{x} ve {y} sayılarının EBOB'u: {ebob}")
