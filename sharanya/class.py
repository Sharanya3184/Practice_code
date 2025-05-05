class College:
    def __init__(self):
       
        self.student = Student()

       
        self.student.details()


class Student:
    def details(self):
        print("🙋‍♀️ Hello! I am a student of Auxilium College.")
college_obj = College()
