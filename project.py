class user:
    def __init__(self,user_id,name):
        self.user_id=user_id
        self.name=name
        self.friends=[]
    def add_friend(self,friend):
        self.friends.append(friend)
    def remove_friend(self,friend):
        self.friends.remove(friend)
class SocialNetworkGraph:
    def __init__(self):
        self.users={}
    def add_user(self,user):
        if user not in self.users:
            self.users[user]=[]
        else:
            print('this user is already using the network ')
            
    