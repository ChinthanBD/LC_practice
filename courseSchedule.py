# https://www.geeksforgeeks.org/problems/course-schedule/1
#User function Template for python3
from collections import deque, defaultdict

class Solution:
    def findOrder(self, V, m, prerequisites):
        adj = defaultdict(list)
        for dest, source in prerequisites:
            adj[source].append(dest)

        indegree = [0] * V
        for i in range(V):
            for node in adj[i]:
                indegree[node] += 1

        q = deque()
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)

        topo = []
        while q:
            node = q.popleft()
            topo.append(node)
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        if len(topo) == V:
            return topo
        return []
