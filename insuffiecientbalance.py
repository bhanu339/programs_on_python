class InsuffiecientBalance(Exception):
    pass
balance = 1000
amount = int(input())
try:
    if amount > balance:
        raise InsuffiecientBalance("sorry Insuffiecient Balance")
    else:
        balance  -= amount
        print("withdrawl success and remaining balance:",balance)
except InsuffiecientBalance as e:
    print("Error:",e)        