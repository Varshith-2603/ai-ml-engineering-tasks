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

