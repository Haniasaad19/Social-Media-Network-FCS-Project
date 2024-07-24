class user:
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
class SocialNetworkGraph:
    def __init__(self):
        self.users={}
        self.graph=nx.SocialNetworkGraph()
    def add_user(self,user_id,name,interests):
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
        plt.figure(figsize=(10,8))
        nx.draw(self.graph,pos,with_labels=True,node_color='skyblue',node_size=2000,edge_color='gray',font_size=10,font_colors='black')
    labels={}
    for node in self.graph.node(data=True):
        user_id=node[0]
        name=node[1].get('name','N/A')
        connections=len(self.graph.edges(user_id))
        interests=",".join(node[1].get('interests',[]))
        labels[user_id]=f"{name}\nfriends:{total_friends}\nconnections:{connections}\ninterests:{interests}
        nx.draw_networkx_labels(self.graph,pos,labels,font_size=8)
        plt.title(title)
        plt.show()
    def menu():
        graph=SocialNetworkGraph()
        while True:
            print('\nMenu:')
            print("1-add user")
            print('2-remove user')
            print('3-add relationship')
            print('4-remove relationship')
            print('5-graph')
            print('6-exit')
            if choice==1:
                user_id=int(input('what is the id: '))
                name=input('what is the name of the user ')
                a=input('what are the interests')
                interests=a.split()
                SocialNetworkGraph.add_user(self,user_id,name,interests)
            elif choice==2:
                name=input('what is the name: ')
                SocialNetworkGraph.remove_user(self,name)
            elif choice==3:
                name1=input('what is the name of first one: ')
                name2=input('what is the name of second one: ')
                SocialNetworkGraph.add_relationship(self,name1,name2)
            elif choice==4:
                name1=input('what is the name of first one: ')
                name2=input('what is the name of second one: ')
                SocialNetworkGraph.remove_relationship(self,name1,name2)
            elif choice==5:
                plt.show()
#example:
user1=user(1011,'hani',['skiing','gym'])
user2=user(1012,'david',['skiing','hiking'])
user3=user(1013,'moe',['eating','party'])
user4=user(1014,'ali',['swimming','gym'])
graph=SocialNetworkGraph()
graph.add_user(user1)
graph.add_user(user2)
graph.add_user(user3)
graph.add_user(user4)
graph.add_edge('user1','user2')
graph.add_edge('user3','user4')    
graph.plot()


