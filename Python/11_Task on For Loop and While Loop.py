#1
for i in range(1,11):
    print(i)

#2
for i in range(2,21,2):
    print(i)

#3
num = int(input("Enter any number: "))
for i in range(1,11):
    print(num,"x",i,"=",num*i)

#4
total = 0
for i in range(1,11):
    total = total+i
print("Sum:",total)

#5
for i in range(1,6):
    print("*" * i)

#6
num_list = list(map(int,input("Enter the numbers: ").split()))
for num in num_list:
    print(num**2)

#7
for i in range(50,29,-1):
    print(i)

#8
count = 0
for i in range(1,51):
    if i % 3 == 0:
        count = count + 1
print("Count:",count)

#9
string = input("Enter any string: ")
for str in string:
    print(str)

#10
for i in range(1,6):
    for j in range(1,11):
        print(i,"x",j,"=",i*j)

#11
i = 1
while i < 16:
    print(i)
    i += 1

#12
num = int(input("Enter any number: "))
i = 1
while i<= 10:
    print(num,"x",i,"=",num*i)
    i += 1

#13
total = 0
num = int(input("Enter any number: "))
while num != 0:
    total = total + num
    num = int(input("Enter any number: "))
print("Sum:",total)

#14
i = 0
while 1 < 21:
    if i % 2 != 0:
        print(i)
    i += 1

#15
num = float(input("Enter any number: "))
steps = 0
while num >= 1:
    num = num/2
    steps += 1
print("Number of steps:",steps)

#17
user_input = input("Enter something: ")
while user_input != "stop":
    print("You Entered: ",user_input)
    user_input = input("Enter something")

print("Program Stopped")

#18
a = 0
b = 1
count = 0
while count < 10:
    print(a)

    c = a+b
    a = b
    b = c

    count += 1

#19
num = int(input("Enetr ny number: "))
if num < 2:
    print("Not a Prime number")
else:
    i = 2

    while i < num:
        if num % i == 0:
            print("Not a prime number")
            break
        i += 1
    else:
        print("Prime number")

#20
while True:
    print("\n1.Add")
    print("2.Subtract")
    print("3.Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Sum:",a+b)

    elif choice == 2:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Difference:",a-b)

    elif choice == 3:
        print("Program exited")
        break

    else:
        print("Invalid choice")