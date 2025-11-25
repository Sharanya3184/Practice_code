# Method 1: Slicing
s = "Sharanya"
rev = s[::-1]
print(rev)  # ayna rahS


# Method 2: Using reversed() and join()
s = "Sharanya"
rev = ''.join(reversed(s))
print(rev)




# 2. Remove Duplicates from Array/List
# Method 1: Using a loop (preserves order)
arr = [1, 2, 3, 2, 4, 1, 5]
unique_arr = []
for num in arr:
    if num not in unique_arr:
        unique_arr.append(num)
print(unique_arr)



# Method 2: Using set() (order may change)
arr = [1, 2, 3, 2, 4, 1, 5]
unique_arr = list(set(arr))
print(unique_arr)


#  Factorial
# Method 1: Using a loop
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print(fact)


# Method 2: Using recursion
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))



# Fibonacci Series
# Method 1: Using a loop
n = 7
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
    
    

# Method 2: Using recursion
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(7):
    print(fibonacci(i), end=" ")
    
    


# min and max without inbuilt function 


arr = [5, 2, 9, 1, 7, 6]

min_val = arr[0]
max_val = arr[0]

for num in arr:
    if num < min_val:
        min_val = num
    if num > max_val:
        max_val = num

print("Min:", min_val)
print("Max:", max_val)




# lambda function 

add = lambda x, y: x + y
print(add(2, 3))  # Output: 5


# Recursive function 

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))


# odd or even 

# Loop through a range of numbers (Python example)
# Check numbers from 1 to 10
for n in range(1, 11):
    if n % 2 == 0:
        print(f"{n} is Even")
    else:
        print(f"{n} is Odd")
        
        
# another method 

n = 7
if n % 2 == 0:
    print("Even")
else:
    print("Odd")


