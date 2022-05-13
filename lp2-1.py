from collections import *

class Graph:
    def __init__(self, v, e):
        self.v = v
        self.e = e
        ajl = defaultdict(list)
        self.ajl = ajl

    def makegraph(self):
        for i in range(self.e):
            n, m = map(int, input("Enter edge nodes separated by space: ").split())
            self.ajl[n].append(m)
            self.ajl[m].append(n)
        print(self.ajl)

    def dfs(self, i, vis):
        vis[i] = True
        print(i, end=" ")
        for j in self.ajl[i]:
            if not vis[j]:
                self.dfs(j, vis)

    def bfs(self, src, vis):
        q = deque([src])
        vis[src] = True

        while q:
            i = q.popleft()
            print(i, end=" ")
            for j in self.ajl[i]:
                if not vis[j]:
                    vis[j] = True
                    q.append(j)


"""ajl = defaultdict(list)
v, e = map(int, input("Enter vertices and edges count separated by space: ").split())
for i in range(e):
    n, m = map(int, input("Enter edge nodes separated by space: ").split())
    ajl[n].append(m)
    ajl[m].append(n)
print(ajl)"""
v, e = map(int, input("Enter vertices and edges count separated by space: ").split())
g = Graph(v, e)
g.makegraph()
while True:
    print("1. DFS\n2. BFS\n3. Re-enter graph\n4. Exit")
    ch = int(input("Enter Choice number: "))
    if ch == 1:
        print("_" * 100)
        vis = defaultdict(bool)
        for i in range(v):
            if not vis[i]:
                g.dfs(i, vis)
        print()
        print("_" * 100)
    elif ch == 2:
        print("_" * 100)
        vis = defaultdict(bool)

        g.bfs(0, vis)
        print()
        print("_" * 100)
    elif ch == 3:
        g.makegraph()
    elif ch == 4:
        break