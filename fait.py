while True:
    try:
        x = int(input("Please enter a number: "))
        y=10/x
        a=input("sayı gir print aaa")
        print(a+5)
        break
    except (ValueError,ZeroDivisionError,TypeError):
        print("please")
        