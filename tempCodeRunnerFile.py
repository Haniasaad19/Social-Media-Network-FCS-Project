import networkx as nx
import matplotlib.pyplot as plt

class User:
    def _init_(self, user_id, name, interests):
        self.user_id = user_id
        self.name = name
        self.friends = []
        self.interests = interests
        self.posts = []

    def add_interest(self, interest):
        self.interests.append(interest)

    def add_post(self, post):
        self.posts.append(post)

    def add_friend(self, friend):
        self.friends.append(friend)

    def remove_friend(self, friend):
        self.friends.remove(friend)

class SocialNetworkGraph:
    def _init_(self):
        self.users = {}
        self.graph = nx.Graph()

    def add_user(self, user_id, name, interests):
        self.users[user_id] = []
        self.graph.add_node(user_id, name=name, interests=interests)

    def add_relationship(self, user1, user2):
        if user1 in self.users and user2 in self.users:
            self.users[user1].append(user2)
            self.users[user2].append(user1)
            self.graph.add_edge(user1, user2)

    def remove_relationship(self, user1, user2):
        if user1 in self.users and user2 in self.users:
            self.users[user1].remove(user2)
            self.users[user2].remove(user1)
            self.graph.remove_edge(user1, user2)

    def remove_user(self, user):
        if user in self.users:
            for friend in self.users[user]:
                self.users[friend].remove(user)
            del self.users[user]
            self.graph.remove_node(user)

    def get_users(self):
        return list(self.users.keys())

    def get_friends(self, user):
        return self.users.get(user, [])

    def dfs(self, start_user):
        visited = set()
        stack = [start_user]
        while stack:
            user = stack.pop()
            if user not in visited:
                visited.add(user)
                print(user)
            stack.extend(set(self.get_friends(user)) - visited)

    def bfs(self, start_user):
        visited = set()
        queue = [start_user]
        while queue:
            user = queue.pop(0)
            if user not in visited:
                visited.add(user)
                print(user)
            queue.extend(set(self.get_friends(user)) - visited)

    def sort_users(self, key_func):
        return sorted(self.users.keys(), key=key_func)

    def average_friends(self):
        total_friends = sum(len(self.get_friends(user)) for user in self.get_users())
        return total_friends / len(self.get_users())

    def dijkstra(self, start_user):
        distances = {user: float('inf') for user in self.get_users()}
        distances[start_user] = 0
        priority_queue = [(0, start_user)]
        while priority_queue:
            current_distance, current_user = heapq.heappop(priority_queue)
            if current_distance > distances[current_user]:
                continue
            for neighbor in self.get_friends(current_user):
                distance = current_distance + 1
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        return distances

    def plot(self, title="Network Graph"):
        pos = nx.spring_layout(self.graph)
        plt.figure(figsize=(10, 8))
        nx.draw(self.graph, pos, with_labels=True, node_color='skyblue', node_size=2000, edge_color='gray', font_size=10, font_color='black')
        labels = {}
        for node, data in self.graph.nodes(data=True):
            user_id = node
            name = data.get('name', 'N/A')
            connections = len(self.graph.edges(user_id))
            interests = ",".join(data.get('interests', []))
            labels[user_id] = f"{name}\nfriends: {connections}\nconnections: {connections}\ninterests: {interests}"
        nx.draw_networkx_labels(self.graph, pos, labels, font_size=8)
        plt.title(title)
        plt.show()

# Example usage:
graph = SocialNetworkGraph()
graph.add_user(1011, 'hani', ['skiing'])
graph.add_user(1012, 'david', ['gym'])
graph.add_relationship(1011, 1012)
graph.plot()