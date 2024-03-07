def greeting(name):
    print("hello",name)
    
#print(greeting("ali"))
#print(greeting)


def outer(num1):
    print(outer)
    def inner_increment(num1):
        return num1+1