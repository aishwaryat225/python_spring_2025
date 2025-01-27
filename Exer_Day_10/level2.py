# Sum of all numbers from 0 to 100
sum_all = 0
for i in range(101):
    sum_all += i
print("The sum of all numbers is:", sum_all)

# Sum of all evens and all odds from 0 to 100
sum_evens = 0
sum_odds = 0
for i in range(101):
    if i % 2 == 0:
        sum_evens += i
    else:
        sum_odds += i

print("The sum of all evens is:", sum_evens)
print("The sum of all odds is:", sum_odds)
