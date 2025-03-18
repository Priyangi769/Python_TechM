## Advanced Debugging Assignment

### 1. Error Classification
```python
# Fixed for loop
for i in range(5):
    print(i)

# Fixed division by zero error
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")

# Fixed calculate_area function
import math
def calculate_area(radius):
    return math.pi * radius * radius
```


### 2. Debugging Complex Functions
```python
def process_data(data):
    total = 0
    count = 0
    
    for item in data:
        try:
            total += int(item)
            count += 1
        except ValueError:
            print(f"Skipping invalid value: {item}")

    if count == 0:
        return 0  # To avoid division by zero
    
    return total / count

print(process_data(['10', '20', 'abc', '30']))
```


### 3. Advanced Debugging Challenge
```python
import random

def unreliable_function():
    number = random.choice([1, 2])  # Avoid 0 completely
    return 10 / number

for i in range(10):
    print(unreliable_function())
```


### 4. Writing Debug-Friendly Code
```python
def calculate_discount(price, discount):
    # Error handling: Check if price is a positive number
    if not isinstance(price, (int, float)) or price <= 0:
        raise ValueError("Price must be a positive number.")
    
    # Error handling: Check if discount is a valid number or a string with a '%' symbol
    if isinstance(discount, str):
        if discount.endswith('%'):
            try:
                discount = float(discount.strip('%'))  # Remove '%' and convert to float
            except ValueError:
                raise ValueError("Discount percentage must be a valid number.")
        else:
            raise ValueError("Discount should be a valid number or percentage string (e.g., '10%').")
    
    # Error handling: Ensure discount is a valid number
    if not isinstance(discount, (int, float)):
        raise ValueError("Discount must be a number.")

    # Calculate the discounted price
    discounted_price = price - (price * discount / 100)
    
    return discounted_price

# Test the function
try:
    print(calculate_discount(100, '10%'))  # Should work
    print(calculate_discount(100, 10))     # Should work
    print(calculate_discount(-100, '10%')) # Should raise an error
    print(calculate_discount(100, 'abc'))  # Should raise an error
except ValueError as e:
    print(f"Error: {e}")
```

### 5. Rubber Duck Debugging

Explain the following code snippet step-by-step as if you’re teaching someone unfamiliar with coding:

```python
numbers = [1, 2, 3, 4, 5]
result = 1
for num in numbers:
    result *= num
print("Product:", result)
```
*Create a list of numbers 
```python
numbers = [1, 2, 3, 4, 5]
```
*Initialize the result variable
```python
result = 1
```
*Loop through each number in list
```python
for num in numbers:
```
*Multiple the current result by current num 
```python
    result *= num
```
*Print the final product
```python
print("Product:", result)
```

### 6. Advanced Challenge: Debug a Multi-threaded Program
```python
import threading
counter = 0
counter_lock = threading.Lock()  # Create a lock to protect the counter

def increment():
    global counter
    for _ in range(100000):
        with counter_lock:  # Acquire the lock before modifying the counter
            counter += 1

threads = [threading.Thread(target=increment) for _ in range(2)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print("Counter:", counter)  # Expected: 200000
```


### 7. Activity: Debug with Breakpoints

Learn to use breakpoints in your IDE (e.g., VSCode, PyCharm) to inspect variable states step-by-step.

**Steps:**

1. Open your IDE and load the following code:

```python
def divide(a, b):
    result = a / b
    return result

a = 10
b = 0
print(divide(a, b))
```
# Fixed the division by zero error 
```python
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero"
    return result

a = 10
b = 0
print(divide(a, b))
```

2. Set a breakpoint at the line where `result` is calculated.
3. Run the code in debug mode.
4. Inspect the values of `a` and `b` before the division.
5. Step through the code to observe the flow of execution.
6. Fix the division by zero error and re-run the code.

#### Learn More:

- [VSCode Debugging Guide](https://code.visualstudio.com/docs/editor/debugging)
- [PyCharm Debugger](https://www.jetbrains.com/help/pycharm/debugging-your-first-python-application.html)

### 8. Memory Leaks and Performance Debugging
```python
def optimized_function():
    # Use a list comprehension to generate the result efficiently
    return [i * 2 for i in range(100000)]

# Call the optimized function and print the length of the result
result = optimized_function()
print(len(result))
```

### 9. Unexpected None

Debug why the function returns `None`:

```python
def add(a, b):
    result = a + b
    return result  # Return the result

print(add(3, 4))  # This will now print 7
```

### 10. Silent Failures
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero!")
print("No error detected!")
```

## Submission Guidelines:

- Submit a Python file containing your solutions.
- Include comments explaining each fix.
- Add a README file summarizing the challenges you faced and how you solved them.

Happy Debugging! 🐞
