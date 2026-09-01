#1
user = input("Enter Any String: ")
print("First 5 Characters:",user[:6])
print("Last 4 Characters:",user[-4:])
print("Characters from index 2 to 8:",user[2:8])
print("Every second character of the string:",user[::2])
first_space = user.find(" ")
last_space = user.rfind(" ")
first_name = user[:first_space]
last_name = user[last_space + 1 :]
print("Fist Name:",first_name)
print("Last Name:",last_name)

#2
user = input("Enter any string: ")
print(user.upper())
print(user.lower())
print(user.title())

#3
sentence = "Varshith reddy"
title_case = sentence.title()
print("Original String:",sentence)
print("Converted to title string:",title_case)

#4
sentence = "VaRsHiTh"
lower_case = sentence.lower()
upper_case = sentence.upper()
print("Lower Case:",lower_case)
print("Upper Case:",upper_case)

#5
user = input("Enter any string:")
print(user.isalpha())
print(user.isdigit())
print(user.isalnum())
print(user.islower())

#6
password = input("Enter the password:")
if password == (password.isalnum()) and len(password) == 8:
    print("Valid Password")
else:
    print("Invalid Password")

#7
string = input("Enter any string: ")
character = input("Enter any character: ")
index = string.find(character)
print("The first occurence of character is at index: ",index)

#8
string = input("Enter any string: ")
word = input("Enter any word: ")
find = string.find(word)
print("Existence:",find)

#9
sentence = "Python"
position = sentence.index("Python")
print(position)

#10
string = input("Enter any string: ")
character = input("Enter any character: ")
find = string.find(character)
print("Find: ",find)
index = string.index(character)
print("Index: ",index)

#11
full_name = "Varshith Reddy"
print("Upper Case:",full_name.upper())
first_space = full_name.find(" ")
last_space = full_name.rfind(" ")
first_name = full_name[:first_space]
last_name = full_name[last_space + 1 :]
print("Index of first space:",full_name.find(" "))
print("First Name: ",first_name)
print("Last Name: ",last_name)

#12
mobile_no = input("Enter mobile number: ")
print(len(mobile_no) == 10)
print(mobile_no.isdigit())

#13
string = input("Enter any string: ")
print("Reverse Order: ",string[::-1])
print("Title Case: ",string.title())
reverse_string = string[::-1]
if string == reverse_string:
    print("Its Palindrome")
else:
    print("Not a palindrome")