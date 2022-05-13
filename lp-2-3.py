import heapq
from math import *
from collections import defaultdict
import sys

class Node:
    def __init__(self, row, col, tot_rows, tot_col):
        self.row = row
        self.col = col
        self.neighb = []
        self.stat = 0
        self.tot_rows = tot_rows
        self.tot_col = tot_col

    def getpos(self):
        return self.row, self.col

    # 0 = open
    # 1 = blocked
    # 2 = start
    # 3 = end
    def isobstacle(self):
        if self.stat == 1:
            return True
        return False

    def isopen(self):
        if self.stat == 0:
            return True
        return False

    def isstart(self):
        if self.stat == 2:
            return True
        return False
o 
    def isend(self):
        if self.stat == 3:
            return True
        return False

    def block(self):
        self.stat = 1

    def open(self):
        self.stat = 0

    def start(self):
        self.stat = 2

    def end(self):
        self.stat = 3

    def update_neigh(self, grid):
        self.neighb = []

        # DOWN
        if self.row < self.tot_rows - 1 and not grid[self.row + 1][self.col].isobstacle():
            self.neighb.append(grid[self.row + 1][self.col])

        # UP
        if self.row > 0 and not grid[self.row - 1][self.col].isobstacle():
            self.neighb.append(grid[self.row - 1][self.col])

        # LEFT
        if self.col > 0 and not grid[self.row][self.col - 1].isobstacle():
            self.neighb.append(grid[self.row][self.col - 1])

        # RIGHT
        if self.col < self.tot_rows - 1 and not grid[self.row][self.col + 1].isobstacle():
            self.neighb.append(grid[self.row][self.col + 1])


class Grid:
    def __init__(self, grid, rows, cols):
        mp = [[] for i in range(rows)]
        self.mp = mp
        for i in range(rows):
            for j in range(cols):
                nd = Node(i, j, rows, cols)
                if grid[i][j] == 1:
                    nd.block()
                elif grid[i][j] == 2:
                    nd.start()
                    self.start = nd
                elif grid[i][j] == 3:
                    nd.end()
                    self.end = nd
                else:
                    nd.open()
                self.mp[i].append(nd)

    def h(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def update_all(self):
        for i in self.mp:
            for j in i:
                j.update_neigh(self.mp)


    def astar(self):
        cnt = 0
        opset = []
        heapq.heapify(opset)
        heapq.heappush(opset, (0, cnt, self.start))
        prev = defaultdict(int) # storing the path

        gscore = defaultdict(float)
        for row in self.mp:
            for nd in row:
                gscore[nd] = float("inf")

        gscore[self.start] = 0

        fscore = defaultdict(float)
        for row in self.mp:
            for nd in row:
                fscore[nd] = float("inf")

        fscore[self.start] = self.h(self.start.getpos(), self.end.getpos())

        opset_hash = defaultdict(bool)


        while opset:
            curr = opset[0][2]
            heapq.heappop(opset)
            opset_hash[curr] = True

            if curr == self.end:
                ans = []
                i = self.end
                while i in prev:
                    ans.append(i.getpos())
                    i = prev[i]
                ans.append(self.start.getpos())
                return ans

            for i in curr.neighb:
                tempg = gscore[curr] + 1

                if tempg < gscore[i]:
                    prev[i] = curr
                    gscore[i] = tempg
                    fscore[i] = tempg + self.h(i.getpos(), self.end.getpos())
                    if not opset_hash[i]:
                        cnt += 1
                        heapq.heappush(opset, (fscore[i], cnt, i))
                        opset_hash[i] = True

            if curr != self.start:
                curr.block()

        return False

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

n, m = map(int, input().split())
grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))
gr = Grid(grid, n, m)
gr.update_all()
ans = gr.astar()
if not ans:
    print("No path found!")
else:
    ans = ans[::-1]
    print("The shortest path is:")
    for i in ans:
        if i != ans[-1]:
            print(str(i) + " ->", end=" ")
        else:
            print(i)
    print()
    print("Representation in a grid: ")
    ans1 = grid[:]
    for i in ans:
        ans1[i[0]][i[1]] = "P"
    ans1[ans[0][0]][ans[0][1]] = "S"
    ans1[ans[-1][0]][ans[-1][1]] = "E"
    for i in range(n):
        print(*ans1[i])
