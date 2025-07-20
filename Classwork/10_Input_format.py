n =input("Enter your name: ")
print(n)
a=int(input("Enter the number of items: "))
print(a)
b=float(input("Enter the product price: "))
print(b)
names=input("Enter the names (space_Seperated): ").split() #Space Seperated 
print(names)
names_comma=input("Enter your names (comma-seperated): ").split(",")
print(names_comma)
marks=list(map(int,input("Enter the marks: ").split()))
print(marks)
weights=list(map(float,input("Enter weights: ").split()))
print(weights)
denominations=tuple(map(int,input("Enter your denominations: ").split()))
print(denominations)
selected_ids=set(map(int,input("Enter selected image IDs:").split()))
print(selected_ids)
profile=eval(input("Enter user profile as a dictionary:"))
print(profile)
username,password=input("Enter your username and password").split()
print(username)
print(password)


# Enter your name: Sanjay
# Sanjay
# Enter the number of items: 45
# 45
# Enter the product price: 55.9
# 55.9
# Enter the names (space_Seperated): Venkata naga raghava
# ['Venkata', 'naga', 'raghava']
# Enter your names (comma-seperated): venkata,naga,raghava
# ['venkata', 'naga', 'raghava']      
# Enter the marks: 34 56 78 65
# [34, 56, 78, 65]
# Enter weights: 34.5 56.8 78.9 23.6 
# [34.5, 56.8, 78.9, 23.6]
# Enter your denominations: 100 10 20
# (100, 10, 20)
# Enter selected image IDs:101 102 10 
# 3
# {10, 3, 101, 102}
# Enter user profile as a dictionary:{"name":"Sanjay","age":"22"}
# {'name': 'Sanjay', 'age': '22'}     
# Enter your username and password 
# Sanjay 2--3
# Sanjay
# 2--3