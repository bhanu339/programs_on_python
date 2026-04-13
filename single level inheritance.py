class A:
    def display_A(self):
        print("I am parent")
class B(A):
    def display_B(self):
        print("I am child")
s = B()
s.display_A()
s.display_B()