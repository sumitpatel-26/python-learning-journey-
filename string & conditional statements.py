#indexing 
from unicodedata import name


str = "sumit kumar patel"
print(str)
print(str[0])
print(str[1])
print(str[2])
print(str[3])
print(str[4])
print(str[5])
print(str[6])
print(str[7])
print(str[8])
print(str[9])
print(str[-1])
print(str[-2])
print(str[-3])
print(str[-4])
print(str[-5])
#slicing
le = len(str)
print("Length of the string is:", le)
print(str[0:5])
print(str[6:11])
print(str[-5:-1])
print(str[-11:-6])

#string functions
print(str.upper())
print(str.lower())
print(str.title())
print(str.capitalize())
print(str.count("a"))
print(str.find("kumar"))
print(str.replace("patel", "singh"))

str1 = "i am a student"
print(str1.endswith("student"))

#practice questions
#write a program to input users first name & print the length of the name
first_name = input("Enter your first name: ")
length = len(first_name)
print("The length of your first name is:", length)

#write a program find the occurrence of a $ in a string
str = "I have $50 in my wallet."
print("The occurrence of '$' in the string is:", str.count("$"))

#conditional statements

#write a program to voting eligibility using conditional statements
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
elif age < 18 and age >= 0:
        print("You are not eligible to vote.")
else:
    print("You are not eligible to vote.")
    
 #write a program to traffic light system using conditional statements   
light = input("Enter the traffic light color (red, yellow, green): ")
if light == "red":
    print("Stop")
elif light == "yellow":
    print("Caution")
elif light == "green":
    print("Go")
else:    print("Invalid traffic light color")

#write a program to student grade based on marks using conditional statements
marks = int(input("Enter the student's marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")
    
    #nested if statements
    #write a program to check if a number is positive, negative or zero using nested if statements
num = float(input("Enter a number: "))
if num >=1:
    if num == 0:
        print("The number is zero.")
    else:
        print("The number is positive.")
else:
    print("The number is negative.")
    
#practice questions
#write a program to check if a numer entered by the the user id odd or even
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:    print("The number is odd.")

#write a program the gratest of three numbers entered by the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if num1 >= num2 and num1 >= num3:
    print("The greatest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("The greatest number is:", num2)
else:
    print("The greatest number is:", num3)
    
#write a program to check if a number is multiple of 7 or not
number = int(input("Enter a number: "))
if number % 7 == 0:
    print("The number is a multiple of 7.")
else:    print("The number is not a multiple of 7.")