# Using for loop
for i in range(11):
    print(i)

# Using while loop
i = 0
while i <= 10:
    print(i)
    i += 1
# Using for loop
for i in range(10, -1, -1):
    print(i)

# Using while loop
i = 10
while i >= 0:
    print(i)
    i -= 1
# Triangle pattern
for i in range(1, 8):
    print('#' * i)
# 8x8 grid
for i in range(8):
    for j in range(8):
        print('#', end=' ')
    print()
# Multiplication pattern
for i in range(11):
    print(f"{i} x {i} = {i * i}")
# List iteration
items = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in items:
    print(item)
# Even numbers
for i in range(0, 101, 2):
    print(i)
# Odd numbers
for i in range(1, 101, 2):
    print(i)
