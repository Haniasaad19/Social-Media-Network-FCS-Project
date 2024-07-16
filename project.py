class user:
    def __init__(self,user_id,name):
        self.user_id=user_id
        self.name=name
        self.friends=set()
    def add_friend(self,friend):
        self.friends.add(friend)
    def remove_friend(self,friend):
        self.friends.discard(friend)