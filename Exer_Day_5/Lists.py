# 1. Declare an empty list
empty_list = []

# 2. Declare a list with more than 5 items
items_list = [1, 2, 3, 4, 5, 6]

# 3. Find the length of your list
length_of_list = len(items_list)
print(f"Length of the list: {length_of_list}")

# 4. Get the first item, the middle item, and the last item of the list
first_item = items_list[0]
middle_item = items_list[len(items_list) // 2]
last_item = items_list[-1]
print(f"First item: {first_item}, Middle item: {middle_item}, Last item: {last_item}")

# 5. Declare a list called mixed_data_types
mixed_data_types = ["John Doe", 30, 175.5, "Married", "123 Main St, Helsinki"]
print(f"Mixed data types list: {mixed_data_types}")

# 6. Declare a list variable named it_companies
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)

# 7. Print the number of companies in the list
number_of_companies = len(it_companies)
print(f"Number of companies: {number_of_companies}")

# 8. Print the first, middle, and last company
first_company = it_companies[0]
middle_company = it_companies[len(it_companies) // 2]
last_company = it_companies[-1]
print(f"First company: {first_company}, Middle company: {middle_company}, Last company: {last_company}")

# 9. Modify one of the companies
it_companies[0] = "Meta"
print(f"Modified list: {it_companies}")

# 10. Add an IT company
it_companies.append("Cisco")
print(f"List after adding a company: {it_companies}")

# 11. Insert an IT company in the middle
it_companies.insert(len(it_companies) // 2, "SAP")
print(f"List after inserting a company in the middle: {it_companies}")

# 12. Change one company's name to uppercase (excluding IBM)
it_companies[1] = it_companies[1].upper()
print(f"List after changing one company name to uppercase: {it_companies}")

# 13. Join the companies with a string '#; '
joined_companies = '#; '.join(it_companies)
print(f"Joined companies: {joined_companies}")

# 14. Check if a certain company exists
company_exists = "Amazon" in it_companies
print(f"Does Amazon exist in the list? {company_exists}")

# 15. Sort the list
it_companies.sort()
print(f"Sorted list: {it_companies}")

# 16. Reverse the list in descending order
it_companies.reverse()
print(f"List in descending order: {it_companies}")

# 17. Slice out the first 3 companies
first_three = it_companies[:3]
print(f"First three companies: {first_three}")

# 18. Slice out the last 3 companies
last_three = it_companies[-3:]
print(f"Last three companies: {last_three}")

# 19. Slice out the middle company or companies
mid_index = len(it_companies) // 2
if len(it_companies) % 2 == 0:  # Even number of elements
    middle_companies = it_companies[mid_index-1:mid_index+1]
else:  # Odd number of elements
    middle_companies = [it_companies[mid_index]]
print(f"Middle company/companies: {middle_companies}")

# 20. Remove the first IT company
it_companies.pop(0)
print(f"List after removing the first company: {it_companies}")

# 21. Remove the middle company or companies
mid_index = len(it_companies) // 2
if len(it_companies) % 2 == 0:  # Even number of elements
    del it_companies[mid_index-1:mid_index+1]
else:  # Odd number of elements
    del it_companies[mid_index]
print(f"List after removing the middle company/companies: {it_companies}")

# 22. Remove the last IT company
it_companies.pop()
print(f"List after removing the last company: {it_companies}")

# 23. Remove all IT companies
it_companies.clear()
print(f"List after clearing all companies: {it_companies}")

# 24. Destroy the IT companies list
del it_companies
# Uncommenting below would throw an error as the list is deleted
# print(it_companies)

# 25. Join two lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
joined_list = front_end + back_end
print(f"Joined list: {joined_list}")

# 26. Copy joined list and insert Python and SQL after Redux
full_stack = joined_list.copy()
redux_index = full_stack.index("Redux")
full_stack[redux_index + 1:redux_index + 1] = ["Python", "SQL"]
print(f"Full stack list: {full_stack}")
