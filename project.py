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
from tkinter import simpledialog, messagebox
class SocialNetworkGraph:
    def __init__(self):
        self.users={}
        self.graph=nx.Graph()
    def add_user(self,user_id,name,interests):
        user=User(user_id,name,interests)
        self.users[user_id]=user
        self.graph.add_node(user_id,name=name,interests=interests)
    def add_relationship(self,user1,user2):
        if user1 in self.users and user2 in self.users:
            self.graph.add_edge(user1,user2)
            self.users[user1].add_friend(user2)
            self.users[user2].add_friend(user1)
    def remove_relationship(self,user1,user2):
        if user1 in self.users and user2 in self.users:
            self.graph.remove_edge(user1,user2)
            self.users[user1].remove_friend(user2)
            self.users[user2].remove_friend(user1)      
    def remove_user(self,user):
        if user in self.users:
            for friend in self.users[user].friends:
                self.users[friend].remove_friend(user)
                self.graph.remove_edge(user,friend)
            del self.users[user]
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
    def menu(self):
        self.root=tk.Tk()
        self.root.title("social network graph ")
        frame=tk.Frame(self.root)
        frame.pack(pady=20)
        btn_add_user=tk.Button(frame,text="add user ",command=self.add_user_gui)
        btn_add_user.grid(row=0, column=0, padx=10, pady=10)

        btn_remove_user = tk.Button(frame, text="Remove User", command=self.remove_user_gui)
        btn_remove_user.grid(row=0, column=1, padx=10, pady=10)

        btn_add_relationship = tk.Button(frame, text="Add Relationship", command=self.add_relationship_gui)
        btn_add_relationship.grid(row=1, column=0, padx=10, pady=10)

        btn_remove_relationship = tk.Button(frame, text="Remove Relationship", command=self.remove_relationship_gui)
        btn_remove_relationship.grid(row=1, column=1, padx=10, pady=10)

        btn_plot_graph = tk.Button(frame, text="Plot Graph", command=self.plot)
        btn_plot_graph.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.root.mainloop()

    def add_user_gui(self):
        user_id = simpledialog.askinteger("Input", "Enter user ID:")
        if user_id is not None:
            name = simpledialog.askstring("Input", "Enter user name:")
            interests = simpledialog.askstring("Input", "Enter interests (separated by spaces):")
            if name and interests:
                interests_list = interests.split()
                self.add_user(user_id, name, interests_list)
                messagebox.showinfo("Info", "User added successfully!")
            else:
                messagebox.showerror("Error", "Invalid input, try again.")
    def remove_user_gui(self):
        user_id = simpledialog.askinteger("Input", "Enter user ID to remove:")
        if user_id is not None:
            self.remove_user(user_id)
            messagebox.showinfo("Info", "User removed successfully!")
    def add_relationship_gui(self):
        user1_id = simpledialog.askinteger("Input", "Enter the first user ID:")
        user2_id = simpledialog.askinteger("Input", "Enter the second user ID:")
        if user1_id and user2_id:
            self.add_relationship(user1_id, user2_id)
            messagebox.showinfo("Info", "Relationship added successfully!")
    def remove_relationship_gui(self):
        user1_id = simpledialog.askinteger("Input", "Enter the first user ID:")
        user2_id = simpledialog.askinteger("Input", "Enter the second user ID:")
        if user1_id and user2_id:
            self.remove_relationship(user1_id, user2_id)
            messagebox.showinfo("Info", "Relationship removed successfully!")



# Example Usage:
graph = SocialNetworkGraph()
graph.menu()
    




