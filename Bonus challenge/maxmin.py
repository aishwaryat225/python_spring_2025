numbers = [12, 45, 2, 67, 34, 89, 1, 23]

# Find maximum and minimum manually
max_num = numbers[0]
min_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print(f"Maximum: {max_num}")
print(f"Minimum: {min_num}")
