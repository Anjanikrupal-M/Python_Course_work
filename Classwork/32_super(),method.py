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
