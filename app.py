
#! Strings And Variables

# print hello world
print("Hello World")

#make variables
name= "Mustafa"
age= 18

#adding variables to text
name="Mustafa"
print("My name is "+name)

#breaking line
print("Mustafa\nWalid")

#adding 4 spaces (tab)
print("Mustafa\tWalid")

#capitalizing & lowecasing strings
name="Mustafa"
print(name.upper())
print(name.lower())

#Checking if its capital or lowcase
name="Mustafa"
print(name.isupper())
print(name.islower())

#checking string length (output: 7)
name="Mustafa"
print(len(name))
print(len("Mohamed"))

#getting specific letter from string (counting starts from 0)
name="Mustafa"
print(name[0])

#getting letters from different strings (output: M H)
name="Mustafa"
name2="Hamada"
print(name[0], name2[0])

#To check position specific character/s in string (output: 2)
name="Mustafa"
print(name.index("s"))

#replace part of string (Output: VirusPlus)
name="VirusMinus"
print(name.replace("Minus","Plus"))




#?-----------------------------------------
#! Numbers and Inputs
#numbers and math operations
print(3)
print(3+5)
print((3*5)+2/3-5)
print(2.3454*7.19929)
print(10%2)

#printing numbers with strings must convert the number to string
number= 5
print(str(number)+" is my favorite number")

#absolute (not negative) and power
number2= -9
print(abs(number2))

number= 3
print(pow(number,3))

#max/min number

number1= 5
number2= 10
print(max(number1,number2))
print(min(number1,number2))

#normal rounding number
number= 3.7
print(round(number))

#importing math library (* means all)/ using floor which rounds down (only used in math library)
from math import *
number= 5.7
print(floor(number))

#round up number
from math import *
number= 5.2
print(ceil(number))

#square root
from math import *
number= 81
print(sqrt(number))

#getting input form user
name= input("Enter your name: ")
print("Hello "+name)

#getting numbers and adding them from user (if numbers are decimals use float instead of int )
n1= input("Enter First Number: ")
n2= input("Enter Second Number: ")
result=int(n1)+int(n2)
print(result)
#?-----------------------------------------------------------------------------




#! Lists and tuples

#Making a list

Mylist=[1,"Virus",True,["Mustafa",5]]
print(Mylist)s

#showing specific list values #*(counting starts from 0, using negative values starts from end)
Mylist=[1,"Virus",True,["Mustafa",5]]
print(Mylist[0])

#Choosing Multiple List Items (Virus and Python), from 1 to before 3
friends= ["Mustafa","Virus","Python","Programing"]
print(friends[1:3])

#Choosing list item and all after it (Virus,Python,Programming)
friends= ["Mustafa","Virus","Python","Programing"]
print(friends[1:])

#Editing list item (changing Mustafa to Mohamed)
friends= ["Mustafa","Virus","Python","Programing"]
friends[0]= "Mohamed"
print(friends)

#Merging 2 lists (way1)
friends1=["Mustafa", "Mohamed"]
friends2=["Virus","Minus"]
friends1.extend(friends2)
print(friends1)

#Merging 2 lists (way2)
friends1=["Mustafa", "Mohamed"]
friends2=["Virus","Minus"]
friends1 += friends2
print(friends1)

#Adding Item to list
friends=["Mustafa", "Mohamed"]
friends.append("Walid")
print(friends)

#Adding Item in specific place
friends=["Mustafa", "Mohamed"]
friends.insert(1,"Walid")
print(friends)

#Removing Item
friends=["Mustafa", "Mohamed"]
friends.remove("Mustafa")
print(friends)

#Removing all items in a List
friends=["Mustafa", "Mohamed"]
friends.clear()
print(friends)

#Removing last item in a List
friends=["Mustafa", "Mohamed"]
friends.pop()
print(friends)

#finding list item index
friends=["Mustafa", "Mohamed"]
print(friends.index("Mohamed"))

#How many of specific item in that list
friends= ["Mustafa","Virus","Programming","Programming"]
print(friends.count("Programming"))

#sorting list alphabetically/ascending
friends= ["Mustafa","Virus","Python","Programing"]
friends.sort()
print(friends)

#copying a list (its shallow copied which means if we changed the original nothing will happen in the copied one)
friends= ["Mustafa","Virus","Python","Programing"]
list_new= friends.copy()
print(list_new)

#copying a list (NOT SHALLOW COPYING)
friends= ["Mustafa","Virus","Python","Programing"]
list_new= friends
print(list_new)
#?---------------------------------------------------------------




#! Tuples (data type) its like a constant list

#making a tuple (cant be changed afterwards)
coordinates= (2,5)
print(coordinates)

#Finding Tuple item by index
coordinates= (2,5,6,10)
print(coordinates[2])

#list of tuples
list_of_tuples= [(2,3),(5,6),(2,6)]
print(list_of_tuples)

#specific item inside list of tupleds (2) first 0 for list second 0 for tuple
list_of_tuples= [(2,3),(5,6),(2,6)]
print(list_of_tuples[0][0])

#?--------------------------------------------




#! Functions

#declaring functiom
def say_hi():
    print("hello")

say_hi()

#parameters (treat it as a variable)
def say_hi(name,age):
    print("Hello "+name+" You are "+str(age)+" years old")

say_hi("Mustafa", 18)

#parameter can take all data types

def say_hi(name, age, True, False, [1,"string"], (12,30)):

#Returning values(return should be in last line) (doing stuff with parameter before getting it out of the function)
def cube(num):
    return num*num*num
result= cube(3)
print(result)

#returning example (sum)

def sum(num1,num2):
    return num1+num2
sum_result= sum(2,3)

print(sum_result)

#?----------------------------------------------




#! If Conditionals

#structure

hungry= False
want_to_eat= False

if hungry or want_to_eat:
    print("Order Food")
elif hungry and not want_to_eat:
    print("Order Food")
elif not hungry and want_to_eat:
    print("Dont Order Food")
else:
    print("Do Nothing"
    )

#Max Number if with function
def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif  num2>=num1 and num2>=num3:
        return num2
    else:
        return num3

result=max_num(5, 5,5)
print(result)

#built-in max function
print(max(1,2,3))

#Matching strings

def match_strings(word1, word2):
    if word1 == word2:
        print("Matching")
    else:
        print("Different")

result=match_strings("Mustafa", "Mustafa")
print(result)

#!-------------------------------------------------------------------




#?Dictionaries

#Dictionary Structure (keys must be unique, can be numbers)

dictionary_name= {
    "key": "Value",
    "Key2": "Value"
}

#Getting Values from Dictionary
convert_month= {
    "jan": "january",
    "feb": "february",
    "mar": "march"
}

print(convert_month["jan"])
#* or
print(convert_month.get("feb"))

#Making Error Messages When writing wrong keys

convert_month= {
    "jan": "january",
    "feb": "february",
    "mar": "march"
}

print(convert_month.get("mustafa","The Value Doesn't Exist"))

#All datatypes in dictionary
convert_month= {
    "jan": "january",
    "2": True,
    "mar": ["march", "march is the 3rd month"]
}

print(convert_month.get("mar","This Key Doesnt't Exist"))


#?-------------------------------------------------------------




#!Loops

#While Loop
i=0

while i<=10:
    print(i)
    i+=1
else:
    print("The Condition Is not true")


#infinite loop
i=0
while True:
    print(i)
    i+=1


#Skipping Iteration (1,2,3,4,5,7,8,9,10,11)
i=0

while i<=10:
    i+=1
    if i==6:
        continue
    print(i)




#Getting Out Of loop (1,2,3,4,5)
i=0

while i<=10:
    i+=1
    if i==6:
        break
    print(i)




#For Loop Struture
for letter in "VirusMinus":
  print(letter)



#For Loop in list
agents= ["Cypher","Jett","Phoenix","Sage"]
for agent in agents:
  print(agent)




  #For Loop in numbers (Range(10) not including 10)
for x in range(10):
  print(x)



#For Loop in specific range (not including 20)
for x in range(5,20):
  print(x)



#getting length of list or string
agents= ["cypher","jett","breach"]
name="VirusMinus"
print(len(agents))
print(len(name))



agents=["cypher","jet","raze"]



#knowing index of all list
agents=["cypher","jet","raze"]
for index in range(len(agents)):
  print(index)



#knowing index of all chars in string
name="VirusMinus"
for index in range(len(name)):
  print(index)



#printing list in other way
agents=["cypher","jet","raze"]
for index in range(3):
  print(agents[index])



#odd or even number
for number in range(10):
  if number%2==0:
    print(number," is even")
  else:
    print(number," is odd")

You unsent a message



#searching for specific name in the list (you can use else,continue,break)
agents=["cypher","jet","raze"]
for agent in range(len(agents)):
  if agents[agent]=="jet":
    print(agent," found")
  else:
    print(agent, "Not Found")



#searching for specific name and gets it only
agents=["cypher","jet","raze"]
for agent in range(len(agents)):
  if agents[agent]=="jet":
    print(agent," found")
    break
else:
 print(agent, "Not Found")



#choosing some numbers exept some numbers (continue)
for x in range(0,10):
  if x==5:
    continue
  else:
    print(x, " Is the chosen number")


#number power number (num^num)
print(3**3)




#power function

def power(base_num, power_num):
    result=1
    for x in range(power_num):
        result=result*base_num
    return result

print(power(5,5))




#2D list to print 8 , [row][column]
no_list=[
  [1,2,3],
  [4,5,6],
  [7,8,9],
  [0]
]

print(no_list[2][1])



#Printing Each Value in 2D List
no_list=[
  [1,2,3],
  [4,5,6],
  [7,8,9],
  [0]
]

for row in no_list:
  for column in row:
    print(column)



#handling errors so not all project sstop wihen facing 1 Error
try:
  result=10/0
  value=int(input("Enter Number: "))
  print(value)
except ZeroDivisionError as err:
  print(err)
except ValueError as err1:
  print(err1)

print("Success")


#!----------------------


#?Reading and writing file
#opening print next parameter can be "r", "w" for writing,"a" for appending (writing only in last line),"r+" for read and writing at same time if file not there it will be created
open("workers.txt","read")



#Checking if file is readable (best practice to close the file after wrting the open so that you dont forget later

workers_file= open("workers.txt","r")
print(workers_file.readable())
workers_file.close()

#Reading file

workers_file= open("workers.txt","r")
print(workers_file.read())
workers_file.close()



#Reading line by line from a  file

workers_file= open("workers.txt","r")
print(workers_file.readline())
print(workers_file.readline())
print(workers_file.readline())

workers_file.close()



#Reading all lines and putting them in a list

workers_file= open("workers.txt","r")
print(workers_file.readlines())
workers_file.close()



#Reading specific line/s and putting them in a list if one line it will not be in list

workers_file= open("workers.txt","r")
print(workers_file.readlines()[0:2])
workers_file.close()



#reading by using for loop and manipulating the file

workers_file= open("workers.txt","r")
for worker in workers_file:
  print(worker+"is cool")


#if you opened a file you dont have it will be created

open("writing.txt","a")



#Writing in file last line
workers_file= open("workers.txt","a")
workers_file.write("\nRaze Explosion Master")
workers_file.close()



#You Can create any file with any extension with python



#writing more than a line
writing_file= open("writing.txt","a")
list_of_phrases= ["Mustafa","\nHamada","\nHamza"]
writing_file.writelines(list_of_phrases)
writing_file.close()

#?------------------------------



#!Modules
#You can access other file's even you can creater the file and import from it variables, functions using modules
import module_name

#installing a not built-in python module
#search google for the module (python docx)
#check the documentation
#pip install python-docx

import docx


#?-----------------------------------
#!Objects and classes (making your own datatype)
#to import class
from file_name import class_name



#making class that describes employee
class Employee:
  def __init__(self, name, age, department, is_manager):
    self.name= name
    self.age= age
    self.department= department
    self.is_manager= is_manager


#using employee class
from app.py import Employee

employee1= Employee("Mustafa", 18, Hacking, False)
employee2= Employee("Virus", 18, Data Analysis, True)

print(employee1.name)
print(employee1.age)


#When I started learning OOP it took me a while to differentiate between methods types, so if you are struggling with that too, here's a quick summary:

#Method = function related to that instance of a class. Use this type it when you are using values of the own instance (its own name, age, etc). You need to create one instance to use it.

#Classmethod = function related to that class and that class only. Use this type when you are using values of the class, not the instance (For example, using a class that retrieves the total count of instances of that Class created and stored in a class variable). You don't need to create one instance to use it.

#Staticmethod = function not related to that class. Used for organization purposes (For example, a Calculator class with add, subtract, multiplicate, etc methods). You don't need to create one instance to use it.



#!------------------------------------------------------------
#? Intermediate

#Map() it is used to add a function in a list without typing alot
#we need to Make every obejct in the list ^2

def power(list):
  return list**2

nums= [1,2,3,4]
print(list(map(power,nums)))

#Printing list in one/same line
li= [1,2,3,4]
print(''.join(map(str,li)))


#?Dictionaries
#initializing
d={} #or  d={"Mustafa": 18, "Hamada": 15}
#adding values
d["Mustafa"]= 24
d["Virus"]=18
#Changing Values
d["Mustafa"]= 20
print(d["Mustafa"])
#Mustafa is the key and keys can be only strings or numbers, values can be anything

#iterating through dictionary
for key, value in d.items():
  print("Key: ")
  print(key)
  print("Value: ")
  print(value)
  print(" ")


#Optional Parameters (if we specified a value to the parameter it will not give an error when we dont't type a parameter so it becomes optional)
def power(x=1):
  return x**2

result =power(5) #overrites the parameter
print(result)

def func(name, freq=1):
  return name*freq

res1= func("Mustafa ", 5)
res2= func("Mustafa ")

print(res1)
print(res2)




#Class Method & Static Method
class Person():
  population = 50
  def __init__(self, name, age):
    self.name= name
    self.age= age

  @classmethod      #decorator to tell python this is a class method(can be called without making object, can access anything public on the class like 'population')
  def get_population(cls): #parameter 'cls' means its not taking object which takes 'self' but it's taking class
    return cls.population

  @staticmethod
  def isAdult(age): #similar to class method but doesnt take 'self' or 'cls' (used when u dont need self or the actual object, cant access anytres1= func("Mustafa ", 5)hing public in the class )
    return age>=18

  def display(self):
    print(self.name, 'is',self.age,'years old')




person1= Person("Mustafa",18)

print(Person.get_population())
print(Person.isAdult(21))
print(person1.display())



#filter(), it filters list ((e.g: filter odd numbers only from list))
def isOdd(n):
  return n%2 != 0

def add7(x):
  return x+7

a= [1,2,3,4,5,6,7,8,9,10]
b= list(filter(isOdd,a))
print(b)
c=list(map(add7,b)) #combining map and filter so that map adds 7 to every filtered odd number fromn 'a' list
print(c)


#Lambda (mini function, anonymous function, when your functuion fits on one line, can have multiple parameters, can have optional parameters)

#* normal function
def func(x):
  return x+5

print(func(5))

#* lambda function
#*lambda parameter: 'return is invisible'
func2= lambda x : x+5
print(func2(10))


#lambda inside function
def func(x):
  func2= lambda x: x+5
  return func2(x)+85

print(func(5))

#lambda inside map() this saves lines and makes the code look cleaner so that we dont define a function for small things

a=[1,2,3,4,5,6,7,8,9,10]

b= list(map(lambda x: x+5, a))
print(b)

#lambda with filter
a=[1,2,3,4,5,6,7,8,9,10]

b= list(filter(lambda x: x%2==0, a))
print(b)