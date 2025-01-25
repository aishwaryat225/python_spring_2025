# 1. Concatenate strings to 'Thirty Days Of Python' and 'Coding For All'
str1 = "Thirty"
str2 = "Days"
str3 = "Of"
str4 = "Python"
result1 = f"{str1} {str2} {str3} {str4}"
print(result1)

str5 = "Coding"
str6 = "For"
str7 = "All"
result2 = f"{str5} {str6} {str7}"
print(result2)

# 2. Assign 'Coding For All' to the variable company and print it
company = "Coding For All"
print(company)

# 3. Print the length of the string using len() and print()
print(len(company))

# 4. Change all characters to uppercase and lowercase
print(company.upper())
print(company.lower())

# 5. Format the string using capitalize(), title(), swapcase()
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 6. Cut (slice) out the first word of the string
print(company[7:])  # Removes the first word "Coding"

# 7. Check if the string contains the word "Coding"
print("Coding" in company)

# 8. Replace "Coding" with "Python"
print(company.replace("Coding", "Python"))

# 9. Replace "Python for Everyone" with "Python for All"
sentence = "Python for Everyone"
print(sentence.replace("Everyone", "All"))

# 10. Split the string 'Coding For All'
print(company.split())

# 11. Split the string "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" at the commas
tech_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(tech_companies.split(", "))

# 12. Character at index 0 in 'Coding For All'
print(company[0])

# 13. Last index of the string 'Coding For All'
print(len(company) - 1)

# 14. Character at index 10
print(company[10])

# 15. Create acronyms
acronym1 = "".join(word[0] for word in "Python For Everyone".split())
print(acronym1)

acronym2 = "".join(word[0] for word in company.split())
print(acronym2)

# 16. Find the position of the first occurrence of 'C' and 'F'
print(company.index("C"))
print(company.index("F"))

# 17. Find the last occurrence of 'l' using rfind
print("Coding For All People".rfind("l"))

# 18. Find the position of the first occurrence of 'because'
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.find("because"))

# 19. Find the last occurrence of 'because'
print(sentence.rfind("because"))

# 20. Slice out the phrase 'because because because'
start = sentence.find("because")
end = sentence.rfind("because") + len("because")
print(sentence[:start] + sentence[end:])

# 21. Does 'Coding For All' start with 'Coding'? End with 'coding'?
print(company.startswith("Coding"))
print(company.endswith("coding"))

# 22. Remove trailing spaces
trimmed = "   Coding For All      "
print(trimmed.strip())

# 23. Check which variables are valid identifiers
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

# 24. Join the list of Python libraries with a hash
libraries = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
print(" # ".join(libraries))

# 25. Use new line escape sequence
print("I am enjoying this challenge.\nI just wonder what is next.")

# 26. Use tab escape sequence
print("Name\t\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

# 27. String formatting for circle area
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {int(area)} meters square.")

# 28. String formatting for basic arithmetic
a, b = 8, 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")

