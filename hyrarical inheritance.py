
class A:
    def display_A(self):
        print("I am parent")
class B(A):
    def display_B(self):
        print("I am child")    
class C(A):
    def display_C(self):
        print("I am child")
s=C()
t=B()
s.display_A()
s.display_C()   
t.display_B()             