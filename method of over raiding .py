class A:
    def show(self):
        print("I am from parent class")
class B(A):
    def show(self):
        print("I am from child class")
s=A()
s.show()                    