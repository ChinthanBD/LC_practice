# https://www.geeksforgeeks.org/problems/alien-dictionary/1
#User function Template for python3
from collections import defaultdict

class Solution:
    def findOrder(self, alien_dict, N, K):
        adj = defaultdict(list)
        
        # Step 1: Create the adjacency list
        for i in range(N - 1):
            s1, s2 = alien_dict[i], alien_dict[i + 1]
            length = min(len(s1), len(s2))
            for j in range(length):
                if s1[j] != s2[j]:
                    adj[ord(s1[j]) - ord('a')].append(ord(s2[j]) - ord('a'))
                    break

        visited = set()  # Set to keep track of visited vertices
        stack = []  # Stack to store the topological sort order

        def dfs(node):
            visited.add(node)  # Mark the current node as visited
            # Recur for all the vertices adjacent to this vertex
            for neighbour in adj[node]:
                if neighbour not in visited:
                    dfs(neighbour)  # Perform DFS on the unvisited neighbor
            stack.append(node)  # Push the current node to the stack after visiting all its neighbors

        # Perform DFS for all vertices to cover disconnected components
        for i in range(K):
            if i not in visited:
                dfs(i)  # Call DFS on the unvisited vertex

        # Convert integers back to characters
        ans = ""
        for c in stack[::-1]:
            ans += chr(c + ord('a'))
        return ans