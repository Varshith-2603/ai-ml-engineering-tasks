#1
student = {
    "name":"Varshith",
    "Age":21,
    "City":"Hyderabad"
}
print(student)

#2
d = {"a":1,"b":2,"c":3}
x = d.keys()
print(x)

#3
d = {"a":1,"b":2}
x = d.values()
print(x)

#4
d = {"name":"Sumit","age":25}
x = d.get("name")
print(x)

#5
numbers = (1,2,3,4,5)
print("Type of Data: ",type(numbers))
print("Length of Datatype: ",len(numbers))

#6
tup = (10,20,30,40,50)
print(tup.count(20))

#7
tuple = (10,20,30,40,50)
print(tuple.index(30))

#8
dict = {}
assigned = {"name":"Varshith","Age":21,"City":"Hyderabad"}
my_dict = assigned.append(dict)

#9
d = {"a":1,"b":2}
d.update({"c":3,"d":4})
print(d)

#10
student = {"name":"Rahul","age":22,"city":"Delhi"}
student.pop("age")
print(student)

#11
d = {"x":10,"y":20,"z":30}
removed_item = d.popitem()
print(removed_item)

#12
dictionary_original = {"a":1,"b":2}
my_dict = dictionary_original.copy()
print(my_dict)

#14
tuple = ("varshith",21,12.3)
tuple.replace(1,22)
print(tuple)

#15
d = {"name":"Sumit"}
d.setdefault("age",25)
print(d)

#16
dict = {"Name":"Varshith","Age":21,"Clg":"Mahindra","Weight":65}
dict.update({"Height":173,"CGPA":7.76,"Branch":"Mechatronics"})
print(dict)

#17
tuple = (1,2,3,4,5,6,7,8,1,2,3,3)
print(tuple[2])
print(tuple.count(3))

#18
student1 = input("Enter student 1 name and marks: ")
student2 = input("Enter student 2 name and marks: ")
student3 = input("Enter student 3 name and marks: ")
dict = {student1,student2,student3}
print(dict)

#19
data = {"a":10,"b":20,"c":10}
for key,value in data.items():
  if value == 10:
    print(key)

#20
dict = {"Name":"Varshith","Age":21,"Clg":"Icfai","Branch":"Mechatronics","Sports":"Badminton"}
copy_dict = dict.copy()
dict.clear()
print("Original Dict: ",dict)
print("Copy Dict: ",copy_dict)

#21
student = {"Name":"Varshith","Age":21,"Clg":"Icfai","Branch":"Mechatronics"}
student.update({"Sports":"Badminton","Core":"AIML ROBOTICs"})
student.popitem()
print(student.items())

#22
this_tuple = (12,25,48,60,72,25,99,88)
print(this_tuple.index(25))
print(this_tuple.count(25))
my_list = list(this_tuple)
my_list.sort(reverse=True)
this_tuple = tuple(my_list)
print(this_tuple)

#23
students = {}
students[input("Enter Student 1 name: ")] = int(input("Enter student 1 marks: "))
students[input("Enter Student 2 name: ")] = int(input("Enter student 2 marks: "))
students[input("Enter student 3 name: ")] = int(input("Enter student 3 marks: "))
students[input("Enter student 4 name: ")] = int(input("Enter student 4 marks: "))
highest_student = max(students,key=students.get) 
print("Student with highest marks: ",highest_student)
print("Marks: ",students[highest_student])

#24
info = {"name":"Aman","Age":21,"city":"Mumbai"}
copied_info = info.copy()
info.clear()
copied_info.update({"country":"India"})
print(info)
print(copied_info)

#25
data = (10,20,30,20,40,20,50)
result = {}
for num in data:
  result[num] = data.count(num)
print(result)
