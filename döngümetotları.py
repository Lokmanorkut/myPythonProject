#list=[1,2,3]
#
#for i in range(50,100,10):
#    print(i)    
#
#    

##enumaruate
#selam="hello there"
#
#for index,letter in enumerate(selam):
#    print(f"letter {{selam[index]}} index {index}")
#


list1=[1,24,5,212,]
list2=["a","c","g","adqd","1w12"]
list3=[100,1222,121212,1313131,13131]
print(list(zip(list1,list2,list3)))
for item in zip(list1,list2,list3):
    print(item)
    for a,b,c in zip(list1,list2,list3):
        print(a,b,c)