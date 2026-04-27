class InvalidMarks(Exception):
    pass
Marks = int(input())
try:
    if Marks>100 or Marks<0:
        raise InvalidMarks("please enter numbers from 0 to 100")
    else:
        print("you enter marks are :",Marks)
except InvalidMarks as e:
    print("Error:",e)        