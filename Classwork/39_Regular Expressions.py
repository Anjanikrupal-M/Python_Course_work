import re

res = re.match('Hello','Hello world')
print(res.group() if res else "NO Match")    #Hello



r = re.match(r'\d','1234v Hello world')
print(r.group() if r else "NO Match")    #1

resu = re.search(r'[6-9]','Hello world 786')
print(resu) 



resul = re.findall(r'[a-z]','hello world wduwdvyuv')
print(resul)


fe = re.finditer(r'[0-9]','Hello world 84 6 865 05')
for i in fe:
    print(i.group(),i.start())

fm = re.fullmatch(r'[0-9]{10}','1234567890')
print(fm.group() if fm else "NO Match") 


ns = re.split(r'[,:/0;]','dinesh,sanjay;jashwanth/mohit')
print(ns)     #['dinesh', 'sanjay', 'jashwanth', 'mohit']

text = "java programming language"
res = re.sub(r'[aeiou]','*',text)
print(res)     #j*v* pr*gr*mm*ng l*ng**g*