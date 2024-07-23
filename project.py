class user:
    def __init__(self,user_id,name):
        self.user_id=user_id
        self.name=name
        self.friends=[]
        self.interests=[]
        self.posts=[]
    def add_interest(self,interest):
        self.interests.append(interest)
    def add_post(self,post):
        self.posts.append(post)
    def add_friend(self,friend):
        self.friends.append(friend)
    def remove_friend(self,friend):
        self.friends.remove(friend)
import networkx as nx
import matplotlib.pyplot as plt
class SocialNetworkGraph:
    def __init__(self):
        self.users={}
        self.graph=nx.SocialNetworkGraph()
    def add_user(self,user_id,name,total_friends):
        self.graph.add_node(user_id,name=name,friends_count=friends_count)
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
    def average_friends(graph):
        total_friends=sum(len(graph.get_friends(user)) for user in graph.get_users()) 
        return total_friends /len(graph.get_users())
    import heapq
    def dijkstra(graph,start_user):
        distances={user: float('inf') for user in graph.get_users()}
        distances[start_user]=0
        priority_queue=[(0,start_user)]
        while priority_queue:
            current_distance,current_user=heapq.heappop(priority_queue)
            if current_distance>distances[current_user]:
                continue
            for neighbor in graph.get_friends(current_user):
               distance=current_distance +1
               if distance<distances[neighbor]:
                 distances[neighbor]=distance
            heapq.heappush(priority_queue,(distance,neighbor))
        return distances
    def add_edge(self,user_id1,user_id2):
        self.graph.add_edge(user_id1,user_id2)
    def plot(self,title="Network Graph"):
        pos=nx.spring_layout(self.graph)
    
    
