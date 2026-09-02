 #1
user = input("Enter any string: ")
print(user.replace(" ","_"))

#2
user = input("Enter any string: ",)
strip = user.strip()
print(strip)

#3
user = input("Enter any sentence: ")
print(user.startswith("Hello"))

#4
user = input("Enter any sentence: ")
print(user.endswith(".com"))

#5
user = input("Enter any comma seperated string: ")
print(user.split(","))

#6
fruits = ["apple","banana","carrot","dragonfruit","mango"]
print(fruits.join(" "))

#8
full_name = "Rahul Kumar Sharma"
parts = full_name.split()
first_name = parts[0]
last_name = parts[-1]
print("First Name: ",first_name)
print("Last Name: ",last_name)

#9
user = input("Enter any sentence: ")
words = user.split()
print(len(words))

#10
user = input("Enter your email address: ")
print(user.endswith("@gmail.com"))

#11
string = "Hello World Python"
replace = string.replace("World","Everyone")
print(replace.split())

#12
list = (list(input("Enter the list of 5 city names: ")))
split_list = list.split()
join = "/n".join(split_list)
print(split_list)
print(join)

#13
string = "   hello world   "
strip = string.strip(" ")
title_case = strip.title()
print(strip)
print(title_case)
print(title_case.startswith("Hello"))

#14
string = "He is a good boy"
split = string.split()
join = " ".join(string)
replace = string.replace("good","bad")
print(split)
print(join)
print(replace)

#15
list = ["10","20","30","40"]
join_list = "-".join(list)
print(join_list)

#17
string = "I love Badminton"
replace_with = string.replace(" ","-")
split_by = replace_with.split("-")
for split in split_by:
  if len(split) > 4:
    print(split)

#18
list = ["Chandler","Rachel","Monica","Ross"]
join = ",".join(list)
replace = join.replace("Chandler","New Student")
print(join)
print(replace)

#20
string = "   I-Love-Fruits-Badminton     " 
replace = string.replace("Badminton","Vegetables")
strip_space = replace.strip()
split_it = strip_space.split("-")
join_tog = " ".join(split_it)
print(replace)
print(strip_space)
print(split_it)
print(join_tog)

