#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1.Write a Python program to print the following string in a specific format (see theoutput).
print("Twinkle,twinkle, little star", 
      "\n\tHow I wonder what you are!" 
      "\n\t\tUp above the world so high," 
      "\n\t\tLike a diamond in the sky." 
      "\nTwinkle, twinkle, little star," 
      "\n\tHow I wonder what you are!")


# In[4]:


#2.Write a Python program to get the Python version you are using
#'sys' module provides access to some variables used or maintained 
#by the interpreter and to functions that interact strongly with the interpreter.
import sys
print("Python version")
print (sys.version)


# In[7]:


#3.Write a Python program to display the current date and time.
from datetime import datetime
now = datetime.now()
print (now.strftime("%Y-%m-%d %H:%M:%S"))


# In[8]:


#4.Write a Python program which accepts the radius of a circle from the user and compute the area.
from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))


# In[9]:


#5.Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)


# In[10]:


#6.Write a python program which takes two inputs from user and print them addition
a = int(input("enter first number: "))
b = int(input("enter second number: "))
 
sum = a + b
 
print("sum:", sum)


# In[12]:


#7.Write a program which takes 5 inputs from user for different subject’s marks, total it and generate mark sheet using grades 
print("Enter Marks Obtained in 5 Subjects: ")
print("Enter marks in Matlab")
Matlab = int(input())
print("Enter marks in Web")
Web = int(input())
print("Enter marks in Machine Learning")
Machine_Learning = int(input())
print("Enter marks in Networking")
Networking = int(input())
print("Enter marks in Cloud Computing")
Cloud_Computing = int(input())

tot = Matlab+Web+Machine_Learning+Networking+Cloud_Computing
avg = tot/5

if avg>=91 and avg<=100:
    print("Your Grade is A1")
elif avg>=81 and avg<91:
    print("Your Grade is A2")
elif avg>=71 and avg<81:
    print("Your Grade is B1")
elif avg>=61 and avg<71:
    print("Your Grade is B2")
elif avg>=51 and avg<61:
    print("Your Grade is C1")
elif avg>=41 and avg<51:
    print("Your Grade is C2")
elif avg>=33 and avg<41:
    print("Your Grade is D")
elif avg>=21 and avg<33:
    print("Your Grade is E1")
elif avg>=0 and avg<21:
    print("Your Grade is E2")
else:
    print("Invalid Input!")


# In[13]:


#8.Write a program which take input from user and identify that the given number is even or odd?
num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")


# In[15]:


#9.Write a program which print the length of the list?
# Initializing list 
test_list = [ 1, 4, 5, 7, 8 ]  
# Printing test_list
print ("The list is : " + str(test_list)) 
# Finding length of list  # using loop # Initializing counter
counter = 0
for i in test_list:    
    # incrementing counter
    counter = counter + 1
# Printing length of list 
print ("Length of list using naive method is : " + str(counter))


# In[17]:


#10.Write a Python program to sum all the numeric items in a list?
def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print("Sum of the List is ")
print(sum_list([1,2,-8]))


# In[19]:


#11.Write a Python program to get the largest number from a numeric list.
def max_num_in_list( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print(max_num_in_list([1, 32, -8, 0]))


# In[20]:


#12. Take a list, say for example this one:
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#Write a program that prints out all the elements of the list that are less than 5
test_list= [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for element in test_list:
    if(int(element) <5):
        print(str(element)+"\n")


# In[ ]:




