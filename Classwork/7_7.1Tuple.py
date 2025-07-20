a=()
print(type(a))   #<class 'tuple'>

b=(2,)
print(b)         #(2,)

c=(1,"banana",9.5) 
print(c)         #(1, 'banana', 9.5)

d=1,2,3
print(d)         #(1, 2, 3)

a=(10,20,40,50)
print(a[2])      #40
print(a[-2])     #40
print(a[1:4])    #(20, 40, 50)

b=(1,2)
c=(3,4)
d=b+c
print(d)         #(1, 2, 3, 4)
print(b*3)       #(1, 2, 1, 2, 1, 2)
print(2 in d)    #True
print(5 not in d) #True

f=(1,2,3)
a,b,c=f
print(a,b,c)      #1 2 3
a=(1,2,1,2,3)
print(f"Count:{a.count(1)}")  #Count:2
print(f"index:{a.index(2)}")  #index:1
print(f"Length {len(a)}")     #Length 5
print(f"Maximum:{max(a)}")    #Maximum:3
print(f"Minimum:{min(a)}")    #Minimum:1
print(f"Sum:{sum(a)}")        #Sum:9
print(tuple[1,2,3])           #tuple[1, 2, 3]
print(tuple("anjani"))        #('a', 'n', 'j', 'a', 'n', 'i')
nested=[1,[1,2]]
print(nested[1][0])           #1