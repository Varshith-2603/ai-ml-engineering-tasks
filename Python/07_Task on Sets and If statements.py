#1
my_set = {1,2,3,2,4,1}
print(my_set)

#2
usual_set = set()
usual_set.add(1)
usual_set.add(2)
usual_set.add(3)
print(usual_set)

#3
s = {10,20,30}
update_set = {40,50,60}
s.update(update_set)
print(s)

#4
s = {10,20,30,40}
s.remove(20)
print(s)

#4.1
s = {10,20,30,40}
s.discard(20)
print(s)

#5
A = {1,2,3,4}
B = {3,4,5,6}
C = A.union(B)
D = A.intersection(B)
E = A.difference(B)
print(C)
print(D)
print(E)

#6
s = {10,20,30,40}
print(25 in s)

#7
data = [1,2,2,3,4,4,5]
my_set = set(data)
print(my_set)
print(len(my_set))

#8
user = input("Enter five numbers: ")
y = set(user)
print(y)

#9
A = {1,2,3}
B = {3,4,5}
C = A.difference(B)
print(C)

#10
unique_set = set()
update_list = {1,2,3}
unique_set.update(update_list)
print(unique_set)

#11
age = int(input("Enter the age: "))
if age >= 18:
    print("You are eligible to vote")

#12
number = 12
if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")

#13
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
if number1 > number2:
    print("Number 1 is greater than number 2")
elif number2 > number1:
    print("Number 2 is greater than number 1")

#14
char = input("Enter a character: ")
if char in "aeiou":
    print("It is a vowel")
else:
    print("It is not a vowel")

#15
marks =int(input("Enter a marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
else:
    print("Fail")

#16
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
if number1 > number2 and number1 > number3:
    print("Number 1 is greater than 2,3")
elif number2 > number1 and number2 > number3:
    print("Number 2 is greater than 1,3")
elif number3 > number1 and number3 > number2:
    print("Number 3 is greater than 1,2")
else:
    print("Wrong number")

#17
number = int(input("Enter the number: "))
if number % 2 == 0 and number > 50:
    print("The number is even and greater than 50")

#18
username = input("Enter the username: ")
password = input("Enter the password: ")
if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Login Failed")

#19
year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Leap year")
else:
    print("Not a leap year")

#20
side1 = int(input("Enter first side: "))
side2 = int(input("Enter second side: "))
side3 = int(input("Enter third side: "))
if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
    print("Valid triangle")
else:
    print("Not a valid triangle")

#21
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
if number1 > number2 and number1 > number3:
    print("Number 1 is the largest number",number1)
elif number2 > number1 and number2 > number3:
    print("Number 2 is the largest number",number2)
elif number3 > number2 and number3 > number1:
    print("Number 3 is the largest number",number3)

if number1 == number2 and number2 == number3:
    print("All three numbers are equal")
else:
    print("All three numbers are not equal")

#22

