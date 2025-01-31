# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, and age to the dog dictionary
dog["name"] = "Buddy"
dog["color"] = "Brown"
dog["breed"] = "Labrador"
dog["legs"] = 4
dog["age"] = 5

# Create a student dictionary
student = {
    "first_name": "John",
    "last_name": "Doe",
    "gender": "Male",
    "age": 22,
    "marital_status": "Single",
    "skills": ["Python", "Java"],
    "country": "USA",
    "city": "New York",
    "address": "123 Street Name"
}

# Get the length of the student dictionary
length_of_student_dict = len(student)
print("Length of student dictionary:", length_of_student_dict)

# Get the value of skills and check the data type
skills_value = student["skills"]
print("Skills:", skills_value)
print("Data type of skills:", type(skills_value))

# Modify the skills values by adding one or two skills
student["skills"].extend(["JavaScript", "SQL"])
print("Updated skills:", student["skills"])

# Get the dictionary keys as a list
student_keys = list(student.keys())
print("Student dictionary keys:", student_keys)

# Get the dictionary values as a list
student_values = list(student.values())
print("Student dictionary values:", student_values)

# Change the dictionary to a list of tuples using items() method
student_items = list(student.items())
print("Student dictionary as list of tuples:", student_items)

# Delete one of the items in the dictionary
del student["marital_status"]
print("Student dictionary after deleting 'marital_status':", student)

# Delete one of the dictionaries
del dog
# Trying to print dog will raise an error since it no longer exists
# print(dog)  # Uncommenting this line will cause a NameError
