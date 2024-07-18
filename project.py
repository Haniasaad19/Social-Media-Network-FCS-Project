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
    def add_relationship(self,user1,user2):
        if user1 in self.users and user2 in self.users:
            self.users[user1].append(user2)
            self.users[user2].append(user1)
            
    