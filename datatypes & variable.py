#arithmetic operations
a=5
b=10
print(a+b)
print(a*b)
print(a/b)
print(a-b)
print(a%b) #remainder
print(a**b) #exponentiation

#relational operators
a=50
b=20
print(a==b) #equal to
print(a!=b) #not equal to
print(a>b) #greater than
print(a<b) #less than
print(a>=b) #greater than or equal to
print(a<=b) #less than or equal to

#assignment operators
a=10
a+=5 #a=a+5
print(a)
a-=3 #a=a-3
print(a)
a*=2 #a=a*2
print(a)
a/=4 #a=a/4
print(a)
a%=3 #a=a%3
print(a)
a**=2 #a=a**2
print(a)

#logical operators
a=10
b=20
print(a>5 and b>15) #logical AND
print(a>15 or b>15) #logical OR
print(not(a>5 and b>15)) #logical NOT

#tpe casting
a=10
b=3.14
c=str(a) #casting integer to string
d=int(b) #casting float to integer
print(c)
print(d)

__name__ = input("Enter your name: ")
print("Hello, " + __name__ + "! Welcome to Python programming.")#all values always a string in input() function

int("50") #casting string to integer
float("3.14") #casting string to float
str(100) #casting integer to string
int_a = int(input("Enter an integer: "))
float_b = float(input("Enter a float: "))
string_c = input("Enter a string: ")
print("You entered the integer:", int_a)
print("You entered the float:", float_b)
print("You entered the string:", string_c)

#practice problems
#1. Write a Python program to calculate the area of a circle given its radius.
import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
print("The area of the circle is:", area)

#practice problem 2
#Write a Python program to add first and second number entered by the user and display the result.

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
sum = first_number + second_number
print("The sum of the two numbers is:", sum)

#practice problem 3
#write a python program input two floating point numbers & print their average
first_number = float(input("Enter the first floating point number: "))
second_number = float(input("Enter the second floating point number: "))
average = (first_number + second_number) / 2
print("The average of the two numbers is:", average)

#practice problem 4
# write a pyhon program to input two numbers ,a and b, print true if a is greter than or equal to b, otherwise print false.
a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))
result = a >= b
print(result)