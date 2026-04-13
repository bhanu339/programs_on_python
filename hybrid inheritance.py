class A:
    def display_A(self):
        print("I am from A")
class B(A):
    def display_B(self):
        print("I am from B")
class C(A):
    def display_C(self):
        print("I am from C")
class D(B,C):
    def display_D(self): 
        print("I am from D")
s=D()
s.display_A()
s.display_B() 
s.display_C()
s.display_D()
              
        
                        