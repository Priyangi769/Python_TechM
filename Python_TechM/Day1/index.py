#value and data Types
'''Write a program that:
     - Assigns different values to variables.
     - Prints the type of each variable
'''
x = 42 
y = 3.14
z = 'Hello'
print(type(x), type(y), type(z)) # <class 'int'> <class 'float'> <class 'str'>

#Operators and Operands
''' Create a Python script that demonstrates:
     - Addition, subtraction, multiplication, and division.
     - Comparisons between numbers.
     - Logical operations like `and`, `or`, `not`.'''

a = 10
b = 3
print(a + b, a - b, a * b, a / b, a // b, a % b, a ** b) # 13 7 30 3.3333333333333335 3 1 1000
print(a > b, a < b, a == b, a != b) # True False False True
print(a > 5 and b < 5) # True

#Function Calls
'''Write a program that uses built-in functions inside expressions:'''

numbers = [5, 3, 8, 1]
print(max(numbers) - min(numbers)) # 7

'''Assign a function to a variable, then call the function using the new variable'''

greet = print
greet('Hello, World!') # Hello, World!

#Data Types
'''Create variables of different types and print their types'''

a = 10
b = 'Python'
c = 3.14
print(type(a), type(b), type(c))

#Type Conversion Functions
'''Convert variables between types and observe the results'''

num = '123'
converted_num = int(num) # 123
print(converted_num, type(converted_num)) # 123 <class 'int'>

#Variables
'''Assign values to variables, print them, and observe changes upon reassignment.'''

x = 5
print(x) # 5
x = 10
print(x)  # 10

#Variable Names and Keywords
'''Try using reserved keywords as variable names and observe the errors.'''

import keyword; 
print(keyword.kwlist) # ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

#Choosing the Right Variable Name
'''Rewrite a piece of code with meaningful variable names.'''

total_price = 100
discount = 0.2
final_price = total_price * (1 - discount)
print(final_price) # 80.0

#total_price is a better name than tp because it is descriptive and easy to understand.

#Statements and Expressions
'''Identify statements and expressions in this code'''

x = 5 + 3
print(x) # 8

#Order of Operations
'''Write expressions using multiple operators to explore Python’s order of operations.'''

result = 2 + 3 * 4 ** 2 / 8
print(result) # 8.0

#Reassignment

'''Assign a value to a variable, reassign it, and observe the changes'''
count = 10
print(count) # 10
count = 20
print(count)    # 20

'''Increment and decrement variables using `+=` and `-=`'''

score = 100
score += 10
print(score) # 110
score -= 5
print(score) # 105