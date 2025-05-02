'''import calculate


def callfunc(num1,num2):
    # print(f'Add: {calculate.add(num1, num2)}, Sub: {calculate.sub(num1, num2)}, Mul: {calculate.mul(num1, num2)}, Div: {calculate.div(num1, num2)}')
    return (f'add:{calculate.add(num1, num2)}\nsub:{calculate.sub(num1, num2)}\nmul:{calculate.mul(num1, num2)}\ndiv:{calculate.div(num1, num2)}')
print(callfunc(10,5))
 
'''

import user
import admin


def function():
    user_name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    Admin_name = input("Enter your admin name: ")
    Admin_id = int(input("Enter your admin id: "))
    return f"User_details: {user_name}\nuser_Age: {age}\nAdmin_user:{Admin_name}\nAdmin_id:{Admin_id}"
print(function())