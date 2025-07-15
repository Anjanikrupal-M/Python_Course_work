n =5
for row in range(n):
    for col in range(n):
        print("*",end=' ')
    print()


n = 5
for row in range(5):
    for col in range(row+1):
        print("*",end=" ")
    print()



n = 5
for row in range(n,0,-1):
    for col in range(row):
        print("*",end=" ")
    print()  


n = int(input())
for row in range(n):
    for col in range(n):
        if row==0 or row==n-1 or row+col==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()            