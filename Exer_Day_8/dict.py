# Create an empty dictionary called dog and add specified keys and values
dog = {}
dog['name'] = None
dog['color'] = None
dog['breed'] = None
dog['legs'] = None
dog['age'] = None

# Create a student dictionary with specified keys
student = {
    'first_name': None,
    'last_name': None,
    'gender': None,
    'age': None,
    'marital_status': None,
    'skills': [],
    'country': None,
    'city': None,
    'address': None
}

# Get the length of the student dictionary
student_dict_length = len(student)

# Get the value of skills and check its data type
skills_value = student['skills']
skills_data_type = type(skills_value)

# Modify the skills values by adding one or two skills
student['skills'].extend(['Python', 'Data Analysis'])

# Get the dictionary keys and values as lists
student_keys = list(student.keys())
student_values = list(student.values())

# Convert the dictionary to a list of tuples using the items() method
student_items = list(student.items())

# Delete one of the items in the dictionary
student.pop('marital_status', None)

# Delete one of the dictionaries
del dog

# Displaying results for verification
print("Length of student dictionary:", student_dict_length)
print("Value of skills:", skills_value)
print("Data type of skills:", skills_data_type)
print("Dictionary keys as a list:", student_keys)
print("Dictionary values as a list:", student_values)
print("Student dictionary as a list of tuples:", student_items)
