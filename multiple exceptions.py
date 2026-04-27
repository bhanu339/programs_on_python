try:
    a = int(input())
    b = int(input())
    c = a/b
    print(c)
except ZeroDivisionError:
    print("I can't divide")
except ValueError:
    print("Value Error")        