class shopping:
    discount = 10
    
















class Details:
    def __init__(self,name,mail,pwd):
        self.name = name
        self._mail = mail
        self.__pwd = pwd


    def getpassword(self):
        return self.__pwd
    def setpassword(self,new_password):
        self.__pwd = new_password

sumanth = Details("sumanth","sumanth@gmail","sumanth@123")

print(sumanth.name)
sumanth.name = "sanjay"
print(sumanth.name)

print(sumanth._mail)
sumanth._mail = "sanjay@gmail.com"
print(sumanth._mail)

print(sumanth.getpassword())
sumanth.setpassword("sanjay@123")
print(sumanth.getpassword())





class Bank:
    def __init__(self):
        self.name = "xyz"
        self._balance = 0

    @property
    def noresbalance(self):
        return self._balance

    @noresbalance.setter
    def noresbalance(self,amount):
        self._balance+=amount

b = Bank()
print(b.noresbalance)
b.noresbalance = 3000
print(b.noresbalance)

print(b.name)
b.name = "abc"
print(b.name)







class instagram:
    def __init__(self,username,bio,account_status=False):
        self

















class status:
    def __init__(self,text,caption,image,video,res_30):
        self.text = text
        self.caption = caption
        self.image = image
        self.video = video
        self.videolenght = 30
    
    def display(self):
        if self.video:
            print(f"---{self.video}---\n'{self.caption}")
        else:
            print(f"---{self.image}---\n'{self.caption}")

class statusv1(status):
    def likes(self):
        print("like")
    def music(self):
        print("music Added")
       
