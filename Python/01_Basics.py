#1. Comments and print
# name = "varshith",college name = "ICFAI",course = "mechatronics"
#name = "varshith"
#college name = "ICFAI"
#course = "Mechatronics"
'''
name = "Varshith"
college name = "Icfai"
course = "mechatronics
'''

#2. Indentation Practise
if True:
    print("Hello World")
print("Welcome to Python")

#3. Variables Declaration
name = "Varshith"
age = 21
height = 178.23
is_student = True
print(type(name))
print(type(age))
print(type(is_student))

#4. Variable Naming Rules
#1st_name = "Invalid"
#my name = "Invalid"
#total@amount = "Invalid"
#class = "Invalid"
#MyVar = "Valid"
#_score = "Valid"
#99marks = "Invalid"

#5. Arithmetic Operators
number1 = int(input("Enter the first number:"))
number2 = int(input("Enter the second number:"))
print("Sum:",number1+number2)
print("Difference:",number1-number2)
print("Product:",number1*number2)
print("Division:",number1/number2)
print("Floor Division:",number1//number2)
print("Modulus:",number1%number2)
print("Power:",number1**number2)

#6. Comparison Operators
a = 10
b = 20
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


#7. Assignment Operators
a = 10
a += 10
print("Sum:", a)
a -= 10
print("Difference:",a)
a *= 10
print("Product:",a)
a /= 10
print("Division:",a)
a //= 10
print("Floor Division:",a)
a %= 10
print("Modulus:",a)
a **= 10
print("Power:",a)

#8. Local VS Global Variable
college = "Icfai tech school"
def hello():
    global college
    print(college)
    return
print(college)

#9. Simple Calculator
number1 = float(input("Enter the first number: "))
operator = input("Choose an operator (+,-,*,/,//,%,**):")
number2 = float(input("Enter the second number: "))
result = None
if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '*':
    result = number1 * number2
elif operator == '/':
    result = number1 / number2
elif operator == '//':
    result = number1 // number2
elif operator == '%':
    result = number1 % number2
elif operator == '**':
    result = number1 ** number2
else:
    print("Invalid Operator")
if result is not None:
    print(result)

#10. Temperature converter
celsius = 25
fahrenheit = (celsius*9/5)+32
print("Fahrenheit:",fahrenheit)

fahrenheit = 77
celsius = (fahrenheit-32)*5/9
print("Celsius:",celsius)

#11. Area and perimeter calculator
r = float(input("Enter the radius of the circle:"))
area = 3.14*r**2
circumference = 2*3.14*r
print("Area of the circle:",area)
print("Circumference of the circle:",circumference)

#12. Student Grade Calculator
subject1 = int(input("Enter subject1 marks:"))
subject2 = int(input("Enter subject2 marks:"))
subject3 = int(input("Enter subject3 marks:"))
subject4 = int(input("Enter subject4 marks:"))
subject5 = int(input("Enter subject5 marks:"))
percentage = (subject1 + subject2 + subject3 + subject4 + subject5)/5
if percentage >= 90:
    print("A+ grade")
elif percentage >= 80:
    print("A grade")
elif percentage >= 70:
    print("B grade")
elif percentage >= 60:
    print("C grade")
else:
    print("Fail")

#13. Swap two variables
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
temp = x
x = y
y = temp
print(x)
print(y)

#without third variable(pythonic way)
x = 100
y = 300
x,y = y,x
print(x)
print(y)

#14. Logical Operators practise
age = int(input("Enter the age:"))
salary = float(input("Enter the salary:"))
if age >= 18 and age <= 60 and salary > 25000:
    print("Person is eligible for loan")
else:
    print("Person is not eligible for loan")

#15
x = 10
print(type(x))
x = '10'
print(type(x))
x = 10.0
print(type(x))
x = True
print(type(x))
