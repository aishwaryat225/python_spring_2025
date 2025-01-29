def calculate_grade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score <= 69:
        return "D"
    elif 0 <= score <= 59:
        return "F"
    else:
        return None

# Get user input
try:
    score = int(input("Enter your score: "))
    grade = calculate_grade(score)
    
    if grade:
        print(f"Your grade is: {grade}")
    else:
        print("Invalid score! Please enter a number between 0 and 100.")
except ValueError:
    print("Invalid input! Please enter a valid integer score.")
