squ = lambda n : n**2
print(squ(5))
#25



isevenorodd = lambda n : "even" if n % 2 ==0  else "odd"
print(isevenorodd(64))
#even



l = [1,0,0,3,5,35,64,0,6]
squ = list(filter(lambda i:i!=0 ,l))
print(squ)
#[1, 3, 5, 35, 64, 6] here it removes 0




data = {'dinesh':47,'mukesh':39,'arjun':43}
d = dict(sorted(data.items(),key =lambda i:i[1],reverse=True))
print(d)

