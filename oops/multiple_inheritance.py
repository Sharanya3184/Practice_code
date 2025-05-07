class Father:
    def __init__(self):
        self.father_name = "Somu"
        self.father_age = 43

    def fishing(self):
        return "He knows fishing"


class Mother:
    def __init__(self):
        self.mother_name = "Kavitha"
        self.mother_age = 39

    def cooking(self):
        return "She knows cooking"

    def chess(self):
        return "She knows chess"


class Child(Father, Mother):

    def details_info(self, father_name, mother_name):
        father_info=self.father_name,self.father_age
        mother_info=self.mother_name,self.mother_age
        return (f"Father: {self.father_name}, Age: {self.father_age}\n"
                f"Mother: {self.mother_name}, Age: {self.mother_age}")


    def details(self):
        fishing_info = self.fishing()
        cooking_info = self.cooking()
        chess_info = self.chess()
        return (f"Fishing: {self.fishing()}\n"
                f"Cooking: {self.cooking()}\n"
                f"Chess: {self.chess()}")
        

obj = Child()
obj.details_info()
obj.details()
print(obj.details())
# print(obj.cooking())
# print(obj.chess())
