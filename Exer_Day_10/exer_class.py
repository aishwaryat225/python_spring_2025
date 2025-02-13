# Loops
# For loop to print all even numbers between 1 and 20
for i in range(2, 21, 2):
    print(i)

# While loop to calculate the sum of numbers from 1 to 100
sum_numbers = 0
n = 1
while n <= 100:
    sum_numbers += n
    n += 1
print("Sum of numbers from 1 to 100:", sum_numbers)


# Lists
numbers = [10, 20, 30, 40, 50]
# Append 60 to the list
numbers.append(60)
# Remove 30 from the list
numbers.remove(30)
# Print the final list
print("Final list:", numbers)

# Function to return a list of unique elements
def unique_elements(input_list):
    return list(set(input_list))

input_list = [1, 2, 2, 3, 4, 4, 5, 5, 5]
result = unique_elements(input_list)
print(result)


# Dictionaries
student = {
    "name": "Matti",
    "age": 19,
    "grade": "A"
}

# Update age and add city
student["age"] = 29
student["city"] = "Helsinki"
print("Updated student dictionary:", student)

# Function to return the key with the maximum value in a dictionary
def key_with_max_value(d):
    return max(d, key=d.get)

sample_dict = {"a": 10, "b": 20, "c": 15}
print("Key with maximum value:", key_with_max_value(sample_dict))


# Functions
# Function to check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("radar"))  # True
print(is_palindrome("hello"))  # False

# Function to calculate the area of a rectangle with default parameters
def calculate_area(length=5, width=5):
    return length * width

print("Area with default sides:", calculate_area())
print("Area with length 10 and width 20:", calculate_area(10, 20))


# Combined Concepts
# Program to create a dictionary with numbers and their squares
squares = {x: x**2 for x in range(1, 11)}
print("Squares dictionary:", squares)

# Function to filter a list based on a provided function
def filter_list(lst, func):
    return [x for x in lst if func(x)]

def is_even(x):
    return x % 2 == 0

filtered = filter_list([1, 2, 3, 4, 5], is_even)
print("Filtered list:", filtered)
