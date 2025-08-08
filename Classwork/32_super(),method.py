class Instagram:
    def __init__(self,username):
        self.username = username
        self.post=[]
        print(f"{self.username.center(40,'-')}")

class Instagramv1(Instagram):
    def __init__(self,username,bio):
        super().__init__(username)
        self.bio=bio
        print(f'bio uploaded')

dinesh = Instagram('dinesh123')
sanjay = Instagramv1("sanjay","coder")    




class Instagram:
    def __init__(self,username):
        self.username = username
        self.post=[]
        print(f"{self.username.center(40,'-')}")

    def uploadpost(self,image):
        self.post.append(image)
        print(f"{image} is posted")    

class Instagramv1(Instagram):
    def __init__(self,username,bio):
        super().__init__(username)
        self.bio=bio
        print(f'bio uploaded')
        
    def uploadpost(self,post,music):
        super().uploadpost(post)
        self.music = music
        print(f"{self.music} is added")         

dinesh = Instagram('dinesh123')
dinesh.uploadpost("photo.png")
sanjay = Instagramv1("sanjay","coder")
sanjay.uploadpost("Hero.png","model.mp3")







#super() can be used only when we have only to call from one parent
class Instagram:
    def __init__(self,username):
        self.username = username
        print(f"{self.username} user is created! parent-1")

class Instav1:
    def __init__(self,username):
        self.username = username
        print(f"{self.username} user is created! parent-2")

class Instav2(Instagram,Instav1):
    def __init__(self, username):
        Instagram.__init__(self,username)
        Instav1.__init__(self,username)
        print("creating users from version 3")

i = Instav2("username-sanjay") 