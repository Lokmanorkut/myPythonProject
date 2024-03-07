#random modülü kullanımı

import random 

#result=random.  
#result=random.  
#result=random.  
#result=random.  
#result=random.  
#result=random.  
#result=random.rand  
result=int(random.uniform(1,10))  
names=["ali","Yagmur","Deniz","cenk","ahmet"]
liste=list(range(10))
random.shuffle(liste)
result=names[random.randint(0,len(names)-1)]
result=random.choice(names)



liste=(range(100))
result=random.sample(liste,3)
result=random.sample(names,2)
print(result)