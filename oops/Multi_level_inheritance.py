class Grandfather:
    def ownhouse(self):
        print("Grandfather owns a house.")

class Father(Grandfather):
    def owncar(self):
        print("Father owns a car.")

class Child(Father):
    def ownbike(self):
        print("Child owns a bike.")

obj=Child()
obj.ownhouse()
obj.owncar()
obj.ownbike()
