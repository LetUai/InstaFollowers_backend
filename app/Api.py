import instaloader

class Insta: 

    def __init__(self, username, password): 
        self.username = username
        self.password = password
        self.L = instaloader.Instaloader()


    def login(self): 
        try:    
            self.L.login(self.username,self.password)
            if self.L.login:
                return({ 'info' : 'success'})
        except:
            return({ 'info': 'Error connecting to your account'  })

    def get_followers(self):
        try:  
            self.profile = instaloader.Profile.from_username(self.L.context, self.username) 

            info = { 'profile_image' : self.profile.get_profile_pic_url() , 'biography' : self.profile.biography }

            followers = set(self.profile.get_followers()) 
            followers = list(followers)
            seguidores = []  

            for i in range(len(followers)):
                seguidores.append(str(followers[i]).split(' ')[1])

            followes = set(self.profile.get_followees())
            followes = list(followes)
            seguindo = []

            for i in range(len(followes)):
                seguindo.append(str(followes[i]).split(' ')[1])
            
            if(seguidores):
                return ({ 'profile': info ,'followers' : seguidores , 'followees' : seguindo })    

        except:
            return({ 'info' : 'Error connecting to your account '})    

    def get_info(self):
        return(self.profile)        