age = 31
heigh=152
complex_num = 1+2j
#Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

area = 0.5 * base * height
print("Area of the triangle:", area)

#Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).

side_a = float(input("Enter the side a of the triangle: "))
side_b = float(input("Enter the side b of the triangle: "))
side_c = float(input("Enter the side c of the triangle: "))

perimeter = side_a + side_b + side_c
print("Perimeter of the triangle:", perimeter)

#Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width
perimeter = 2 * (length + width)
print("Area of the rectangle:", area)
print("Perimeter of the rectangle:", perimeter)


#Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

radius = float(input("Enter the radius of the circle: "))

area = math.pi * radius * radius
circumference = 2 * math.pi * radius
print("Area of the circle:", area)
print("Circumference of the circle:", circumference)

#Calculate the slope, x-intercept and y-intercept of y = 2x -2

slope = 2
x_intercept = 0
y_intercept = -2

print("Slope:", slope)
print("X-intercept:", x_intercept)
print("Y-intercept:", y_intercept)  

#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
import math
x1 = 2
y1 = 2
x2 = 6
y2 = 10     

slope = (y2 - y1) / (x2 - x1)                       
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Slope:", slope)  
print("Euclidean distance:", distance)   

#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

import math

x = float(input("Enter the value of x: "))  

y = x**2 + 6*x + 9                   

print("The value of y is:", y)                                                              

if y == 0:                      
        print("At x =", x, "y is 0.")        
else:                                               
        print("At x =", x, "y is not 0.")                                                                                                                                                           


#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
word1 = "python"
word2 = "dragon"    

length1 = len(word1)                                                                                                                                          
length2 = len(word2)                                                                                                                                  

if length1 > length2:                                                                                                                                             
        print(word1, "is longer than", word2)                                                                                                             
else:                                                                                                                                                
        print(word2, "is longer than", word1)   
        
#Use and operator to check if 'on' is found in both 'python' and 'dragon'
word1 = "python"
word2 = "dragon"                                                                                                                                         
if "on" in word1 and "on" in word2:                                                                                                                             
        print("'on' is found in both", word1, "and", word2)                                                                                                  
else:                                                                                                                                                
        print("'on' is not found in both", word1, "and", word2)                                 
        
#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = "I hope this course is not full of jargon."                                                                                                           
if "jargon" in sentence:                                                                                                                                     
        print("jargon is found in the sentence")                                                                                                             
else:                                                                                                                                                       
        print("jargon is not found in the sentence")                                                                                                         

#Find the length of the text python and convert the value to float and convert it to string
text = "python"
length = len(text)                                                                          
float_length = float(length)
str_length = str(float_length)
print(str_length)       

#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = 10
if number % 2 == 0:                                                                                                                                            
        print(number, "is even")                                                                                                                             
else:                                                                                                                                                        
        print(number, "is odd")                                                                                                     
        
#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
result = 7 // 3
print(result == int(2.7))       

#Check if type of '10' is equal to type of 10
print(type('10') == type(10))       

#Check if int('9.8') is equal to 10
print(int('9.8') == 10)

#Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = input("Enter hours: ")
rate = input("Enter rate per hour: ")                                                                                               

try:
        hours = float(hours)
        rate = float(rate)
        pay = hours * rate
        print("Pay:", pay)
except ValueError:
        print("Error: Please enter valid numbers for hours and rate per hour.")
        
        
#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

years = int(input("Enter number of years: "))

seconds = years * 365 * 24 * 60 * 60
print("Number of seconds a person can live:", seconds)                                  

#Write a Python script that displays the following table

# Function to print the table
def display_table():
    # Print the header of the table
    print(f"{'n':<5}{'1':<5}{'n':<5}{'n^2':<5}{'n^3':<5}")
    print("-" * 25)
    
    # Loop through each row
    for n in range(1, 6):
        print(f"{n:<5}{1:<5}{n:<5}{n**2:<5}{n**3:<5}")

# Call the function to display the table
display_table()
        