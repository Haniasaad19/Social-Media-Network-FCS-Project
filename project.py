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
    def remove_relationship(self,user1,user2):
        if user1 in self.users and user2 in self.users:
            self.users[user1].remove(user2)
            self.users[user2].remove(user1)      
    def remove_user(self,user):
        if user in self.users:
            for friend in self.users[user]:
                self.users[friend].remove(user)
            del self.users[user]
    def get_users(self):
        return list(self.users.keys())
    def get_friends(self,user):
        return self.users.get(user,[])
    def dfs(graph,start_user):
        visited=set()
        stack=[start_user]
        while stack:
            user=stack.pop()
            if user not in visited:
                visited.add(user)
                print(user)
            stack.extend(set(self.get_friends(user))-visited)
    def bfs(graph,start_user):
        visited=set()
        queue=[start_user]
        while queue:
            user=queue.pop(0)
            if user not in visited:
                visited.add(user)
                print(user)
            queue.extend(set(graph.get_friends(user))-visited) 
    def sort_users(users,key_func):
        return sorted(users,key=key_func)   
