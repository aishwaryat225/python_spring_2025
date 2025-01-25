import math

# Step 1: Declare variables
first_name = "Aisha"
last_name = "Mishra"
full_name = first_name + " " + last_name
country = "Finland"
city = "Helsinki"
age = 31
year = 2025
is_married = True
is_true = True
is_light_on = True
a, b, c = 5, 10.5, "Python"

# Step 2: Check the data type of all variables
print(type(first_name))  # str
print(type(last_name))   # str
print(type(full_name))   # str
print(type(country))     # str
print(type(city))        # str
print(type(age))         # int
print(type(year))        # int
print(type(is_married))  # bool
print(type(is_true))     # bool
print(type(is_light_on)) # bool

# Step 3: Find the length of the first name
print("Length of first name:", len(first_name))

# Step 4: Compare the length of the first name and last name
print("Is first name longer than last name?", len(first_name) > len(last_name))

# Step 5: Arithmetic operations with num_one and num_two
num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

print("Total:", total)
print("Difference:", diff)
print("Product:", product)
print("Division:", division)
print("Remainder:", remainder)
print("Exponentiation:", exp)
print("Floor Division:", floor_division)

# Step 6: Circle calculations
radius = 30
area_of_circle = math.pi * radius**2
circum_of_circle = 2 * math.pi * radius
print("Area of Circle:", area_of_circle)
print("Circumference of Circle:", circum_of_circle)

# Step 7: Take radius as user input and calculate the area
radius_input = float(input("Enter the radius of the circle: "))
area_of_circle_input = math.pi * radius_input**2
print("Area of Circle with user input:", area_of_circle_input)

# Step 8: Get user input for first name, last name, country, and age
user_first_name = input("Enter your first name: ")
user_last_name = input("Enter your last name: ")
user_country = input("Enter your country: ")
user_age = int(input("Enter your age: "))

print(f"User Info - Name: {user_first_name} {user_last_name}, Country: {user_country}, Age: {user_age}")

# Step 9: Check Python reserved keywords
help('keywords')
