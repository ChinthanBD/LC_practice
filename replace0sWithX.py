# https://bit.ly/3QyPr5g

class Solution:
    def fill(self, n, m, mat):
        visited = set()
        
        def dfs(i, j):
            visited.add((i, j))
            for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m:
                    if mat[ni][nj] == 'O' and (ni, nj) not in visited:
                        dfs(ni, nj)
        
        # Traverse top and bottom rows
        for i in range(m):
            if mat[0][i] == 'O':
                dfs(0, i)
            if mat[n-1][i] == 'O':
                dfs(n-1, i)
        
        # Traverse left and right columns
        for j in range(n):
            if mat[j][0] == 'O':
                dfs(j, 0)
            if mat[j][m-1] == 'O':
                dfs(j, m-1)
        
        # Convert 'O' to 'X' if they are not in the visited set
        for i in range(n):
            for j in range(m):
                if (i, j) not in visited and mat[i][j] == 'O':
                    mat[i][j] = 'X'
        
        return mat