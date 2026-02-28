student=["sumit", "kumar", "patel", 23, 5.9, True]
print(student)
print(type(student))
student[0]="karan" #list is mutable
print(student)
print(student[0])
print(student[1])
print(student[2])
print(student[3])
print(student[4])
print(student[5])
print(student[-1])
print(student[-2])
print(student[-3])
print(student[-4])
print(student[0:3])
print(student[3:6])
print(student[-6:-3])
print(student[-3:])

list=[1, 2, 3]
list.append(4) #add an element to the end of the list
print(list)
list.sort() #sort the list in ascending order
print(list)
list.sort(reverse=True) #sort the list in descending order
print(list)
list.reverse() #reverse the order of the list
print(list)
list.extend([5, 6]) #add multiple elements to the end of the list
print(list)
list.insert(1, 5) #add an element at a specific index
print(list)
list.remove(2) #remove an element by value
print(list)
list.pop() #remove the last element
print(list)
list.pop(0) #remove an element by index
print(list)
list.clear() #remove all elements from the list
print(list)
list.copy() #create a copy of the list
print(list)

#tuple in python
student=("sumit", "kumar", "patel", 23, 5.9, True)
print(student)
print(type(student))
print(student[0])
print(student[1])
print(student[2])
print(student[3])
print(student[4])
print(student[5])
print(student[-1])
print(student[-2])
print(student[-3])
print(student[-4])
print(student[0:3])
print(student[3:6])
print(student[-6:-3])
print(student[-3:]) 

#tuple methods
tuple=(1, 2, 3, 4, 5)
print(tuple)
print(tuple.count(2)) #count the number of occurrences of an element
print(tuple.index(3)) #find the index of the first occurrence of an element

#write a program to ask user to enter name of their 3 favorite fruits and store them in a list and print the list
fruits=[]
for i in range(3):
    fruit=input("Enter the name of your favorite fruit: ")
    fruits.append(fruit)
print("Your favorite fruits are: ", fruits)
