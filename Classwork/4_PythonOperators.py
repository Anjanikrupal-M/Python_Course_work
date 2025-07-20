#1. Arthimetic Operators
a = 10
b = 20
print("Addition:",a+b) #Addition: 30
print("Subtraction:",a-b) #Subtraction: -10
print("Multiplication:",a*b) #Multiplication: 200
print("Division:",a/b) #Division: 0.5
print("FloorDivision:",a//b) #FloorDivision: 0
print("Modulus:",a%b) #Modulus: 10
print("Exponential:",a**b) #Exponential: 100000000000000000000



#2. Comparision Operators
c = 20
d = 40
print(c==d) #Equalto(==): False

print(c!=d) #Noteuqalto(!=): True

print(c>d) #Greaterthan(>): False

print(c<d) #Lessthan(<): True

print(c>=d) #GreaterthanorEqualto(>=): False

print(c<=d) #LessthanorEqualto(<=): True


#3.Assignment Operators
x = 10
print("Assign:",x) #Assign: 10

x+=30
print(x) #Add & Assign(+=): 40

x-=20
print(x) #Subtract & Assign(-=): 20

x*=2
print(x) #Multiply & Assign(*=): 40

x/=2
print(x) #Divide & Assign(/=): 20.0

x//=10
print(x) #Floor Divide & Assign(//=): 2.0

x%=2
print(x) #Modulus & Assign(%=): 0.0

x**=10
print(x) #Exponentiate & Assign(**=): 0.0


#4. Logical Operators

print("Logical operators")
x=30
y=10
print("and:",(x%10==0)and (y%10==0)) #and: True
print("OR:",(x%10==0)or (y%10==0)) #OR: True
print("not:",not (x%10==0)) #not: False


#5.Membership operators

Names = ['suman','ashok','manoj','arjun']
print('in result:','rahul' in Names)  # in result: False
print('not in result:','suhas' not in Names) # not in result: True


#6. Identity operator

l = [1,2,3,4]
b = [1,2,3,4]
print("l is b:",l is b) #l is b: False

a = b
print("a is b:",a is b) #a is b: True

print("id(l):",id(l)) #id(l): 2330410329280

print("id(b):",id(b)) #id(b): 2330412008640

print("id(a):",id(a)) #id(a): 2330412008640

print("a is not b:",a is not b) #a is not b: False

print("l is not b:",l is not b) #l is not b: True


#7.Bitwise Operators

print("Bitwise Operators:")
print("and operator 3 & 5:",3&5)
print("or operator  4 | 5:",4|5)
print("xor operator 5 ^ 6:",5^6)
print("~1 not operator : ",~1)
print("left shift operator by   1 bit 4<<1: ",2<<1)#Multiply by 2
print("left shift operator by   2 bit 4<<2: ",4<<2)
print("right shift operator by  1 bit 4>>1: ",4>>1)# Divide by 2
print("right shift operator by  2 bit 4>>2: ",4>>2)
