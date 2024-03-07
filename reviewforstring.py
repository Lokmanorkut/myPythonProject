message="hello there my name is sadik turan"

message=message.upper()
#tüm karakterleri büyük harf yapar
message=message.lower()
#küçük yapar

message=message.title()
#başlık tipi yazı

message=message.capitalize()
#sadece ilk harfi büyük yapar
message=message.strip()
#ilk boşluğu siler

message=message.split()
#boşluktan böler split adı üstünde 
#split(".") noktalardan ayırır
#"".join() ne eklemek istersen

message=message.find("sadık")
#bu sadığı arar ve 24. karakter itibaren -1 olmadığını söyler
#.startswith("ne ile başlıyor")
#.endswith
message=message.replace("sadık","çınar")
#adı üstünde yerine yazar
#for instanec mms.replace("ç","c") mesela türkçe karakterleri çeviri

message=message.center(50,12)


