#for x in range(11):
#    print(x)

numbers=[x for x in range(11)]

for x in range(10):
    print(x**2)
numbers=[x**2 for x in range(11) if x%3==0]
print(numbers)

mystri="hello"
myli=[]
myli=[letter for letter in mystri]

year=[1992,1994,1912,2012]

ages=[2019-year for year in year]
print(ages)
#[işlem for i in nereden alacağın ]

result=[x if x%2==0 else "tek" for x in range(1,10)]
print(result)

result=[]
#kartezyen çarpım
for x in range(3):
    for y in range(3):
        result.append((x,y))
print(result)

numbers=[(x,y) for x in range(3) for y in range(3)]
print(numbers)