import instaloader

class Insta: 

    def __init__(self, username, password): 
        self.username = username
        self.password = password
        self.L = instaloader.Instaloader()
        self.seguidores = []
        self.seguindo = []

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

            for i in range(len(followers)):
                self.seguidores.append(str(followers[i]).split(' ')[1])

            followes = set(self.profile.get_followees())
            followes = list(followes)

            for i in range(len(followes)):
                self.seguindo.append(str(followes[i]).split(' ')[1])
            
            if(self.seguidores):
                return ({ 'profile': info ,'followers' : self.seguidores , 'followees' : self.seguindo })    

        except:
            return({ 'info' : 'Error connecting to your account '})    

    def get_followes_pic(self):
        try:
            seguindo = []
            profile = instaloader.Profile.from_username(self.L.context, self.username) 
            followes = set(profile.get_followees())

            for i in followes:
                seguindo.append({ 'name' : i.full_name , 'photo' : i.get_profile_pic_url()})
            
            if(seguindo):
                return({ 'data' : seguindo })
        except: 
            return({ 'info' : 'Error'})        

    def get_unfollowees(self): 
        try: 
            result  = set(self.seguindo).difference(self.seguidores)
            result  = list(result)
            return({ 'unfollowees' : result })
        except: 
            return({ 'info' : 'Error'})