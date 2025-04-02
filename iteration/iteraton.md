# Write a for loop to print numbers from 1 to 10.
for i in range(1, 11):
    print(i)

# Write a program that counts vowels in a string.
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Calculate the sum of squares from 1 to 100
sum_of_squares = sum(i**2 for i in range(1, 101))
print("Sum of squares from 1 to 100 is:", sum_of_squares)

# Generate and print a 10x10 multiplication table
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:4}", end=" ")  # Printing each value with spacing for alignment
    print()  # New line after each row

# Use PIL to invert the colors of an image.
image_path = 'your_image.jpg'  # Replace with the path to your image
image = Image.open(image_path)
image = image.convert('RGB')
inverted_image = ImageOps.invert(image)
inverted_image.save('inverted_image.jpg')  # Save the inverted image
inverted_image.show()  # Display the inverted image

