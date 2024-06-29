#https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/description/?envType=daily-question&envId=2024-06-29
from collections import defaultdict, deque
from typing import List

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = [0] * n
        ancestors = [set() for _ in range(n)]

        # Build the graph and compute the indegree of each node
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        # Initialize the queue with nodes having zero indegree
        queue = deque([i for i in range(n) if indegree[i] == 0])

        # Perform BFS
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                # Add current node's ancestors to the neighbor
                ancestors[neighbor].update(ancestors[node])
                ancestors[neighbor].add(node)
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Convert sets to sorted lists
        return [sorted(list(ancestor_set)) for ancestor_set in ancestors]
