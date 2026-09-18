#1
num = int(input("Enter any number: "))
if num > 0:
    if num % 2 == 0:
        print("It is positive and even number")
    else:
        print("It is positive and odd number")
else:
    print("It is a negative number")

#2
age = int(input("Enter the age: "))
if age >= 18:
    if age >= 60:
        print("He/She is a senior citizen")
    else:
        print("He is an adult")
else:
    print("Minors")

#3
char = input("Enter any character: ")
if char .isalpha():
    if char .isupper():
        print("Character is an alphabet and in upper case")
    else:
        print("Character is an alphabet and in lower case")
else:
    print("Character is not an alphabet")

#4
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
if num1 > num2:
    if num1 > num3:
        print("Largest Number: ",num1)
    else:
        print("Largest Number: ",num3)
else:
    if num2 > num3:
        print("Largest Number: ",num2)
    else:
        print("Largest Number is: ",num3)

#5
marks = int(input("Enter the student marks: "))
if marks >= 40:
    if marks >= 75:
        print("Pass with distinction")
    else:
        print("Just Pass")
else:
    print("Fail")

#6
num = int(input("Enter any number: "))
if num % 2 == 0:
    if num % 4 == 0:
        print("The number is divisible by 2 and 4")
    else:
        print("The number is only divisible by 2")
else:
    print("The number is not divisible by 2 also")

#7
username = input("Enter the username: ")
password = input("Enter the password: ")
if username == "admin":
    if password == "1234":
        print("Login Successful")
    else:
        print("Invalid Password")
else:
    print("Invalid username")

#8
side1 = int(input("Enter the first side of the triangle: "))
side2 = int(input("Enter the second side of the triangle: "))
side3 = int(input("Enter the third side of the triangle: "))
if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
    if side1 == side2 and side2 == side3:
        print("It is an equilateral triangle")
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("It is an isoceles triangle")
    else:
        print("It is an scalene triangle")
else:
    print("The given sides doesnt form any triangle")

#9
salary = int(input("Enter the salary: "))
experience = int(input("Enter the experience: "))
if salary > 50000:
    if experience > 7:
        print("Senior Manager")
    else:
        print("Manager")
else:
    print("Employee")


#10
char = input("Enter any character: ")
if char .isalpha():
    if char .lower() in "aeiou":
        print("It is an alphabet and it is a vowel")
    else:
        print("It is an alphabet and it is a consonant")
else:
    if char .isdigit():
        print("Digit")
    else:
        print("Special Character")

#11
year = int(input("Enter the year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It is a leap year")
        else:
            print("It is not a leap year")
    else:
        print("It is a leap year")
else:
    print("It is not a leap year")


#12
temp = int(input("Enter the temperature: "))
if temp > 30:
    print("Hot")
else:
    if temp >= 20:
        print("Warm")
    else:
        print("Cold")

#13
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third year: "))
if num1 == num2:
    if num2 == num3:
        print("All three numbers are equal")
else:
    if num1 == num3:
        print("Any two numbers are equal")
    elif num2 == num3:
        print("Any two numbers are equal")
    else:
        print("No numbers are equal")

#14
num = int(input("Enter any number: "))
if num > 0:
    if num % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")

#15
subj1 = int(input("Enter subject 1 marks: "))
subj2 = int(input("Enter subject 2 marks: "))
subj3 = int(input("Enter subject 3 marks: "))
subj4 = int(input("Enter subject 4 marks: "))
subj5 = int(input("Enter subject 5 marks: "))
average = subj1 + subj2 + subj3 + subj4+ subj5 / 5
if average >= 60:
    if subj1 > 40 and subj2 > 40 and subj3 > 40 and subj4 > 40 and subj5 > 40:
        print("passed")
    else:
        print("Not passed because all subjects are not above 40")
else:
    print("the average is below 60")

#16
username = input("Enter the username: ")
password = input("Enter the password: ")
age = int(input("Enter the age: "))
if username == "admin" and password == "python123":
    if age >= 18:
        print("Login Successful")
    elif age < 18:
        print("Age Restriction")
else:
    print("Wrong Credentials")

#17
num = int(input("Enter the number: "))
if num % 3 == 0:
    if num % 5 == 0:
        print("Number is divisble by both 3 and 5")
    else:
        print("Number is only divisible by 3")
else:
    print("Number is not divisible by 3")

#19
grade = input("Enter the grade: ")
if grade == "A":
    print("Excellent")
elif grade == "B":
    print("Good")
elif grade == "C":
    print("Average")
elif grade == "D":
    print("Below Average")
elif grade == "E":
    print("Low")
else:
    print("Fail")

#20
income = int(input("Enetr the icnome: "))
if income > 1000000:
    print("Check tax slab")
elif income >= 50000:
    print("Different slab")
else:
    print("Low Income")
