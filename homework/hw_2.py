# -*- coding: utf-8 -*-
"""hw_2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_tUb7V8y1xDgCZ01LBjbwis19FC4T32w
"""

print("**************Login Page**************")

user_name = "Johnny"
password ="Crazy_stuff"

user_name1 =input("Please enter your user name = ")

password1= input("Please enter your password = ")

if (user_name != user_name1 and password == password1):
    print("Invalid user name")
elif (user_name==user_name1 and password != password1):
    print("Invalid Password")
elif (user_name != user_name1 and password!= password1):
    print("Invalid user name and password")
else:
    print("You are now logged in...")

print("**************Login Page**************")

user_name = "Johnny"
password ="Crazy_stuff"

user_name1 =input("Please enter your user name = ")

password1= input("Please enter your password = ")

dict_1 = {"Johnny":user_name1, "Crazy_stuff":password1}

if (user_name != user_name1 and password == password1):
    print("Invalid user name")
elif (user_name==user_name1 and password != password1):
    print("Invalid Password")
elif (user_name != user_name1 and password!= password1):
    print("Invalid user name and password")
else:
    print("You are now logged in...")