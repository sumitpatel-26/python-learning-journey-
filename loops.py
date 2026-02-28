#while loop
i = 0
while i >=-5: #stop the loop when i is less than -5
    print("hello", i)
    i -= 1
    
    #print numbers from 1 to 10
i = 1
while i <= 10: #stop the loop when i is greater than 10
    print(i)
    i += 1
    
    #print numbers from 10 to 1
i = 10
while i >= 1: #stop the loop when i is less than 1
    print(i)
    i -= 1
    
    #print even numbers from 1 to 10
i = 1
while i <= 10:     #stop the loop when i is greater than 10                   
    if i % 2 == 0: #check if the number is even
        print(i)
    i += 1
    
    #print odd numbers from 1 to 10
i = 1
while i <= 10: #stop the loop when i is greater than 10
    if i % 2 != 0: #check if the number is odd
        print(i)
    i += 1
    
    #print the muitiplication table of a number n
n = int(input("Enter a number: "))
i = 1
while i <= 10: #stop the loop when i is greater than 10
    print(n, "x", i, "=", n * i) #print the multiplication of n and i       
    i += 1
    
    #print the elements of a list using while loop
my_list = [1, 2, 3, 4, 5]
i = 0
while i < len(my_list): #stop the loop when i is greater than or equal to the length of the list
    print(my_list[i]) #print the element at the current index of the list
    i += 1
    
    #search for a number x in this tuple using loop
my_tuple = (1, 2, 3, 4, 5)
x = int(input("Enter a number to search: "))
i = 0
found = False
while i < len(my_tuple): #stop the loop when i is greater than or equal to the length of the tuple
    if my_tuple[i] == x: #check if the element at the current index of the tuple is equal to x
        found = True
        break #exit the loop if x is found
    i += 1
if found:
    print(x, "is found in the tuple.")
else:    print(x, "is not found in the tuple.")

#break statement
i = 1
while i <= 10:
    if i == 5:
        break #exit the loop when i is equal to 5
    print(i)
    i += 1
    
    #continue statement
i = 1
while i <= 10:
    if i == 5:
        i += 1
        continue #skip the rest of the loop when i is equal to 5
    print(i)
    i += 1
    
    #for loop
for i in range(1, 11): #loop from 1 to 10
    print(i)
    
    #for loop else statement
for i in range(1, 11):
    print(i)
else:    print("Loop is finished.")

#print the ements of the followig list using for loop
my_list = [1, 2, 3, 4, 5]
for element in my_list: #loop through each element in the list
    print(element)
    
    #print the keys and values of the following dictionary using for loop
my_dict = {"a": 1, "b": 2, "c": 3}
for key, value in my_dict.items(): #loop through each key-value pair in the dictionary
    print(key, ":", value)
    
    #search for a number x in this tuple using for loop
my_list = [1, 2, 3, 4, 5]
x = int(input("Enter a number to search: "))
found = False
for element in my_list: #loop through each element in the list
    if element == x: #check if the current element is equal to x
        found = True
        break #exit the loop if x is found
if found:    print(x, "is found in the list.")
else:    print(x, "is not found in the list.")

#range function
for i in range(2,10,2):
    print(i)
    
    #practice question
    
    #print numbers from 1 to 100
    for i in range(100,0,-1):
        print(i)
        
        
        #print the multipliction table of a number n
        n = int(input("enter number :"))
        for i in range(1,11):
            print(n*i)
            
            #pass statement
            for i in range(5):
                pass
            print("some useful work")
            
            #write to find the sum of first n number .(using while loop)
            n=5
            sum=0
            while i<=n:
                sum+=i
                i+=1
                print("total sum=",sum)
                
                
            
            
            
            