a={}
print(type(a))
a=[("name","anjani"),("age",21),("course","python")]
print(dict(a))
student={
    "name":"anjani",
    "age":21,
    "course":"python"
}
print(student["name"])
## Dictionary methods for Accessing Data
print(student.get("age"))
print(student.get("city","Not Available"))
student["city"]="Hyderabad"
student["name"]="arjun"
print(student)
print(student.items())
print(student.keys())
print(student.values())
age=student.pop("age")
print(f"age :{age}")
print(student)
student.popitem()
print(student)
##Dictionary methods for Adding and updating data
student={
    "name":"anjani",
    "age":21,
    "course":"python",
    "city":"Hyderabad"
}
print(student)
student.update({"city":"Vijayawada"})
print(student)
student.setdefault("skills","Python")
print(student)
student.setdefault("skills","java")
print(student)
print(f"length {len(student)}")
print(f"Maximum {max(student)}")
print(f"Minimum {min(student)}")
print(f"Sorted {sorted(student)}")
# <class 'dict'>
# {'name': 'anjani', 'age': 21, 'course': 'python'}
# anjani
# 21
# Not Available
# {'name': 'arjun', 'age': 21, 'course': 'python', 'city': 'Hyderabad'}
# dict_items([('name', 'arjun'), ('age', 21), ('course', 'python'), ('city', 'Hyderabad')])
# dict_keys(['name', 'age', 'course', 'city'])
# dict_values(['arjun', 21, 'python', 'Hyderabad'])
# age :21
#{'name': 'arjun', 'course': 'python', 'city': 'Hyderabad'}
#{'name': 'arjun', 'course': 'python'}
#{'name': 'anjani', 'age': 21, 'course': 'python', 'city': 'Hyderabad'}
#{'name': 'anjani', 'age': 21, 'course': 'python', 'city': 'Vijayawada'}
#{'name': 'anjani', 'age': 21, 'course': 'python', 'city': 'Vijayawada', 'skills': 'Python'}
#{'name': 'anjani', 'age': 21, 'course': 'python', 'city': 'Vijayawada', 'skills': 'Python'}
#length 5
#Maximum skills
#Minimum age
#Sorted ['age', 'city', 'course', 'name', 'skills']