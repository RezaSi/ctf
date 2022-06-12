import pprint
import sys
from pwn import *

 
class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                    for row in range(vertices)]
 
    # A utility function to print the constructed MST stored in parent[]
    def mst(self, parent):
        res = 0
        for i in range(1, self.V):
            res += self.graph[i][parent[i]]
        return res
 
    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minKey(self, key, mstSet):
 
        # Initialize min value
        min = sys.maxsize
 
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
 
        return min_index
 
    # Function to construct and print MST for a graph
    # represented using adjacency matrix representation
    def primMST(self):
 
        # Key values used to pick minimum weight edge in cut
        key = [sys.maxsize] * self.V
        parent = [None] * self.V # Array to store constructed MST
        # Make key 0 so that this vertex is picked as first vertex
        key[0] = 0
        mstSet = [False] * self.V
 
        parent[0] = -1 # First node is always the root of
 
        for cout in range(self.V):
 
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minKey(key, mstSet)
 
            # Put the minimum distance vertex in
            # the shortest path tree
            mstSet[u] = True
 
            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.V):
 
                # graph[u][v] is non zero only for adjacent vertices of m
                # mstSet[v] is false for vertices not yet included in MST
                # Update the key only if graph[u][v] is smaller than key[v]
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                        key[v] = self.graph[u][v]
                        parent[v] = u
 
        return self.mst(parent)



# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(g.graph)

r = remote('hacking-pt2.hsctf.com', 1337)
res = r.recv()
print(res)
for oo in range(10):
    res = r.recvline()
    print(res)
    n = r.recvline().decode()
    print(n)
    n = int(n)
    g = Graph(n)
    for i in range(n):
        res = r.recvline().decode()
        res = res.strip()
        print(res)
        arr = res.split(' ')
        for j in range(len(arr)):
            m, c = map(int, arr[j].split(','))
            g.graph[i][m - 1] = c
            if g.graph[m - 1][i] != 0:
                g.graph[m - 1][i] = min(g.graph[m - 1][i], c)
                g.graph[i][m - 1] = min(g.graph[m - 1][i], c)
            else:
                g.graph[m - 1][i] = c

    result = g.primMST()
    print(result)
    r.sendline(str(result))
    res = r.recvline().decode()
    print(res)
    res = r.recvline().decode()
    print(res)