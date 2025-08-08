#here we use pass if we have nothing to overcome the error

class NormalUser:
    def playvideo(self,name):
        print(f"\n{name} is playing video with :\n1.Normal Quality\n2.Ads run\n3.No background play\n4.Limited videos download\n5.Music with ads")
    def likes(self):
        pass
    def comments(self):
        pass
    def comments(self):
        pass
    def share(self):
        pass
    def title(self):
        pass
    def description(self):
        pass
    def  subscribe(self):
        pass

class premiumUser:
    def playvideo(self,name):
        print(f"\n{name} is playing video with :\n1.High Quality\n2.Ads free\n3.Background play\n4.Unlimited videos download\n5.Exclusive Music")

dinesh = NormalUser()
sanjay = premiumUser()

dinesh.playvideo("dinesh")
sanjay.playvideo("sanjay")









class NormalUser:
    def playvideo(self,name):
        print(f"\n{name} is playing video with :\n1.Normal Quality\n2.Ads run\n3.No background play\n4.Limited videos download\n5.Music with ads")
    

class premiumUser:
    def playvideo(self,name):
        print(f"\n{name} is playing video with :\n1.High Quality\n2.Ads free\n3.Background play\n4.Unlimited videos download\n5.Exclusive Music")

def play_video(user,username):
    user.playvideo(username)

dinesh = NormalUser()
sanjay = premiumUser()
mohit = NormalUser()
gopal = premiumUser()

play_video(dinesh,"dinesh")
play_video(sanjay,"sanjay")
play_video(mohit,"mohit")
play_video(gopal,"gopal")




#operator overloading
class number:
    def __init__(self,n):
        self.n=n
    def __add__(self,others):
        return self.n+ others.n
    def __sub__(self,others):
        return self.n-others.n
    def __mul__(self,others):
        return self.n*others.n
    def __str__(self):
        return f"{self.n}"
    def __lt__(self,others):
        return self.n<others.n
    def __gt__(self,others):
        return self.n>others.n
    def __eq__(self,others):
        return self.n==others.n

number1 = number(10)
number2 = number(20)

print(number1+number2)
print(number1-number2)
print(number1*number2)
print(number1)
print(number1<number2)
print(number1>number2)
print(number1==number2)