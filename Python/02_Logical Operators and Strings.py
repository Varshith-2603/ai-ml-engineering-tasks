#1. LOGICAL OPERATORS
#1
age = int(input("Enter the age: "))
marks = float(input("Enter the marks: "))
if age >= 18 and age <= 25 and marks >= 60:
    print("Student is eligible for admission")
else:
    print("Student is not eligible for admission")

#2
Username = input("Enter the username: ")
Password = input("Enter the password: ")
if Username == "admin" and Password == "12345":
    print("Login Successful")
else:
    print("Login Failed")


#3
user = int(input("Enter the number: "))
print(user >= 50 and user <= 100)
print(not user%5==0)

#4
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
if number1 > number2 and number1 > number3:
    print("Number 1 is the largest Number")
elif number2 > number1 and number2 > number3:
    print("Number 2 is the largest number")
elif number3 > number1 and number3 > number2:
    print("Number 3 is the largest number")


#2. STRING AND STRING SLICING OPERATIONS
#5.
name = input("Enter Your full name: ")
print(name.upper())
print(name.lower())
print(len(name))
print(name[:3])
print(name[-3:])

#6
user = input("Enter any sentence: ")
print(user[:11])
print(user[-10:])
print(user[5:15])
print(user[::2])

#7
user = input("Enter any word")
if user == user[::-1]:
    print("Entered word is a palindrome")
else:
    print("Entered word is not a palindrome")

#8
email = input("Enter the email: ")
username, domain = email.split("@")
print("Username:",username)
print("Domain:",domain)

#9
user = input("Enter the password: ")
if len(user) >= 8 and ('@' in user or '#' in user):
    print("Strong Password")
else:
    print("Weak Password")

#10
English = input("Enter the English marks: ")
Math = input("Enter the Math marks: ")
Science = input("Enter the science marks: ")
if English >= 40 and Math >= 40 and Science >= 40:
    print("Passed")
else:
    print("Fail")

#11
num = int(input("Enter any number:"))
if (num > 0 and num%2 == 0) or (num < 0 and num%2 != 0):
    print("The number matches the condition")
else:
    print("The number doesnt matches the condition")

#12
city = input("Enter your city name: ")
print(city[::-1])
vowels = "aeiouAEIOU"
print(vowels in city)
without_first_char = city.remove(0)
without_last_char  = city.remove(-1)
print("City name without first character:",without_first_char)
print("City name without last character:",without_last_char)

#13
mobile_no = int(input("Enter your mobile number: "))
print("Network Code:",mobile_no[:3])
print("Last Four Digits:",mobile_no[-4:])
print("Middle Three Digits:",mobile_no[3:6])

#14
user = input("Enter any string: ")
if len(user) > 5 and (user[1] == "A" or user[1] == "a"):
    print("Valid String")
else:
    print("Invalid String")

