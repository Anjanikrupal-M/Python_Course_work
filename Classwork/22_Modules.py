data = {
    '1234':{'balance':45678,'pin':123,'history':[]},
    '6378':{'balance':45676,'pin':253,'history':[]},
    '9827':{'balance':82638,'pin':739,'history':[]},
    '1739':{'balance':40328,'pin':123,'history':[]},
}

acc_num = None
login_status = False


def Welcome():
    print('Welcome to the ATM'.center(40,'-'))

def menu():
    print('1.Check balance')
    print('2.Deposit')
    print('3.Withdraw')
    print('4.View Transation')
    print('0.Exit')


def login(acc,pin):
    if acc in data:
        if data[acc]['pin']==pin:
            global acc_num
            global login_status
            acc_num= acc
            login_status=True
            print("Login Successful")
        else:
            print("Invalid pin")
    else:
        print()     
    

