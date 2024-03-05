# https://www.geeksforgeeks.org/problems/rat-in-a-maze-problem/1
#User function Template for python3

class Solution:
    def findPath(self, m, n):
        def dfs(x, y, path):
            if x == n - 1 and y == n - 1:
                paths.append("".join(path))
                return
            
            directions = [(1, 0, 'D'), (-1, 0, 'U'), (0, 1, 'R'), (0, -1, 'L')]
            
            for dx, dy, d in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and m[nx][ny] == 1:
                    visited[nx][ny] = True
                    dfs(nx, ny, path + [d])
                    visited[nx][ny] = False

        if m[0][0] == 0 or m[n - 1][n - 1] == 0:
            return []

        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True
        paths = []
        dfs(0, 0, [])
        return sorted(paths) if paths else ["-1"]