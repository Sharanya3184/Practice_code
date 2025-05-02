# import keyword
# print(keyword.kwlist)


# #input statement
# name=input()
# print("Enter you name:", name)

# a=10
# b=20
# c=a+b
# print(c)
# print(id(a))                                                            # basic syntax


# name1 , name2, name3=input("Enter 3 Names:").split()
# print("name1:", name1)
# print("name2:", name2)
# print("name3:", name3)                                                  #string split function


# para=[]
# print("enter the value:")
# while True:
#     line=input()
#     if line:
#         para.append(line)
#     else:
#         break                                                              #entering multiple value in input

#
# a1=43
# b1=0.23
# c1="String"
# print(type(a1))
# print(type(b1))
# print(type(c1))                                                            #data type example
# print(float(a1))                                                           # type casting


# String function
#
# s = " Sharan "
# print(s)
# print("Type of:", type(s))
# print("Upper:", s.upper())
# print("Lower:", s.lower())
# print("Capitalize:", s.capitalize())
# print("Title:", s.title())
# print("Count :", s.count("s"))
# print("Endswith:", s.endswith("s"))
# print("Find the words:", s.find("S"))
# print("Replace:", s.replace("a","o"))
# print("Is upper:", s.isupper())
# print("Is Alpha numeric:", s.isalnum())
# print("Is Alphabet:", s.isalpha())
#
# s1="she\nis\n sony"                                                         #split using list
# print(s1)
# print("Splitlines", s1.splitlines())
# print("Splitlines", s1.splitlines(True))
#
# s2="sharan studying BCA"
# print("Split:",s2.split(" "))
# print("Split:",s2.split(", "))
#
#
# s3="         sharan      "
# print("length of S3:", len(s3))
# print("count of the value :", len(s3.strip()))
# print("count of the left strip value :", len(s3.lstrip()))
# print("count of the right strip value :", len(s3.rstrip()))
#
#
# s4="27-03-2025"
# print(s4.partition("-"))
#
#
# #String Manipulation
#
#
# s5="Sample"
# print(s5)
# print("String1:", s5[0:3])
# print("String2:",s5[0:5])
# print("String3:", s5[-1])
# print("Reverse the string:", s5[::-1])


# Arithmetic operators

"""
+ Addition
- Subtraction
* Multiplication
/ Division
% Modulus (To get the Remainder as an output)
//Floor Division(It is used to convert the divided value
                 in decimal no into whole number0.89 to 89)
** Exponentiation (2 power of 2 can be done as here )
"""


# a2 = 10
# b2 = 13
# print("Add:", a2 + b2)
# print("Sub:", a2 - b2)
# print("Divide:", a2 / b2)
# print("Multiple:", a2 * b2)
# print("Modulus:", a2 % b2)
# print("Floor division:", a2 // b2)
# print("Exponentiation:", a2 ** b2)

# Assignment Operators

# c = 23
# print(c)
# c += 4     #c=c+4
# print(c)
# c-=4       #c=c-4
# print(c)
# c/=3       #c=c/4
# print(c)
# c%=3       #c=c%3
# print(c)


'''Comparison operators
== Equal to
!= not equal to 
>  Greater than
<  lesser than
>= Greater than or equal to 
<= lesser than or equal to 

'''

g = 4
f = 10
# if g==f:
#     print("true")
# else:
#     print("not true")
#
#          #or#
#
# print(g==f)
# print(g!=f)
# print(g > f)
# print(g>=f)
# print(g<f)
# print(g<=f)

'''Logical operators
and (like multiplication)
or  (like addition)
not (like opposite answer)
'''
# if f<=20 and g>2:
#     print("true")
# else:
#     print("not true")
#
#     #Or#
#
# print(f<=20 and g<=2)
# print(not (f<=20 and g<=2))


'''Bitwise Operators
     It converts the given value as 1s and 0s 
     then using the bit value like 4(100), 5(101) 
     if it is and it will be like multiple, for like 
     add and it convert the binary value into numbers
     then gives the o/p.
& and 
| or
^ Xor (same means 0 different means 1)
~ not
<< Zero fill left shift (represent in 8bit and add 
                3 zero in front of the binary value and find
                the o/p)
>> Signed right shift  (same as left shift but move from back
                side and get the o/p)
'''

# print(f & g)
# print(f | g)
# print(f ^ g)
# print(~f)
# print(f >> 2)
# print(f << 2)


# If statement

'''write a program for check the given no  is even'''
#
# n = int(input("Enter the value:"))
# if n % 2 == 0:
#     print("The entered value", n, "is an Even number")
# else:
#     print("The entered value", n, "is an odd number")


# If-else and elif statement

'''write a program to check vote eligibility by enter name and age'''
#
# name = input("Enter the name:")
# age = int(input("Enter your age:"))
# if age <= 17:
#     print(name, "you are not eligible for vote")
# elif age >= 18:
#     print(name, "you are eligible for vote")
# else:
#     print("Better luck next time")
#


# elif statement
'''write a program for library book return
1-5   days 0.5 fine amount
5-18  days 1.0 fine
18-38 days 5.0 fine
>38   Membership cancel'''

# days = int(input("Enter your days:"))
# if days == 0:
#     print("No fine")
# elif days >= 1 and days <= 5:
#     print("your fine amount is 0.5")
# elif days >= 5 and days <= 18:
#     print("your fine amount is 1")
# elif days >= 18 and days <= 38:
#     print("your fine amount is 5")
# else:
#     print("Your membership cancelled")

'''Nested if statement
3 Marks as input 
Total
Average
Result
If pass grade 
 98-100 A
 88-89  B
 70-79  C
 else   D
 '''
#
# mark1 = int(input("Enter the value1:"))
# mark2 = int(input("Enter the value2:"))
# mark3 = int(input("Enter the value3:"))
# total = mark1 + mark2 + mark3
# print("Total marks are:", total)
# average = total / 3
# print("The average value is :", average)
# if mark1 >= 35 and mark2 >= 35 and mark3 >= 35:
#     print("Result:Pass")
#     if average <= 98 and average >= 100:
#         print("Result: Grade A")
#     elif average <= 88 and average <= 89:
#         print("Result: Grade B")
#     elif average <= 70 and average <= 79:
#         print("Result: Grade C")
#     else:
#         print("You are fail")
#           print("Grade: No Grade")


'''Looping statement
'''
# While loop
# i=1
# while i<=10:
#     print(i)
#     i+=1
#
# #To print the even no through while loop
#
# print("___________________")
# n=29
# i=2
# while i<=29:
#     print(i)
#     i+=2
# print("___________________")
#
# #To print the odd no through while loop
# n=30
# i=3
# while i<=30:
#     print(i)
#     i+=3

'''Continue statement'''
#
# i=1
# while i<=20:
#     if i%2==0:
#        i+=1
#        continue
#     print(i)
#     i+=1

'''Break statement'''

# i = 1
# while i <= 20:
#     if i == 7:
#         break
#     print(i)
#     i += 1


'''Range(range gives the o/p as n-1 example(6-1)=5 function only will execute'''

# print(list(range(5)))
# print(list(range(0, 20, 2)))  # n-1 for even no in range
# print(list(range(0, 20, 3)))  # n+1 for odd no
#
# ''''for loop in range'''
#
# for i in range(20):
#     print(i)

'''execute a loop for 5 times'''
#
# for i in range(5):
#     r = int(input("Enter a number:"))
#     r1 = int(input("Enter a number:"))
#     print(r + r1)


'''print the symbol in loop 
*
**
***
****
*****'''

# for i in range(6):
#     for j in range(i):
#         print("*",end="")
#     print("")
#

# reverse the symbol in loop
#
# for i in range(20, 0, -1):
#     for j in range(i):
#         print("*", end="")
#     print("")

# number to character using for loop
# ABCDE
# ABCDE
# ABCDE
# ABCDE
# ABCDE

#
# for i in range(65,70,1):
#     for j in range(65,70,1):
#         print(chr(j), end="")
#     print("")


'''list[](Indexing, ordered, Mutable, duplicate)'''
#
# l = [1, 2, 3, 4, 5, 6, 6, 6]
# print(l)
# print(type(l))
# print(l[1])
# print("List sciling:", l[0:3])
# print("Reverse the list:", l[::-1])
#
# # List accept all the datatype in single list
# l1 = [1, True, "Sharan", 2.5]
# print(l1)

# in-built functions of list

# b = l.copy()
# print("Values:", l)
# print("Count of the values:", l.count(6))
# print("Index of the value:", l.index(6))
# print("Length of the value:", len(l))
# print("minimum value:", min(l))
# print("maximum value:", max(l))
# print(l)
# l.pop(3)  # remove the elements using the index
# print("Pop the value:", l)
# l.remove(3)  # remove based on value
# print("Remove:", l)
# l.append("sharan")
# print("Append:", l)
# l2 = ["sharan", "Sony"]
# l.extend(l2)
# print("Extend:", l)
# l.insert(0,"sri")
# print("Insert:",l)
# print(list(range(5)))
# print(list("Sharan"))
# l2.sort()
# print("Ascending order sorting:",l2)
# l2.sort(reverse=True)
# print("Descending order sorting:",l2)
# l.clear()
# print("Clear the list:", l)


'''Tuple()(Indexing, Ordered, Duplicate)
same as list but it cannot be mutable use only delete function'''
# m = (1, 2, 3, 4, 5, 6, 2, 4, 8)
# print("Tuple:", m)
#
# for i in m:
#     print(i)
#     if 1 in m:
#         print("The number is there")
#     else:
#         print("Noo")
# print(len(m))
#
# m1 = ("Sony",)* 10
# print("Repeatation in tuple:", m1)


'''set{}(Unordered, unindexing)'''

# s = {'Sony', 'Mango', 'Sharan'}
# print("Set values:", s)
# print(type(s))
#
# for names in s:
#     print("Access values using for loop:", names)
#
# s1 = {'Ram', 'sam', 'ravi', "Sony"}
# s1.discard("sam")  # if it's there it will remove or execute the value
# print("Discard:", s1)
# s1.pop()
# print("pop value:", s1)
#
# s3 = {1, 2, 3, 4, 5}
# s4 = {5, 7, 8, 9, 10, 12}
# c = s3.intersection(s4)
# print(c)
# s3.intersection_update(s4)
# print(s3)
#
# c1 = s3.symmetric_difference(s4)
# print(c1)
# s3.symmetric_difference_update(s4)
# print(s3)

'''Dictionary{key and values}'''
#
# User={
#     "name": "Ram",
#     "age" :  24,
#     "isMarried" :True
# }
#
# print(User)
# print(User["name"])
# print(User.get("age"))
# print(User.values())
# print(User.keys())
# print(User.items())
#
# #Nested dictionary
#
#
User = {
    "user1": {
        "name": "Ram",
        "age": 24,
        "isMarried": True
    },
    "user2": {
        "name": "Sharan",
        "age": 20,
        "isMarried": True
    }
}

# print(User)
print(User["user1"]["name"])

'''Identity operator,Membership operator'''
#
# i=[1,2]
# i1=[1,2]
# print(i in i1)
# print(i not in i1)
# print(i is i1)
# print(i is not i1)


'''Function'''

#
# def sharan():
#     print("welcome to sharan coding ")
#
#
# sharan()
#
'''No return without argument'''
# def add():
#     a=int(input("Enter the value of:"))
#     b = int(input("Enter the value of:"))
#     c=a+b
#     print("Total:",c)
# add()


'''  No return with argument'''
# def add(a,b):
#     c=a-b
#     print(c)
#
# add(4,2)


''' return without argument'''
# def add():
#     a=int(input("Enter the value of:"))
#     b = int(input("Enter the value of:"))
#     c=a+b
#     return c
# # x=add()
# # print("add:",x)  #OR we can use this method
# print(add())


'''return with argument'''
# def add(a,b):      #Argument
#     c=a+b
#     return c
# x=add()
# print("add:",x)  #OR we can use this method
# print(add(5,5))                             #parameter

'''Arbitrary function (*)[We can pass the multiple value in single function) '''

#
# def class_10(*students):
#     print(students)
#
#
# class_10("Sharan", "Sony", "Sai", "Shanti", "Dinesh", "Archana")


'''Keyword Argument function'''
#
# def message(name,age):
#     print(name,"Age is :",age)
# message(name="Ram",age=25)  #using this key name and age we can be able to access the value.


'''Arbitrary keyword Argument'''
#
# def class_10(**student):
#     print(student)
# class_10(name="Sharan",Age=20, Gender="Female")


'''Default parameter function'''

# def user(name, city="Hyderabad"):
#     print(name, "is from ", city)
#
#
# user(name="sharan", city="chennai")
# user(name="sharanya")

'''passing list as an argument'''

# def function(marks):
#     return sum(marks)
#
#
# print(function([10, 20, 30, 40, 59, 2930, 23940, 2347]))

'''Recursive function[ it will call by itself to complete a work] '''

#
# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return x * factorial(x - 1)
#
# print(factorial(2))
'''execution understand the processes

x(5)*factorial (x-1)=5-1=4

5=factorial(4)
5=4*factorial(3)
5=4*3 factorial(2)
5=4*3*2factorial(1)'''

'''pass             #it will execute without defining the values'''

''''Lambda function[anonymous function]'''

# c=lambda a:a+50
# print(c(5))


