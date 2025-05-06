from abc import ABC, abstractmethod

class Student(ABC):
    @abstractmethod
    def display_marks(self):
        pass

class BCAStudent(Student):
    def display_marks(self):
        print("BCA Student Marks: 85")

class BScStudent(Student):
    def display_marks(self):
        print("BSc Student Marks: 90")


bca = BCAStudent()
bsc = BScStudent()
bca.display_marks()  
bsc.display_marks()  
