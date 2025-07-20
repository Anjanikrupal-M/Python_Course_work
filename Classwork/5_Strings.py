name = "sanjay"
print(name)

print(name.ljust(30,' '))

print(name.ljust(30,' ')+":") #leftside

print(name.rjust(30," ")+":")  #rightside

print('56'.zfill(6))  #000056

print(''.zfill(10))  #0000000000

w = 'arjun is a cop'
print(w)            #arjun is a cop

print(w.find('a'))  #0

print(w.rfind('a')) #9

print(w.index('a'))
#0

print(w.rindex('a'))
#9

print(w.find('z'))
#-1

#name.index('z')    #error when it can't find

print(w.count('a'))  #counts
#2

print(w.startswith("arjun")) #True

d = 'abc'.isalpha()  #check it is alphabet or not
#True
d = 'abc123'.isalpha()
#False
di = '123'.isdigit()  #checks digits or not
True
n = '1.23'.isdigit()
False
n = 'arjun123'.isalnum()  #checks numerics and alphabets and no other special chars
'arjun@123'.isalnum()
#False
'arjun'.islower()
#True
'Arjun'.islower()
#False
'ARJUN'.isupper()
#True

s = ' '.isspace()  #checks whether having space
#True