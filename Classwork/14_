data = {
    1:{'name':'Dinesh','exam_status':True,'python':100,'sql':95,'html':98},
    2:{'name':'Shivani','exam_status':True,'python':80,'sql':45,'html':68},
    3:{'name':'Arun','exam_status':False,'python':None,'sql':None,'html':None},
    4:{'name':'Sushmitha','exam_status':True,'python':30,'sql':15,'html':25},
    5:{'name':'Dharshitha','exam_status':True,'python':80,'sql':75,'html':65}
}

for i in data.keys():
    print(f'{i}. {data[i]["name"]}')

stuid = int(input("Enter the student id: "))

if stuid in data:
    if data[stuid]["exam_status"]:
        total = (data[stuid]["python"] + data[stuid]["sql"] + data[stuid]["html"]) / 3
        if total > 90:
            print(f'Congrats!!!\n{data[stuid]["name"]} got "A" grade')
        elif total > 75:
            print(f'Good!!!\n{data[stuid]["name"]} got "B" grade')
        elif total > 50:
            print(f'Need improvement!!!\n{data[stuid]["name"]} got "C" grade')
        elif total > 35:
            print(f'Just Passed!!!\n{data[stuid]["name"]} got "D" grade')
        else:
            print(f'{data[stuid]["name"]} - Fail, Better luck next time!!!!')
    else:
        print(f'{data[stuid]["name"]} is not attempted the exams')
else:
    print("The id is not present. Try Again")