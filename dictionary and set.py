from turtle import st


dict = {
    "name": "sumit",
    "age": 18,
    "city": "New delhi",
    "is_student": True,
    "subjects": ["math", "science", "english"],
    "hobbies": ("reading", "coding", "gaming")
}
print(dict)
print(dict["name"])
print(dict["age"])
print(dict["city"])
print(dict["is_student"])
print(dict.get("name"))
print(dict.get("age"))
print(dict.get("city"))
print(dict.get("is_student"))
print(dict.keys())
print(dict.values())
print(dict.items())
dict["age"] = 19 #update the value of an existing key
print(dict)
dict["country"] = "India" #add a new key-value pair to the dictionary
print(dict)
dict.pop("city") #remove a key-value pair by key
print(dict)         

#nested dictionary
student = {
    "name": "sumit",
    "age": 18,
    "subjects": {
        "math": 90,
        "science": 85,
        "english": 95
    }
}
print(student)
print(student["subjects"])
print(student["subjects"]["math"])

#dictionary methods
student = {
    "name": "sumit",
    "age": 18,
    "city": "New delhi",
}
print(student.keys()) #return a tuple of the dictionary's keys
print(student.values()) #return a list of the dictionary's values
print(student.items()) #return a list of the dictionary's key-value pairs
print(student.get("name")) #return the value of the specified key
sumit_dict={"age":19} #create a new dictionary with the updated age
student.update(sumit_dict) #update the value of an existing key
print(student)

#set in python
my_set = {1, 2, 3, 4, 5}
print(my_set)
print(type(my_set))
print(len(my_set))
my_set.add(6) #add an element to the set
print(my_set)       

#set methods
set1 = {1, 2, 3}
set1.add(4) #add an element to the set
print(set1)
set1.update({5, 6}) #add multiple elements to the set
print(set1)
my_set1 = my_set.copy() #create a copy of the set
my_set1.remove(3) #remove an element from the set
print(my_set1)
my_set1.discard(4) #remove an element from the set without raising an error if it does not exist
print(my_set1)
my_set1.pop() #remove and return an arbitrary element from the set
print(my_set1 )
my_set1.clear() #remove all elements from the set
print(my_set1)       
my_set1 = my_set1.copy() #create a copy of the set
print(my_set1)
my_set1 = my_set.copy() #create a copy of the set
my_set1 = my_set1.union({7, 8, 9}) #return a new set that is the union of two sets
print(my_set1)
my_set1 = my_set1.intersection({2, 3, 4}) #return a new set that is the intersection of two sets
print(my_set1)
my_set1 = my_set1.difference({2, 3, 4}) #return a new set that is the difference of two sets
print(my_set1)
my_set1 = my_set1.symmetric_difference({2, 3, 4}) #return a new set that is the symmetric difference of two sets
print(my_set1)  

#practoice problems

#store following word meanings in a python dictonary 
word_meanings = {
    "python": "a high-level programming language",
    "dictionary": "a collection of key-value pairs",
    "set": "a collection of unique elements",
    "list": "a collection of ordered elements",
    "tuple": "a collection of ordered, immutable elements"
}
print(word_meanings)

#you are give a list of subject for students. assume one classroom is required for 1 subject.how many classrooms are needed by all the students in the school
subjects = ["math", "science", "english", "history", "geography"]
classrooms_needed = len(subjects)
print("Number of classrooms needed:", classrooms_needed)

#write a pyhon program to enter marks of 3 subjects from the user and store them in a dictionary.start with an empty dictionary & add one by one.use subject name as key and marks as value. finally print the dictionary
marks = {}
for i in range(3):
    subject = input("Enter the subject name: ")
    mark = int(input("Enter the marks: "))
    marks[subject] = mark
print(marks)    

#figure out a way to store 9 & 9.0 as seprate valuse in the set.(you can take help of built-in-data types)
numbers = {9, 9.0}
print(numbers)      