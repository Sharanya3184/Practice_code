class Student:
    name = "Sharan"
    age = 20

# Using getattr with default values
print(getattr(Student, "name", "Default Name"))
print(getattr(Student, "age", "Default Age"))
print(getattr(Student, "gender", "Default Gender"))

print(Student.age)

