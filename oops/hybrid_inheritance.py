
class A:
    def display_a(self):
        print("This is class A")


class B(A):
    def display_b(self):
        print("This is class B")


class C(A):
    def display_c(self):
        print("This is class C")
        

class D(B, C):
    def display_d(self):
        print("This is class D")


obj = D()
obj.display_a()
obj.display_b()
obj.display_c()
obj.display_d()
