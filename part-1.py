#1. Write a Python program to print the following string in a specific format (see the output).
#Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"

#solution:

print("Twinkle, twinkle, little star,\n\t How I wonder what you are!\n Up above the world so high,\n \tLike a diamond in the sky.\n Twinkle, twinkle, little star,\n\t How I wonder what you are")

#2. Write a Python program to get the Python version you are using.

#solution:
import sys
print("python version")
print(sys.version)
print("version_info")
print(sys.version_info)

#output
# python version
# 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)]
# version_info
# sys.version_info(major=3, minor=6, micro=5, releaselevel='final', serial=0)

#3. Write a Python program to display the current date and time.

import datetime
now=datetime.datetime.now()
print("current date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))

#output
# current date and time :
# 2018-07-08 20:19:33

#4. Write a Python program which accepts the radius of a circle from the user and compute the area. Go to the editor

r=int(input("enter radius of circle : "))
pi=3.14
area=pi*r*r
print("Area of circle is : ",area)

#5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them. Go to the editor

fname=input("enter your first name: ")
lname=input("enter your last name: ")
print("hello"+" ",lname+" ",fname)

#6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. Go to the editor

n=input("enter a sequence of comma-separated numbers :  ")
list=n.split(",")
tuple=tuple(list)
print("list : ",list)
print("tuple : ",tuple)

