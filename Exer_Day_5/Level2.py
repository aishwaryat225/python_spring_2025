# List of students' ages
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# 1. Sort the list and find the min and max age
ages.sort()
min_age = ages[0]
max_age = ages[-1]
print(f"Sorted ages: {ages}")
print(f"Min age: {min_age}, Max age: {max_age}")

# 2. Add the min age and max age again to the list
ages.extend([min_age, max_age])
print(f"Ages after adding min and max age: {ages}")

# 3. Find the median age
ages.sort()  # Ensure the list is sorted
n = len(ages)
if n % 2 == 0:  # Even number of items
    median_age = (ages[n // 2 - 1] + ages[n // 2]) / 2
else:  # Odd number of items
    median_age = ages[n // 2]
print(f"Median age: {median_age}")

# 4. Find the average age
average_age = sum(ages) / len(ages)
print(f"Average age: {average_age}")

# 5. Find the range of ages
age_range = max_age - min_age
print(f"Range of ages: {age_range}")

# 6. Compare (min - average) and (max - average) using abs()
min_avg_diff = abs(min_age - average_age)
max_avg_diff = abs(max_age - average_age)
print(f"|Min - Average|: {min_avg_diff}, |Max - Average|: {max_avg_diff}")

# 7. Find the middle country(ies) in the countries list
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
n_countries = len(countries)
if n_countries % 2 == 0:  # Even number of countries
    middle_countries = countries[n_countries // 2 - 1:n_countries // 2 + 1]
else:  # Odd number of countries
    middle_countries = [countries[n_countries // 2]]
print(f"Middle country(ies): {middle_countries}")

# 8. Divide the countries list into two equal lists
half = n_countries // 2
if n_countries % 2 == 0:  # Even number of countries
    first_half = countries[:half]
    second_half = countries[half:]
else:  # Odd number of countries
    first_half = countries[:half + 1]
    second_half = countries[half + 1:]
print(f"First half: {first_half}")
print(f"Second half: {second_half}")

# 9. Unpack the first three countries and the rest as scandic countries
first_country, second_country, third_country, *scandic_countries = countries
print(f"First three countries: {first_country}, {second_country}, {third_country}")
print(f"Scandic countries: {scandic_countries}")
