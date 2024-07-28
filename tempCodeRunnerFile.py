class User:
    def __init__(self,user_id,name,interests):
        self.user_id=user_id
        self.name=name
        self.friends=[]
        self.interests=interests
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
import tkinter as tk
from tkinter import messagebox
class SocialNetworkGraph:
    def __init__(self,root):
        self.users = {}
        self.graph = nx.Graph()
        self.root = root
        self.root.title('Social Network Graph')

        self.add_button = tk.Button(root, text="Add User", command=self.add_user)
        self.add_button.pack()
        self.remove_button = tk.Button(root, text="Remove User", command=self.remove_user)
        self.remove_button.pack()
        self.add_relationship_button = tk.Button(root, text="Add Relationship", command=self.add_relationship)
        self.add_relationship_button.pack()
        self.visualize_button = tk.Button(root, text="Visualize Graph", command=self.visualize_graph)
        self.visualize_button.pack()

    def add_user(self,user_id,name,interests):
        user_id = simpledialog.askinteger("Input", "Enter user ID:")
        name = simpledialog.askstring("Input", "Enter user name:")
        interests = simpledialog.askstring("Input", "Enter interests (comma-separated):").split(',')
        if user_id and name:
            user = User(user_id, name, interests)
            self.users[user_id] = user
            self.graph.add_node(user_id, name=name, interests=interests)
    def add_relationship(self,user1,user2):
        user1_id = simpledialog.askinteger("Input", "Enter the first user ID:")
        user2_id = simpledialog.askinteger("Input", "Enter the second user ID:")
        if user1_id in self.users and user2_id in self.users:
         self.graph.add_edge(user1_id, user2_id)
         self.users[user1_id].add_friend(user2_id)
         self.users[user2_id].add_friend(user1_id)
    def remove_relationship(self,user1,user2):
        if user1 in self.users and user2 in self.users:
            if user1_id in self.users and user2_id in self.users:
             self.graph.remove_edge(user1_id, user2_id)
             self.users[user1_id].remove_friend(user2_id)
             self.users[user2_id].remove_friend(user1_id)      
    def remove_user(self,user):
        user_id = simpledialog.askinteger("Input", "Enter user ID to remove:")
        if user_id in self.users:
            for friend in self.users[user_id].friends:
                self.users[friend].remove_friend(user_id)
                self.graph.remove_edge(user_id, friend)
            self.graph.remove_node(user_id)
            del self.users[user_id]
    def get_users(self):
        return list(self.users.keys())
    def get_friends(self,user_id):
        return list(self.graph.neighbor(user_id))
    def dfs(graph,start_user_id):
        visited=set()
        stack=[start_user_id]
        while stack:
            user=stack.pop()
            if user not in visited:
                visited.add(user)
                print(user)
            stack.extend(set(self.get_friends(user))-visited)
    def bfs(graph,start_user_id):
        visited=set()
        queue=[start_user_id]
        while queue:
            user=queue.pop(0)
            if user not in visited:
                visited.add(user)
                print(user)
            queue.extend(set(self.get_friends(user))-visited) 
    def sort_users(users,key_func):
        return sorted(self.users.values(),key=key_func)
    def average_friends(graph):
        total_friends=sum(len(self.get_friends(user)) for user in self.get_users()) 
        return total_friends /len(self.get_users()) if self.get_users() else 0
    import heapq
    def dijkstra(self,start_user_id):
        distances={user: float('inf') for user in self.get_users()}
        distances[start_user_id]=0
        priority_queue=[(0,start_user_id)]
        while priority_queue:
            current_distance,current_user=heapq.heappop(priority_queue)
            if current_distance>distances[current_user]:
                continue
            for neighbor in self.get_friends(current_user):
               distance=current_distance +1
               if distance<distances[neighbor]:
                 distances[neighbor]=distance
            heapq.heappush(priority_queue,(distance,neighbor))
        return distances
    def add_edge(self,user_id1,user_id2):
        self.graph.add_edge(user_id1,user_id2)
    def plot(self,title="Network Graph"):
        pos=nx.spring_layout(self.graph)
        plt.figure(figsize=(10,8))
        nx.draw(self.graph,pos,with_labels=True,node_color='skyblue',node_size=4000,edge_color='gray',font_size=10,font_color='black')
        labels={}
        for node_id,node_data in self.graph.nodes(data=True):
          name=node_data.get('name','N/A')
          interests=','.join(node_data.get('interests',[]))
          labels[node_id]=  f"{name}\nInterests: {interests}"
        nx.draw_networkx_labels(self.graph,pos,labels,font_size=8)
        plt.title(title)
        plt.show()