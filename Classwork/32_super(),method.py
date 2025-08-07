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
