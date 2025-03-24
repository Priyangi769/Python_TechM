# Sequences in Python: Comprehensive Notes

## 5.1 Introduction: Sequences

In Python, a **sequence** is an ordered collection of items. The order of elements is preserved, and each element is accessible via its index. The main types of sequences in Python are:

- Strings
- Lists
- Tuples

### 5.1.1 Learning Goals

- Understand different types of sequences.
- Learn how to manipulate sequences.
- Perform operations like slicing, concatenation, and repetition.

### 5.1.2 Objectives

- Identify and use strings, lists, and tuples.
- Access elements using indexing and slicing.
- Perform operations like count, index, split, and join.

---

## 5.2 Strings, Lists, and Tuples

### 5.2.1 Strings

A **string** is an immutable sequence of characters.

```python
text = "Hello, World!"
```

- Access elements using indexes:

```python
print(text[0])  # Output: H
```

### 5.2.2 Lists

A **list** is a mutable sequence used to store items of different types.

```python
numbers = [1, 2, 3, 4, 5]
numbers[0] = 10  # Lists are mutable
```

### 5.2.3 Tuples

A **tuple** is an immutable sequence.

```python
tuple_example = (1, 2, 3)
# tuple_example[0] = 10  # Raises TypeError
```

---

## 5.3 Index Operator: Working with the Characters of a String

The index operator (`[]`) allows accessing elements by index.

```python
text = "Python"
print(text[1])  # Output: y
```

### 5.3.1 Index Operator: Accessing Elements of a List or Tuple

```python
my_list = [10, 20, 30]
print(my_list[2])  # Output: 30
```

---

## 5.4 Disambiguating []: Creation vs Indexing

- **Creation:**

```python
my_list = []  # Empty list
```

- **Indexing:**

```python
value = my_list[0]  # Access first element
```

---

## 5.5 Length

Use `len()` to get the number of elements:

```python
my_list = [1, 2, 3, 4]
print(len(my_list))  # Output: 4
```

---

## 5.6 The Slice Operator

Slicing extracts a portion of the sequence.

```python
my_list = [0, 1, 2, 3, 4]
print(my_list[1:4])  # Output: [1, 2, 3]
```

### 5.6.1 List Slices

```python
numbers = [1, 2, 3, 4, 5]
print(numbers[1:4])  # Output: [2, 3, 4]
```

### 5.6.2 Tuple Slices

```python
tuple_example = (10, 20, 30, 40)
print(tuple_example[1:3])  # Output: (20, 30)
```

---

## 5.7 Concatenation and Repetition

- **Concatenation:**

```python
list1 = [1, 2]
list2 = [3, 4]
result = list1 + list2  # [1, 2, 3, 4]
```

- **Repetition:**

```python
my_list = [0] * 5  # [0, 0, 0, 0, 0]
```

---

## 5.8 Count and Index

### 5.8.1 Count

Counts occurrences of an item:

```python
my_list = [1, 2, 2, 3]
print(my_list.count(2))  # Output: 2
```

### 5.8.2 Index

Finds the index of the first occurrence:

```python
print(my_list.index(2))  # Output: 1
```

---

## 5.9 Splitting and Joining Strings

- **Splitting:**

```python
sentence = "Python is awesome"
words = sentence.split()  # ['Python', 'is', 'awesome']
```

- **Joining:**

```python
words = ['Python', 'is', 'awesome']
sentence = ' '.join(words)  # 'Python is awesome'
```

---

## Assignment Questions

1. Define a sequence. What types of sequences exist in Python?
A sequence is a data structure that contains items arranged in order, and you can access each item using an integer index that represents its position in the sequence. You can always find the length of a sequence. 
Types of Sequences in Python
Python has several built-in types of sequences:

List:
 - A list is an ordered collection of items that can be changed (mutable).
 - Lists can store items of different data types.
Example: 
```python
   my_list = [1, 2, 3, "apple", 4.5]
```
Tuple:
 - A tuple is similar to a list but is immutable (i.e., its items cannot be modified after creation).
Example: 
```python
   my_tuple = (1, 2, 3, "apple", 4.5)
```
String:
 - A string is a sequence of characters, which is also immutable.
Example:
```pyhton
   my_string = "Hello, World!"
```
Range:
 - A range is a sequence of numbers, often used in loops. It's a memory-efficient sequence for    representing a range of numbers.
Example: 
```python
   my_range = range(1, 10)
```
Bytes:
 - A byte sequence represents immutable sequences of bytes.
Example:
```pyhton
   my_bytes = b"Hello"
```
2. How are strings, lists, and tuples different from each other?
Strings, lists, and tuples in Python are all sequence types, but they have some important differences in terms of mutability, behavior, and usage. Here's a breakdown of how they differ:

Mutability:
 - String: Immutable.
   Once a string is created, its content cannot be changed. If you try to modify a string, a new string will be created.
Example: 
```python
   s = "hello"
   s[0] = "H"  # This will raise a TypeError because strings are immutable.
```
- List: Mutable.
  You can change, add, or remove elements in a list after it's created.
Example:
```python
lst = [1, 2, 3]
lst[0] = 100  # This works, so lst becomes [100, 2, 3]
lst.append(4)  # Adds an element to the end, so lst becomes [100, 2, 3, 4]
```
- Tuple: Immutable.
  Like strings, tuples are immutable, meaning their elements cannot be changed after they are created.
Example:
```python
tup = (1, 2, 3)
tup[0] = 100  # This will raise a TypeError because tuples are immutable.
```
3. Explain how indexing works in Python with an example.
Indexing in Python
Indexing in Python allows you to access specific elements within a sequence (like lists, strings, tuples, etc.) by referring to their position or index.
Python sequences are zero-indexed, meaning that the first element of a sequence has an index of 0, the second has an index of 1, and so on.
How Indexing Works:
Positive Indexing: Starts from 0 for the first element and increases as you move to the right.
Negative Indexing: Starts from -1 for the last element and decreases as you move to the left.
- Example:
```python
   my_list = [10, 20, 30, 40, 50]

# Access elements using positive indexing
print(my_list[0])   # Output: 10  (first element)
print(my_list[2])   # Output: 30  (third element)
print(my_list[4])   # Output: 50  (fifth element)

# Access elements using negative indexing
print(my_list[-1])  # Output: 50  (last element)
print(my_list[-2])  # Output: 40  (second-to-last element)
print(my_list[-4])  # Output: 20  (fourth element from the end)
```
4. Write code to access the last character of a string.
```python
string = "hello"
last_character = string[len(string) - 1]
print(last_character)
```
5. Create a list of numbers and access the third element.
```python
# Create a list of numbers
my_list = [10, 20, 30, 40, 50]

# Access the third element (index 2, since indexing starts from 0)
third_element = my_list[2]

# Print the third element
print(third_element)  # Output: 30
```
6. What is the result of `len([1, [2, 3], 4])` and why?
The len() function in Python returns the number of elements in a list. It does not count the individual items within sublists, but rather counts the number of items at the top level of the list.

For the list [1, [2, 3], 4]:

The first element is 1 (an integer).
The second element is [2, 3] (a sublist).
The third element is 4 (an integer).
So, there are three top-level elements in the list:
 - 1
 - [2, 3] (the sublist itself is counted as one element)
 - 4
Thus, len([1, [2, 3], 4]) returns 3.

7. Explain slicing with a practical example.
Slicing in Python
Slicing is a way to access a subset of a sequence (such as a list, string, or tuple) by specifying a start index, end index, and an optional step. The syntax for slicing is:
 - sequence[start:end:step]
   start: The index of the first element to include in the slice. If not specified, defaults to 0.
   end: The index of the element where the slice stops, but does not include the element at the end index. If not specified, defaults to the end of the sequence.
   step: The step between each index in the slice. If not specified, defaults to 1.
Practical Example of Slicing
Let's work through an example using a list:
```python
my_list = [10, 20, 30, 40, 50, 60, 70, 80]

# Slicing with start and end
subset = my_list[2:6]
print(subset)  # Output: [30, 40, 50, 60]

# Slicing with start, end, and step
subset_with_step = my_list[1:7:2]
print(subset_with_step)  # Output: [20, 40, 60]

# Slicing from the beginning to a specific index
subset_from_start = my_list[:4]
print(subset_from_start)  # Output: [10, 20, 30, 40]

# Slicing from a specific index to the end
subset_to_end = my_list[3:]
print(subset_to_end)  # Output: [40, 50, 60, 70, 80]

# Slicing with negative indices (counting from the end)
subset_negative = my_list[-5:-1]
print(subset_negative)  # Output: [30, 40, 50, 60]

# Slicing with negative step (reversing the list)
reverse_slice = my_list[7:2:-1]
print(reverse_slice)  # Output: [80, 70, 60, 50]
```
8. How would you reverse a string using slicing?
```python
   my_string = "Python"
   reversed_string = my_string[::-1]
   print(reversed_string)  # Output: "nohtyP"
```
9. Demonstrate list concatenation and repetition with examples.
List Concatenation and Repetition in Python
 - List Concatenation:
   List concatenation is the operation of joining two or more lists together to form a single list.
   It is done using the + operator.
Example of List Concatenation:
```python
   list1 = [1, 2, 3]
   list2 = [4, 5, 6]
   # Concatenate the two lists
   concatenated_list = list1 + list2
   print(concatenated_list)  # Output: [1, 2, 3, 4, 5, 6]
```
Example of List Repetition:
```python
   my_list = [1, 2, 3]
   # Repeat the list 3 times
   repeated_list = my_list * 3
   print(repeated_list)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]
```
10. Write code to count the occurrences of an element in a list.
```python
   my_list = [1, 2, 3, 4, 2, 5, 2]
   # Count the occurrences of the element 2
   count_of_2 = my_list.count(2)
   print(count_of_2)  # Output: 3
```
11. What will `my_tuple = (1, 2, 3); print(my_tuple[1:])` output?
(2, 3)

12. Explain the difference between `list.append()` and `list.extend()`.
list.append():
- Purpose: Adds a single element to the end of the list.
- Behavior: The argument passed to append() is added as a single element, meaning the entire       object is appended as one element, even if it’s a list or another iterable.
list.extend():
- Purpose: Adds all the elements of an iterable (like a list, tuple, or string) to the end of the list.
- Behavior: Each element of the iterable is added individually to the list. If you pass a list to extend(), it will add each element of the list to the original list, not the list as a single element.

13. Write code to split the sentence: "Learn Python, step by step!" into words.
```python
   sentence = "Learn Python, step by step!"
   # Split the sentence into words
   words = sentence.split()
   print(words)  # Output: ['Learn', 'Python,', 'step', 'by', 'step!']
```

14. Join a list `['Python', 'is', 'fun']` into a single string.
```python
   words = ['Python', 'is', 'fun']
   # Join the list into a single string with a space separator
   sentence = ' '.join(words)
   print(sentence)  # Output: "Python is fun"
```
15. Given a list `numbers = [1, 2, 2, 3, 4, 2]`, find the index of the first `2`.
```python
   numbers = [1, 2, 2, 3, 4, 2]
   # Find the index of the first occurrence of 2
   index_of_first_2 = numbers.index(2)
   print(index_of_first_2)  # Output: 1
```
16. Write code to check if a string is a palindrome.
```python
   def is_palindrome(s):
    # Convert the string to lowercase and remove non-alphanumeric characters
    s = ''.join(e for e in s if e.isalnum()).lower()
    # Check if the string is equal to its reverse
    return s == s[::-1]
    # Example usage
    string = "A man, a plan, a canal, Panama"
    result = is_palindrome(string)
    print(result)  # Output: True
```
17. Implement a function that returns the length of the longest word in a sentence.
```python
   def longest_word_length(sentence):
    # Split the sentence into words
    words = sentence.split()
    # Find the length of the longest word
    longest_length = max(len(word) for word in words)
    return longest_length
    # Example usage
    sentence = "The quick brown fox jumped over the lazy dog"
    result = longest_word_length(sentence)
    print(result)  # Output: 6
```
18. Demonstrate nested list indexing.
```python
   # Nested list (list of lists)
   nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
   # Accessing an element from the first inner list (index 0)
   first_inner_list = nested_list[0]
   print(first_inner_list)  # Output: [1, 2, 3]
   # Accessing an individual element within the first inner list
   element_1 = nested_list[0][1]  # First inner list, second element (index 1)
   print(element_1)  # Output: 2
   # Accessing an element from the second inner list (index 1)
   element_2 = nested_list[1][2]  # Second inner list, third element (index 2)
   print(element_2)  # Output: 6
   # Accessing the last element from the last inner list (index -1)
   element_3 = nested_list[-1][-1]  # Last inner list, last element
   print(element_3)  # Output: 9
```
19. How do you convert a list of characters into a string?
```python
   # List of characters
   char_list = ['H', 'e', 'l', 'l', 'o']
   # Convert the list of characters into a string
   result_string = ''.join(char_list)
   print(result_string)  # Output: "Hello"
```
20. Write code to remove duplicates from a list while preserving order.
```python
   def remove_duplicates(input_list):
      seen = set()  # Set to keep track of seen elements
      result = []   # List to store the elements without duplicates

    for item in input_list:
        if item not in seen:
            result.append(item)  # Add the item to the result if it's not seen
            seen.add(item)        # Mark this item as seen

    return result
# Example usage
my_list = [1, 2, 2, 3, 4, 2, 5, 3]
result = remove_duplicates(my_list)
print(result)  # Output: [1, 2, 3, 4, 5]
```
21. Write a function that takes a list of tuples and sorts it by the second element of each tuple.
```python
   def sort_by_second_element(tuple_list):
    # Sort the list of tuples by the second element of each tuple
    return sorted(tuple_list, key=lambda x: x[1])

   # Example usage
   my_list = [(1, 5), (2, 3), (4, 1), (3, 4)]
   sorted_list = sort_by_second_element(my_list)
   print(sorted_list)  # Output: [(4, 1), (2, 3), (3, 4), (1, 5)]
```

22. Implement a program to flatten a nested list of arbitrary depth.
```python
   def flatten(nested_list):
       flat_list = []
    
          for element in nested_list:
              if isinstance(element, list):  # If the element is a list
              flat_list.extend(flatten(element))  # Recursively flatten it and extend the result
          else:
              flat_list.append(element)  # If it's not a list, just add it to the result
    return flat_list
   # Example usage
   nested_list = [1, [2, [3, 4], 5], 6, [7, [8, [9]]]]
   flattened_list = flatten(nested_list)
   print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```
23. Create a function that rotates a list to the right by k steps.
```python
   def rotate_list(lst, k):
    # If k is greater than the length of the list, take the remainder of k divided by length
    k = k % len(lst) if lst else 0  # Handle empty list as well
    # Slice the list to rotate it
    return lst[-k:] + lst[:-k]
    # Example usage
    my_list = [1, 2, 3, 4, 5, 6]
    rotated_list = rotate_list(my_list, 2)
    print(rotated_list)  # Output: [5, 6, 1, 2, 3, 4]
```
24. Given two strings, write a function that returns True if they are anagrams.
```python
   def are_anagrams(str1, str2):
       # Remove spaces and convert to lowercase for case-insensitive comparison
       str1 = str1.replace(" ", "").lower()
       str2 = str2.replace(" ", "").lower()
       # Sort the strings and compare them
       return sorted(str1) == sorted(str2)
       # Example usage
       str1 = "listen"
       str2 = "silent"
       result = are_anagrams(str1, str2)
       print(result)  # Output: True
```
25. Create a function to split a list into chunks of a specified size.
```python
   def split_list(lst, chunk_size):
       """Splits a list into chunks of a specified size."""
        return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]
```
26. Implement a function that merges two sorted lists into one sorted list.
```python
   def merge_sorted_lists(list1, list2):
       """Merges two sorted lists into one sorted list."""
       merged_list = []
       i, j = 0, 0
    
    # Traverse both lists and append the smaller element to merged_list
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    
    # Append remaining elements from list1 (if any)
    merged_list.extend(list1[i:])
    
    # Append remaining elements from list2 (if any)
    merged_list.extend(list2[j:])
    
    return merged_list
```


# 🚀 Questions on Sequences in Python

1. **Data Pipeline Validator**

   - **Task**: Identify the longest pipeline and return pipelines taking more than a given threshold time.
   - **Input**:
     ```python
     pipelines = [
         ("Data Ingestion", 30),
         ("Preprocessing", 45),
         ("Model Training", 120),
         ("Evaluation", 20)
     ]
     threshold = 40
     ```
   - **Expected Output**:
     ```
     Longest Pipeline: Model Training
     Pipelines exceeding threshold: ['Preprocessing', 'Model Training']
     ```
To solve this problem, we need to perform the following steps:
- Identify the longest pipeline by comparing the times.
- Filter out the pipelines whose times exceed the given threshold.
```python
def data_pipeline_validator(pipelines, threshold):
    # Find the longest pipeline
    longest_pipeline = max(pipelines, key=lambda x: x[1])[0]
    
    # Find pipelines exceeding the threshold
    exceeding_threshold = [pipeline[0] for pipeline in pipelines if pipeline[1] > threshold]
    
    # Prepare the result
    return {
        "Longest Pipeline": longest_pipeline,
        "Pipelines exceeding threshold": exceeding_threshold
    }

# Example Input
pipelines = [
    ("Data Ingestion", 30),
    ("Preprocessing", 45),
    ("Model Training", 120),
    ("Evaluation", 20)
]
threshold = 40

# Get the output
output = data_pipeline_validator(pipelines, threshold)
print(output)
```

2. **Log File Parser**
   - **Task**: Extract unique error codes from a log file.
   - **Input**:
     ```python
     logs = """ERROR 404: Not Found
     INFO: Connection established
     ERROR 500: Internal Server Error
     ERROR 404: Not Found
     """
     ```
   - **Expected Output**:
     ```
     Unique Error Codes: ['404', '500']
     ```
To extract unique error codes from the log file, we need to:
- Parse the log entries to extract error codes.
- Filter out any non-error lines or duplicates.
- Return a list of unique error codes.
```python
import re

def log_file_parser(logs):
    # Regular expression to find error codes after the "ERROR" keyword
    error_codes = re.findall(r'ERROR (\d+)', logs)
    
    # Get unique error codes
    unique_error_codes = list(set(error_codes))
    
    # Return the result
    return {
        "Unique Error Codes": unique_error_codes
    }

# Example Input
logs = """ERROR 404: Not Found
INFO: Connection established
ERROR 500: Internal Server Error
ERROR 404: Not Found
"""

# Get the output
output = log_file_parser(logs)
print(output)
```

## 5.2. Strings, Lists, and Tuples

3. **Config File Reader**

   - **Task**: Parse key-value pairs from a configuration string.
   - **Input**:
     ```python
     config = "host=127.0.0.1;port=8080;mode=debug"
     ```
   - **Expected Output**:
     ```
     [('host', '127.0.0.1'), ('port', '8080'), ('mode', 'debug')]
     ```
To parse the key-value pairs from the given configuration string, we can:
- Split the string using the semicolon (;) delimiter to   separate the key-value pairs.
- Further split each key-value pair by the equal sign (=) to separate the keys from the values.
- Convert the result into a list of tuples.
```python
def config_file_reader(config):
    # Split the configuration string by semicolon to separate key-value pairs
    pairs = config.split(';')
    
    # Split each pair by '=' and convert them to a tuple (key, value)
    result = [tuple(pair.split('=')) for pair in pairs]
    
    return result

# Example Input
config = "host=127.0.0.1;port=8080;mode=debug"

# Get the output
output = config_file_reader(config)
print(output)
```

4. **Social Media Data Cleaner**
   - **Task**: Extract unique hashtags from a social media post.
   - **Input**:
     ```python
     post = "Loving the new #Python course! #Coding #Python #Learning"
     ```
   - **Expected Output**:
     ```
     ['#Python', '#Coding', '#Learning']
     ```
To extract unique hashtags from the given social media post, we need to:
- Identify the hashtags in the text, which begin with the  symbol.
- Collect these hashtags, ensuring that we remove duplicates.
- Return the list of unique hashtags.
```python
import re
def social_media_data_cleaner(post):
    # Use regex to find all hashtags
    hashtags = re.findall(r'#\w+', post)
    
    # Get unique hashtags by converting the list to a set and back to a list
    unique_hashtags = list(set(hashtags))
    
    return unique_hashtags

# Example Input
post = "Loving the new #Python course! #Coding #Python #Learning"

# Get the output
output = social_media_data_cleaner(post)
print(output)
```
---

## 5.3. Index Operator: Working with Characters

5. **Secret Code Decoder**

   - **Task**: Extract every third character from a string.
   - **Input**:
     ```python
     secret_message = "hweollrolwd"
     ```
   - **Expected Output**:
     ```
     'hello world'
     ```
To extract every third character from a string and decode the secret message, we can use Python's slicing technique.

Here's the approach:
- We can use slicing with a step size of 3 to get every third character from the input string.
- After extracting the characters, we will join them to form the decoded message.
```python
def secret_code_decoder(secret_message):
    # Extract every third character starting from index 0
    decoded_message = secret_message[::3]
    return decoded_message

# Example Input
secret_message = "hweollrolwd"

# Get the output
output = secret_code_decoder(secret_message)
print(output)
```

6. **Inventory Tracker**
   - **Task**: Find the product with the highest quantity.
   - **Input**:
     ```python
     inventory = [
         ("Apples", 50),
         ("Oranges", 75),
         ("Bananas", 30)
     ]
     ```
   - **Expected Output**:
     ```
     'Oranges'
     ```
To solve the problem of finding the product with the highest quantity, we can:
- Iterate through the list of inventory items.
- Compare the quantities and identify the product with the highest quantity.
```python
def inventory_tracker(inventory):
    # Find the product with the highest quantity using max() based on the second element (quantity)
    highest_quantity_product = max(inventory, key=lambda item: item[1])[0]
    return highest_quantity_product

# Example Input
inventory = [
    ("Apples", 50),
    ("Oranges", 75),
    ("Bananas", 30)
]

# Get the output
output = inventory_tracker(inventory)
print(output)
```
---

## 5.4. Disambiguating `[]`: Creation vs Indexing

7. **Survey Data Analyzer**

   - **Task**: Extract scores from a survey string and find min/max.
   - **Input**:
     ```python
     survey_data = "5,3,4,1,2"
     ```
   - **Expected Output**:
     ```
     Max Score: 5, Min Score: 1
     ```
To extract the scores from the survey string and find the minimum and maximum scores, we can:
- Split the string into individual score components.
- Convert those components into integers.
- Use the built-in min() and max() functions to find the minimum and maximum scores.
```python
def survey_data_analyzer(survey_data):
    # Split the string by commas to extract individual scores and convert to integers
    scores = list(map(int, survey_data.split(',')))
    
    # Find the max and min scores
    max_score = max(scores)
    min_score = min(scores)
    
    # Return the result in the desired format
    return f"Max Score: {max_score}, Min Score: {min_score}"

# Example Input
survey_data = "5,3,4,1,2"

# Get the output
output = survey_data_analyzer(survey_data)
print(output)
```

8. **Access Control Manager**
   - **Task**: Manage user access levels using lists and tuples.
   - **Input**:
     ```python
     users = ["Alice", "Bob", "Charlie"]
     roles = ("Admin", "Editor", "Viewer")
     ```
   - **Expected Output**:
     ```
     Alice: Admin, Bob: Editor, Charlie: Viewer
     ```
To manage user access levels using the lists and tuples, we need to:
- Pair each user with their corresponding role.
- Format the output to show each user's name followed by their role.
```python
def access_control_manager(users, roles):
    # Zip users and roles together, then format the output as required
    user_roles = [f"{user}: {role}" for user, role in zip(users, roles)]
    
    # Join the results with a comma and return the output
    return ", ".join(user_roles)

# Example Input
users = ["Alice", "Bob", "Charlie"]
roles = ("Admin", "Editor", "Viewer")

# Get the output
output = access_control_manager(users, roles)
print(output)
```
---
## 5.5. Length

9. **Customer Support Ticket System**

   - **Task**: Categorize tickets based on message length.
   - **Input**:
     ```python
     message = "My account is locked, please help!"
     ```
   - **Expected Output**:
     ```
     Category: Medium
     ```
To categorize the support ticket based on message length, we can follow these steps:
- Determine the length of the message.
Categorize the message based on its length (e.g., short, medium, or long).
Let's assume the following categorization rules:
- Short: Message length is less than or equal to 20 characters.
- Medium: Message length is between 21 and 50 characters.
- Long: Message length is greater than 50 characters.
```python
def categorize_ticket(message):
    # Get the length of the message
    message_length = len(message)
    
    # Categorize based on message length
    if message_length <= 20:
        category = "Short"
    elif 21 <= message_length <= 50:
        category = "Medium"
    else:
        category = "Long"
    
    return f"Category: {category}"

# Example Input
message = "My account is locked, please help!"

# Get the output
output = categorize_ticket(message)
print(output)
```

10. **Product Catalog Manager**

- **Task**: Find the product with the longest name.
- **Input**:
  ```python
  products = ["Laptop", "Smartphone", "Wireless Headphones"]
  ```
- **Expected Output**:
  ```
  'Wireless Headphones'
  ```
To solve the problem of finding the product with the longest name, we can:
- Iterate through the list of products.
- Use the max() function to find the product with the longest name based on the length of the product name.
```python
def product_catalog_manager(products):
    # Find the product with the longest name using the max() function based on length
    longest_product = max(products, key=len)
    return longest_product

# Example Input
products = ["Laptop", "Smartphone", "Wireless Headphones"]

# Get the output
output = product_catalog_manager(products)
print(output)
```

---

## 5.6. The Slice Operator

11. **Sensor Data Analyzer**

- **Task**: Extract the last 10 sensor readings and calculate the average.
- **Input**:
  ```python
  sensor_readings = [12, 15, 14, 16, 20, 22, 21, 23, 25, 30, 28, 27]
  ```
- **Expected Output**:
  ```
  Average: 22
  ```
To extract the last 10 sensor readings and calculate the average, we can follow these steps:
- Extract the last 10 readings from the list using slicing.
- Calculate the average of these 10 readings.
```python
def sensor_data_analyzer(sensor_readings):
    # Extract the last 10 sensor readings
    last_10_readings = sensor_readings[-10:]
    
    # Calculate the average
    average = sum(last_10_readings) / len(last_10_readings)
    
    # Return the result
    return f"Average: {int(average)}"  # rounding off for whole number

# Example Input
sensor_readings = [12, 15, 14, 16, 20, 22, 21, 23, 25, 30, 28, 27]

# Get the output
output = sensor_data_analyzer(sensor_readings)
print(output)
```

12. **Transaction Reverser**

- **Task**: Reverse the list of transactions.
- **Input**:
  ```python
  transactions = [100, -50, 200, -150, 50]
  ```
- **Expected Output**:
  ```
  [50, -150, 200, -50, 100]
  ```
To reverse the list of transactions, we can use Python's built-in list reverse method or slicing.
```python
def transaction_reverser(transactions):
    # Reverse the list of transactions
    return transactions[::-1]

# Example Input
transactions = [100, -50, 200, -150, 50]

# Get the output
output = transaction_reverser(transactions)
print(output)
```

---

## 5.7. Concatenation and Repetition

13. **Log Formatter**

- **Task**: Format logs with timestamps.
- **Input**:
  ```python
  logs = ["System Boot", "Network Connected", "User Login"]
  timestamp = "2025-03-20"
  ```
- **Expected Output**:
  ```
  ['2025-03-20: System Boot', '2025-03-20: Network Connected', '2025-03-20: User Login']
  ```
To format the logs with timestamps, we can simply prepend the timestamp to each log entry. Here's how you can do that:
- Iterate over the list of log messages.
- Prepend the timestamp to each log entry.
- Return the formatted log entries.
```python
def log_formatter(logs, timestamp):
    # Format each log with the timestamp
    formatted_logs = [f"{timestamp}: {log}" for log in logs]
    return formatted_logs

# Example Input
logs = ["System Boot", "Network Connected", "User Login"]
timestamp = "2025-03-20"

# Get the output
output = log_formatter(logs, timestamp)
print(output)
```

14. **Pattern Generator**

- **Task**: Generate patterns with repetition.
- **Input**:
  ```python
  symbol = "*"
  count = 5
  ```
- **Expected Output**:
  ```
  '* * * * *'
  ```
To generate a pattern with repetition of a symbol, we can:
- Repeat the symbol a specified number of times, separated by spaces.
- Join the repeated symbols into a single string.
```python
def pattern_generator(symbol, count):
    # Generate the pattern by repeating the symbol with spaces
    pattern = " ".join([symbol] * count)
    return pattern

# Example Input
symbol = "*"
count = 5

# Get the output
output = pattern_generator(symbol, count)
print(output)
```

---

## 5.8. Count and Index

15. **Customer Feedback Analyzer**

- **Task**: Count keyword occurrences.
- **Input**:
  ```python
  feedback = "The product is excellent, absolutely excellent!"
  ```
- **Expected Output**:
  ```
  'excellent' count: 2
  ```
To count the occurrences of a specific keyword in a string, we can:
- Use the count() method to count how many times the keyword appears in the string.
```python
def customer_feedback_analyzer(feedback, keyword):
    # Count occurrences of the keyword in the feedback string
    keyword_count = feedback.lower().count(keyword.lower())
    return f"'{keyword}' count: {keyword_count}"

# Example Input
feedback = "The product is excellent, absolutely excellent!"
keyword = "excellent"

# Get the output
output = customer_feedback_analyzer(feedback, keyword)
print(output)
```

16. **Sentence Index Finder**

- **Task**: Find the index of the first occurrence of "error".
- **Input**:
  ```python
  log = "INFO: All systems go. ERROR: Failed to start service."
  ```
- **Expected Output**:
  ```
  Index: 21
  ```
To find the index of the first occurrence of the word "error" (or "ERROR" in this case) in a string, we can:
- Use the find() method of the string, which returns the index of the first occurrence of the specified substring.
- Ensure that we are looking for the word "ERROR" specifically (case-sensitive in this case).
```python
def sentence_index_finder(log, keyword):
    # Find the index of the first occurrence of the keyword
    index = log.find(keyword)
    return f"Index: {index}"

# Example Input
log = "INFO: All systems go. ERROR: Failed to start service."
keyword = "ERROR"

# Get the output
output = sentence_index_finder(log, keyword)
print(output)
```
---

## 5.9. Splitting and Joining Strings

17. **CSV Parser**

- **Task**: Parse CSV data into lists.
- **Input**:
  ```python
  csv_data = "Alice,25,Engineer\nBob,30,Doctor\nCharlie,22,Artist"
  ```
- **Expected Output**:
  ```
  [['Alice', '25', 'Engineer'], ['Bob', '30', 'Doctor'], ['Charlie', '22', 'Artist']]
  ```
To parse CSV data into lists, we can:
- Split the string by newline characters (\n) to get individual rows.
- Split each row by commas (,) to get the individual values in each row.
```python
def csv_parser(csv_data):
    # Split the data into rows and then split each row by commas
    parsed_data = [row.split(',') for row in csv_data.split('\n')]
    return parsed_data

# Example Input
csv_data = "Alice,25,Engineer\nBob,30,Doctor\nCharlie,22,Artist"

# Get the output
output = csv_parser(csv_data)
print(output)
```

18. **Username Generator**

- **Task**: Generate usernames from full names.
- **Input**:
  ```python
  names = ["Alice Wonderland", "Bob Builder", "Charlie Chaplin"]
  ```
- **Expected Output**:
  ```
  ['AWonderland', 'BBuilder', 'CChaplin']
  ```
To generate usernames from full names, we can:
- Extract the first letter of the first name.
- Append the full last name to this first letter.
- Construct the username by combining these parts.
```python
def username_generator(names):
    # Generate usernames by combining the first letter of the first name with the full last name
    usernames = [name.split()[0][0] + name.split()[1] for name in names]
    return usernames

# Example Input
names = ["Alice Wonderland", "Bob Builder", "Charlie Chaplin"]

# Get the output
output = username_generator(names)
print(output)
```

---

## Bonus Advanced Problems

19. **Chat Log Analyzer**

- **Task**: Count messages per user from chat logs.
- **Input**:
  ```python
  chat_logs = [
      "Alice: Hi!",
      "Bob: Hello!",
      "Alice: How are you?",
      "Bob: I’m good, thanks!"
  ]
  ```
- **Expected Output**:
  ```
  Alice: 2 messages, Bob: 2 messages
  ```
To count the number of messages per user in the chat logs, we can:
- Iterate through each chat log entry.
- Split each entry by the delimiter : to extract the user's name.
- Count the occurrences of each user's name.
```python
def chat_log_analyzer(chat_logs):
    # Create a dictionary to store the message counts per user
    message_count = {}
    
    # Iterate through each chat log entry
    for log in chat_logs:
        user = log.split(":")[0]  # Extract the user's name (before the colon)
        
        # Increment the count for the user
        message_count[user] = message_count.get(user, 0) + 1
    
    # Format the output string
    output = ", ".join([f"{user}: {count} messages" for user, count in message_count.items()])
    return output

# Example Input
chat_logs = [
    "Alice: Hi!",
    "Bob: Hello!",
    "Alice: How are you?",
    "Bob: I’m good, thanks!"
]

# Get the output
output = chat_log_analyzer(chat_logs)
print(output)
```

20. **Data Compressor**

- **Task**: Compress recurring substrings.
- **Input**:
  ```python
  data = "abababababab"
  ```
- **Expected Output**:
  ```
  'ab' repeated 6 times
  ```
To solve the problem of compressing recurring substrings, we can follow these steps:
- Identify the longest repeating substring.
- Determine how many times the substring repeats consecutively.
- Format the output to show the substring and its  repetition count.
```python
def data_compressor(data):
    # Find the smallest repeating unit by checking increasing lengths of substrings
    for i in range(1, len(data)//2 + 1):
        substring = data[:i]
        repeat_count = len(data) // len(substring)
        
        # Check if the substring repeats to form the entire string
        if substring * repeat_count == data:
            return f"'{substring}' repeated {repeat_count} times"
    
    # If no repeating pattern is found, return the original string
    return data

# Example Input
data = "abababababab"

# Get the output
output = data_compressor(data)
print(output)
```

---