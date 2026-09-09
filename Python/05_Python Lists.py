#1
students = ["Varshith","Kruthika","likhi"]
print(students)

#2
numbers = [10,20,30,40,50]
print("Data type:",type(numbers))
print("Length of Numbers:",len(numbers))

#3
list = []
numbers = [1,2,3]
list.append(numbers)
print(list)

#4
list = [1,2,3]
numbers = [4,5,6]
list.extend(numbers)
print(list)

#5
list = [10,20,30,40,50]
list.insert(2,100)
print(list)

#6
list = [10,20,30,40,50]
list.remove(50)
print(list)

#7
list = [5,10,15,20]
list.pop(-1)
print(list)

#8
data = [1,2,3,4,5]
data.clear()
print(data)

#9
list = [10,15,25,30,40]
print(list.index(25))

#10
list = [7,2,7,5,7,8]
print(list.count(7))

#11
list = [45,12,78,23,56]
list.sort()
print(list)

#12
list = [45,12,78,23,56]
list.sort(reverse = True)
print(list)

#13
fruits = ["apple","banana","mango","orange"]
fruits.reverse()
print(fruits)

#14
original = [1,2,3,4]
copy_list = original.copy()
print("Original List:",original)
print("Copy List:",copy_list)

#15
user = input("Enter any sentence: ")
split = user.split()
print(user)
print(split)

#16
numbers = [9,2,4,5,3]
append_list = [1,8,6]
numbers.extend(append_list)
numbers.sort(reverse=True)
print(numbers)

#17
list = ["Java","is","Love"]
list.insert(0,"Python")
list.pop(-1)
print(list.index("Python"))
print(list)
print("Length of the list: ",len(list))

#18
city1 = input("Enter the city 1 name: ")
city2 = input("Enter the city 2 name: ")
city3 = input("Enter the city 3 name: ")
city4 = input("Enter the city 4 name: ")
city5 = input("Enter the city 5 name: ")
list = [city1,city2,city3,city4,city5]
list.reverse()
print(list)

#19
data = [10,20,30,20,40,20]
data.remove(20)
print(data)
data.remove(20)
print(data)
data.remove(20)
print(data)

#19.1
data = [10,20,30,20,40,20]
while 20 in data:
  data.remove(20)
data

#20
student_marks = [98,97,89,78,72]
student_marks.sort()
highest_mark = max(student_marks)
lowest_mark = min(student_marks)
print("Student Marks: ",student_marks)
print("Highest Marks: ",highest_mark)
print("Lowest Marks: ",lowest_mark)