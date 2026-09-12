#1
number = int(input("Enter any number: "))
if number > 0:
    print("The given number is positive")
elif number < 0:
    print("The given number is negative")
elif number == 0:
    print("The given number is zero")

#2
age = int(input("Enter the age: "))
if age >= 18:
    print("You can enter theatre")
else:
    print("You cannot enter the theatre")

#3
number = int(input("Enter any number: "))
if number % 2 == 0:
    print("The given number is divisble by 2")

#4
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
if number1 > number2:
    print("Number 1 is greater than number ")
elif number2 > number1:
    print("Number 2 is greater than number 1 ")

#5
char = input("Enter any character: ")
if char .isupper():
    print("The given character is upper case")
elif char .islower():
    print("The given character is lower case")

#6
year = int(input("Enter the year: "))
if (year % 4 == 0 and year % 100 !=0) or year % 400 == 0:
    print("Its a leap year")
else:
    print("Its not a leap year")

#7
time = int(input("Enter the time: "))
if time < 12:
    print("Morning")
elif time >= 12 and time <= 5:
    print("Afternoon")
else:
    print("Evening")

#8
marks = int(input("Enter the student marks: "))
if marks > 75:
    print("Distinction")
elif marks >= 35 and marks <= 74:
    print("Pass")
elif marks < 35:
    print("Fail")

#9
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
if num1 > num2 and num1 > num3:
    print("Number 1 is greater than number 2 and number 3")
elif num2 > num3 and num2 > num1:
    print("Number 2 is greater than number 1 and number 3")
elif num3 > num1 and num3 > num2:
    print("Number 3 is greater than number 2 and number 1")

#10
units = int(input("Enter the units: "))
if units < 100:
    print("₹2/unit")
elif units >= 100 and units <= 300:
    print("₹4/unit")
elif units > 300:
    print("₹6/unit")

#11
side1 = int(input("Enter the first side of a triangle: "))
side2 = int(input("Enter the second side of a triangle: "))
side3 = int(input("Enter the third side of a triangle"))
if side1 == side2 and side2 == side3:
    print("Equilateral Triangle")
elif side1 == side2 or side2 == side3 or side3 == side1:
    print("Isoceles Triangle")
else:
    print("Scalene Triangle")

#12
salary = int(input("Enter the salary: "))
if salary > 50000:
    print("20% bonus")
elif salary >= 30000 and salary <= 50000:
    print("10% bonus")
else:
    print("5% bonus")

#13
username = input("Enter the username: ")
password = input("Enter the password: ")
if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Login Failed")

#14
num = int(input("Enter any number: "))
if num % 3 == 0 and num % 5 == 0:
    print("Number is multiple of both 3 and 5")
elif num % 3 == 0:
    print("Number is multiple of 3")
elif num % 5 == 0:
    print("Number is multiple of 5")
else:
    print("None")

#15
age = int(input("Enter the age: "))
if age >= 0 and age <= 12:
    print("Child")
elif age >= 13 and age <= 19:
    print("Teenager")
elif age >= 20 and age <= 59:
    print("Adult")
elif age >= 60:
    print("Senior Citizen")

#16
age = input("Enter the age: ")
if age <  5:
    print("Entry Free")
elif age >= 5 and age <= 18:
    print("₹100")
elif age == "adults":
    print("₹200")
elif age == "Senior Citizens":
    print("₹150")

#17
print("1.Check Balance")
print("2.Withdraw money")
print("3.deposit money")
choice = int(input("Enter your choice: "))
if choice == 1:
    print("Check balane")
elif choice == 2:
    print("Withdraw money")
elif choice == 3:
    print("Deposit money")
else:
    print("Invalid option message")

#18
income = int(input("Enter the amount: "))
if income < 250000:
    print("No Tax")
elif income >= 250000 and income <= 500000:
    print("5%")
elif income >= 500000 and income <= 1000000:
    print("20%")
elif income >= 1000000:
    print("30%")

#19
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
d = b**2-4*a*c
if d > 0:
    print("Two distinct real roots")
if d == 0:
    print("Two equal roots")
else:
    print("No equal roots")

#20
number1 = float(input("Enter the first number: "))
operator = input("Choose an Operator (+,-,*,/,//,%,**): ")
number2 = float(input("Enter the second number: "))
if operator == "+":
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "*":
    print(number1 * number2)
elif operator == "/":
    print(number1 / number2)
elif operator == "//":
    print(number1 // number2)
elif operator == "%":
    print(number1 % number2)
elif operator == "**":
    print(number1 ** number2)


#23
purchase = int(input("Enter the amount: "))
if purchase > 5000:
    print("30% discount")
elif purchase >= 2000 and purchase <= 5000:
    print("20% discount")
elif purchase < 2000:
    print("10% discount")

#24
performance = int(input("Enter the performance rating: "))
if performance > 90:
    print("Excellent")
elif performance >= 70 and performance <= 89:
    print("Good")
elif performance >= 50 and performance <= 69:
    print("Average")
elif performance < 50:
    print("poor")

