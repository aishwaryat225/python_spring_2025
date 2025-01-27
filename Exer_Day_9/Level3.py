person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Check if the person dictionary has 'skills' key
if 'skills' in person:
    skills = person['skills']
    # Print the middle skill
    middle_index = len(skills) // 2
    print("Middle skill:", skills[middle_index])
    
    # Check if 'Python' is in skills
    has_python = 'Python' in skills
    print("Has Python skill:", has_python)
    
    # Determine the person's title based on skills
    if set(skills) == {'JavaScript', 'React'}:
        print("He is a front end developer.")
    elif set(['Node', 'Python', 'MongoDB']).issubset(skills):
        print("He is a backend developer.")
    elif set(['React', 'Node', 'MongoDB']).issubset(skills):
        print("He is a fullstack developer.")
    else:
        print("Unknown title.")
else:
    print("'skills' key is not present in the person dictionary.")

# Check if the person is married and lives in Finland
if person.get('is_married') and person.get('country') == 'Finland':
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"{full_name} lives in Finland. He is married.")
