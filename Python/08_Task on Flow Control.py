#1
num = int(input("Enter a number: "))
if num > 0:
    print("The given number is positive")
elif num < 0:
    print("The given number is negative")

#2
age = int(input("Enter the age: "))
if age >= 18:
    print("You can vote")

#3
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print("Number 1 is the largest number",num1)
elif num2 > num1:
    print("MNumber 2 is the largest number",num2)

#4
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even")
elif number % 2 != 0:
    print("The number is odd")

#5
char = input("Enter any character: ")
if "A" in char:
    print("Its A")
else:
    print("Its not A")

#6
marks = int(input("Enter the marks: "))
if marks >= 40:
    print("PASS")
else:
    print("Fail")

#7
number = int(input("Enter a number: "))
if number % 5 == 0:
    print("The number is divisible by 5")
else:
    print("The given number is not divisible by 5")

#8
number = int(input("Enter a number: "))
if number > 0:
    print("The given number is positive")
elif number < 0:
    print("The given number is negative")
elif number == 0:
    print("The given number is zero")


#9
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
if number1 > number2 and number1 > number3:
    print("Number 1 is greater than number 2 and 3",number1)
elif number2 > number1 and number2 > number3:
    print("Number 2 is greater than nu8mber 1 and 3")
else:
    print("Number 3 is greater than number 1 and 2")

#10
year = int(input("Enter the year: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("It is a leap year")
else:
    print("It is not a leap year")

#11
char = input("Enter any character: ")
if char in "aeiou":
    print("It is a vowel")
else:
    print("It is a consonant")

#12
salary = int(input("Enter the salary: "))
if salary > 50000:
    print("High")
elif salary > 30000:
    print("Medium")
else:
    print("Low")

#13
temp = int(input("Enter the temperature in celsius: "))
if temp > 30:
    print("High")
elif temp >= 20 and temp <= 30:
    print("Warm")
elif temp < 20:
    print("Cold")

#14
username = input("Enter the username: ")
password = input("Enter the password: ")
if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Login Failed")

#15
side1 = int(input("Enter the side 1 of a triangle: "))
side2 = int(input("Enter the second side of a triangle: "))
side3 = int(input("Enter the third side of a triangle: "))
if side1 + side2 > side3 and side3 + side1 > side2 and side3 + side2 > side1:
    print("It is a triangle")
else:
    print("It is not a triangle")

if side1 == side2 and side2 == side3:
    print("It is an Equilateral triangle")
elif side1 == side2 or side2 == side3 or side3 == side1:
    print("It is an Isosceles Triangle")
else:
    print("Scalene Triangle")

#16
subject1 = int(input("Enter subject 1 marks: "))
subject2 = int(input("Enter subject 2 marks: "))
subject3 = int(input("Enter subject 3 marks: "))
subject4 = int(input("Enter subject 4 marks: "))
subject5 = int(input("Enter subject 5 marks: "))
total = subject1 + subject2 + subject3 + subject4 + subject5
percentage = total/5
if percentage > 90:
    print("A+")
elif percentage >= 80 and percentage <= 89:
    print("A")
elif percentage >= 70 and percentage <= 79:
    print("B")
elif percentage >= 60 and percentage <= 69:
    print("C")
elif percentage < 60:
    print("Fail")

#17
number = int(input("Enter any number: "))
if number % 2 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)

#18
age = int(input("Enter the age: "))
gender = input("Enter the gender: ")
if age >= 18 and gender == "Male":
    print("Eligible for Army")
elif age >= 18 and gender == "Female":
    print("Eligible for other services")
else:
    print("Not Eligible")

#19
char = input("Enter any character: ")
if char .isupper():
    print("It is Upper case")
elif char .islower():
    print("It is Lower Case")
elif char .isdigit():
    print("It is a digit")
else:
    print("It is a Special Character")

#20
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
if num1 <= num2 and num2 <num3:
    print(num1,num2,num3)
elif num1 <= num3 and num3 <= num2:
    print(num1,num3,num2)
elif num2 <= num1 and num1 <= num3:
    print(num2,num1,num3)
elif num2 <= num3 and num3 <= num1:
    print(num2,num3,num1)
elif num3 <= num1 and num1 <= num2:
    print(num3,num1,num2)
else:
    print(num3,num2,num1)