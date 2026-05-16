#function with no parameters
#greeting function
# Defining a function
def greet():
#defines a function named greet that takes no parameters and prints "Hello!" when called.
    print("Hello!")

# Calling (using) the function
greet()
#when we call greet, it runs the code inside the function, which prints "Hello!" to the console.

# Function with one parameter
# greeting function that takes a name as input
def greet(name):
    print("Hello,", name)

greet("Lalitha")
# This version of greet takes a parameter called name.
#here name is the parameter
#parameters are like input slots for functions. 

#function with multiple parameters
#add two numbers
def add(a, b):   # two input slots
    return a + b

print(add(2, 3))   # Output: 5
print(add(10, 7))  # Output: 17
#a and b are parameters that the add function takes. 

#square a number
def square(x):
    return x * x
print(square(4))  # Output: 16
print(square(7))  # Output: 49

#check even or odd
def check_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even(7))  # Output: Odd
print(check_even(10)) # Output: Even

#find the maximum of two numbers
def maximum(a, b):
    if a > b:
        return a
    else:
        return b

print(maximum(4, 9))  # Output: 9
print(maximum(15, 7)) # Output: 15

#double a number
def double(x):
    return x * 2

print(double(7))  # Output: 14
print(double(3.5))  # Output: 7.0

# Find area of a rectangle
def area(length, width):
    return length * width

print(area(5, 3))  # Output: 15
print(area(10, 4)) # Output: 40

# Convert Celsius to Fahrenheit
def temp(c,f):
    cf=(c * 9/5) +32
    fc=(f - 32) * 5/9
    return cf,fc
print(temp(25, 77))  # Output: (77.0, 25.0)
#seperate funcions for c to f and f to c
def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

print(c_to_f(25))   # 77.0
print(f_to_c(77))   # 25.0
#user interactive
choice = input("Convert (C)elsius or (F)ahrenheit? ").lower()

if choice == "c":
    c = float(input("Enter Celsius: "))
    print("Fahrenheit:", (c * 9/5) + 32)
elif choice == "f":
    f = float(input("Enter Fahrenheit: "))
    print("Celsius:", (f - 32) * 5/9)
else:
    print("Invalid choice! Please enter 'c' or 'f'.")

#mini calci using functions
entered_choice = input("Choose an operation: Add, Subtract, Multiply, Divide: ").lower()
def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b
if entered_choice == "add":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result:", add(num1, num2))
elif entered_choice == "subtract":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result:", subtract(num1, num2)) 
elif entered_choice == "multiply":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result:", multiply(num1, num2))
elif entered_choice == "divide":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result:", divide(num1, num2))
else:
    print("Invalid operation! Please choose Add, Subtract, Multiply, or Divide.")