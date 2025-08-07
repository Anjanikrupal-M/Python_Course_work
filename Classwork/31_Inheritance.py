#single inheritance(1 to 1)

class status:       #parent 
    def uploadimage(self,imageurl):
        self.image = imageurl
        print(f"{self.image} is uploaded to your status")

class statusv1(status):     #child
    def addcaption(self,text=None):
        self.caption = text
        print(f'"{self.caption}" is added to your status')

sravani = status()
sravani.uploadimage('self.png')

hema = statusv1()
hema.uploadimage('Goodmorning.png')
hema.addcaption("Morning friends!!!")




#2.Hierarchical Inheritance(1 to many)

class status:       #parent 
    def uploadimage(self,imageurl):
        self.image = imageurl
        print(f"{self.image} is uploaded to your status")

class statusv1(status):     #child1
    def addcaption(self,text=None):
        self.caption = text
        print(f'"{self.caption}" is added to your status')

class statusv2(status):   #child2
    def like(self):
        print(f'you can like status')     

sravani = status()
sravani.uploadimage('self.png')

hema = statusv1()
hema.uploadimage('Goodmorning.png')
hema.addcaption("Morning friends!!!")

vaishnavi = statusv2()
vaishnavi.uploadimage("coffee.png")
vaishnavi.like()



#Multiple Inheritance(many to one )

class status:       #parent 
    def uploadimage(self,imageurl):
        self.image = imageurl
        print(f"{self.image} is uploaded to your status")

class statusv1(status):     #child1
    def addcaption(self,text=None):
        self.caption = text
        print(f'"{self.caption}" is added to your status')

class statusv2(status):   #child2
    def like(self):
        print(f'you can like status')

class statusv3(statusv1,statusv2):
    def addMusic(self,music):
        self.music = music
        print(f'{self.music}... is added to your status')    

sravani = status()
sravani.uploadimage('self.png')

hema = statusv1()
hema.uploadimage('Goodmorning.png')
hema.addcaption("Morning friends!!!")

vaishnavi = statusv2()
vaishnavi.uploadimage("coffee.png")
vaishnavi.like()

deepika = statusv3
deepika.uploadimage("Mountains and Trees.png")
deepika.addcaption("no wifi")
deepika.like()
deepika.add("Mature.mp3")


#Multilevel Inheritance

class status:       #parent 
    def uploadimage(self,imageurl):
        self.image = imageurl
        print(f"{self.image} is uploaded to your status")

class statusv1(status):     #child1
    def addcaption(self,text=None):
        self.caption = text
        print(f'"{self.caption}" is added to your status')

class statusv2(status):   #child2
    def like(self):
        print(f'you can like status')

class statusv3(statusv1,statusv2):
    def addMusic(self,music):
        self.music = music
        print(f'{self.music}... is added to your status')   

class statusv4(statusv3):
    def videolenght(self,video):
        self.video = video
        print(f'{self.video} is uploaded to your status')         

sravani = status()
sravani.uploadimage('self.png')

hema = statusv1()
hema.uploadimage('Goodmorning.png')
hema.addcaption("Morning friends!!!")

vaishnavi = statusv2()
vaishnavi.uploadimage("coffee.png")
vaishnavi.like()

deepika = statusv3
deepika.uploadimage("Mountains and Trees.png")
deepika.addcaption("no wifi")
deepika.like()
deepika.add("Mature.mp3")

nikitha= statusv4
nikitha.uploadimage("Sunrise.png")
nikitha.addcaption("Nothing")
nikitha.like()
nikitha.add("Music")
nikitha.videolenght("Somevideo.mp4")

