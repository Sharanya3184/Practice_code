

import user
import admin


def function():
    user_name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    Admin_name = input("Enter your admin name: ")
    Admin_id = int(input("Enter your admin id: "))
    return f"User_details: {user_name}\nuser_Age: {age}\nAdmin_user:{Admin_name}\nAdmin_id:{Admin_id}"
print(function())