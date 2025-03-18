# Variables, Statements, and Expressions
**Variables** -- Symbolic names that act as containers for storing data values.<br>
**Statements** -- A line of code that the interpreter executes, performing a specific action, such as assigning a value, making a decision, or executing a loop.**ex.--** x = 5,for, while.<br> 
**Expressions** -- A combination of operators and operands that is interpreted to produce some other value.**ex.--** x = 15 + 1.3<br>

# Value and DataTypes in Python
## Value
-A value is one basic things in any program works with,such as a number, text, or boolean.
    
## Data Types
1. **Integer(int)** -- value is represented by int class.It contains positive or negative whole numbers. No limit for how long the integer value can be.(e.g., 42, -7)<br>
2. **Float(float)**: It is a real number with a floating-point representation.Decimal numbers (e.g., 3.14, -2.5).<br>
3. **String (str)**:Represented by str class. Text values (e.g., 'Hello').<br>
4. **Boolean (bool)**:Boolean objects that are equal to True are truthy (true), and those equal to False are falsy (false).True/False values (True, False).<br>

# Operators and Operands
## Operators
-These are the special symbols.<br>**eg.-** + , * , /, etc.
1. **Arithmatic Operators** --  perform basic mathematical operations like addition, subtraction, multiplication and division.+, -, *, /, //, %, **<br>
2. **Comparison Operators** -- It either returns True or False according to the condition.==, !=, >, <, >=, <=<br>
3. **Logical Operators** --  used to combine conditional statements, allowing you to perform operations based on multiple conditions.and, or, not<br>
## Operands 
    -The values or variables on which an operator performs an action.<br>

# Function Calls
**Fun Fact:**
   - In Python, functions are first-class objects, meaning they can be assigned to variables and passed as arguments.<br>

## Type Conversion Functions
**Fun Fact:**
   - Python provides built-in functions like `int()`, `float()`, and `str()` to handle type conversions.<br>
 -- Python defines type conversion functions to directly convert one data type to another.<br>
 1. **Implicit Type Conversion** -- The Python interpreter automatically converts one data type to another without any user involvement.<br>

 2. **Explicit Type Conversion** -- The data type is manually changed by the user as per their requirement.
 <br>

 ## Variables
 -- They are stored directly on the stack. When the function is called, the local variable result is also stored on the stack.

## Variable Names and Keywords
-- Keywords are reserved words with specific meanings, while variables are named storage locations that hold data values.<br>

## Statements and Expressions

**Statements**                                  
A complete instruction that performs an action. 
Returns a Value.                                 
*Example*--5 + 3, max(4, 7), x * 2               
Can be part of a statement.                      

**Expression**<br>
A combination of values and operators that produces a result.<br>
Does not return a value.<br>
*Example*-- x = 5 + 3, print(x), if x > 5:<br>
Cannot be used where a value is expected.<br>