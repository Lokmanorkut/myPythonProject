#def squ(num): return num**2
numbers=[1,3,5,8]
result=list(map(lambda num:num**2,numbers))
print(result)

square=lambda num:num**2

def che(num): return num%2==0

list(filter(che,numbers))