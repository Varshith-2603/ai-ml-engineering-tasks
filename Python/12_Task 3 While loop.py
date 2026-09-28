#1
i = 1
while i < 21:
    print(i)

    i+=1

#2
num = 1
while num <= 50:
    if num % 2 == 0:
        print(num)
    num += 1

#3
n = int(input("Enter any number:"))
sum = 0
num = 1
while num <= n:
    sum += num
    num += 1
print("Sum:",sum)

#4
num = int(input("Enter the number: "))
reverse = 0
while num > 0:
    digit = num%10
    reverse = reverse*10+digit
    num = num//10
print("Reversed number =",reverse)

#5
num = int(input("Enter the number: "))
count = 0
while num > 0:
    num = num//10
    count+=1
print("Total Digits:",count)

#6
num = int(input("Enter the number: "))
original = num
reverse = 0
while num > 0:
    digit = num%10
    reverse = reverse*10+digit
    num = num//10
if original == reverse:
    print("Its a palindrome")
else:
    print("Its not a palindrome")

#7
num = int(input("Enter the number: "))
original = num
sum = 0
while num > 0:
    digit = num % 10
    sum = sum + digit **3
    num = num//10
if sum == original:
    print("Armstrong")
else:
    print("Not armstrong")

#8
correct_password = "python123"
password = input("Enter the password: ")
while password != correct_password:
    print("incorrect password")
    password = input("Enter the password")
print("Correct password,access granted")

#9
num = 34
user = int(input("Guess the number:"))
while user != num:
    print("The guessed number is wrong")
    user = int(input("Guess the number:"))
print("The guessed number is correct")

#10
num = int(input("Enter the number required for multiplication: "))
i = 1
while i <= 10:
    print(num,"X",i,"=",num*i)
    i += 1

#11
n = int(input("Enter the number: "))
a = 0
b = 1
count = 0 
while count < n:
    print(a)

    c = a+b
    a = b
    b = c

    count += 1

#12
num = int(input("Enter the number: "))
factorial = 1
i = 1
while num <= i:
    factorial = factorial * i
    i += 1
print("Factorial =",factorial)

#13
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
        print("Subtract:",a-b)

    elif choice == 3:
        print("Program Exited")
        break

    else:
        print("Invalid Choice")


#14
while True:
    print("\n1.Check Balance")
    print("2.Deposit money")
    print("3.Withdraw money")
    print("4.Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Check Balance")
    elif choice == 2:
        print("Deposit Money")
    elif choice == 3:
        print("Withdraw money")
    elif choice == 4:
        print("Exit")
        break
    else:
        print("Invalid choice")

#15

    
