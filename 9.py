student={
    "Name":"alice",
    "age":"18",
    "course":"Btech"
}
print(student)


student={
    "Name":"Pankhuri",
    "age":"18",
    "course":"Btech"
}
# print(student)
# Name=student["Name"]
# age=student["age"]
student["age"]=21 
for key,value in student.items():
    print(f"{key}:{value}")