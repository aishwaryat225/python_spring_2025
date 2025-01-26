# Create an empty tuple
empty_tuple = ()

# Create tuples containing names of your imaginary siblings
sisters = ("Alice", "Sophia", "Emily")
brothers = ("James", "John", "Michael")

# Join brothers and sisters tuples and assign to siblings
siblings = sisters + brothers

# Find the number of siblings
number_of_siblings = len(siblings)
print(f"I have {number_of_siblings} siblings.")

# Add the name of your father and mother to the siblings tuple and assign it to family_members
family_members = siblings + ("Father", "Mother")

# Display the family_members tuple
print("Family members:", family_members)


# Unpack siblings and parents from family_members
siblings = family_members[:-2]
parents = family_members[-2:]
print("Siblings:", siblings)
print("Parents:", parents)

# Create fruits, vegetables, and animal products tuples
fruits = ("apple", "banana", "orange")
vegetables = ("carrot", "broccoli", "spinach")
animal_products = ("milk", "cheese", "eggs")

# Join the three tuples and assign it to food_stuff_tp
food_stuff_tp = fruits + vegetables + animal_products

# Change food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# Slice out the middle item or items from the food_stuff_lt list
middle_index = len(food_stuff_lt) // 2
if len(food_stuff_lt) % 2 == 0:
    middle_items = food_stuff_lt[middle_index - 1:middle_index + 1]
else:
    middle_items = food_stuff_lt[middle_index:middle_index + 1]
print("Middle item(s):", middle_items)

# Slice out the first three and last three items from food_stuff_lt list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print("First three items:", first_three)
print("Last three items:", last_three)

# Delete the food_stuff_tp tuple completely
del food_stuff_tp

# Check if an item exists in a tuple
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

# Check if 'Estonia' is a Nordic country
is_estonia_nordic = 'Estonia' in nordic_countries
print("Is Estonia a Nordic country?", is_estonia_nordic)

# Check if 'Iceland' is a Nordic country
is_iceland_nordic = 'Iceland' in nordic_countries
print("Is Iceland a Nordic country?", is_iceland_nordic)
