# https://www.geeksforgeeks.org/problems/flood-fill-algorithm1856/1

from collections import deque

class Solution:
    
    def floodFill(self, image, sr, sc, newColor):
        # m = len(image)
        # n = len(image[0])
        # initialColor = image[sr][sc]
        # queue = deque()
        # visited = set()
        # queue.append((sr, sc))
        # visited.add((sr, sc))
        # while queue:
        #     i, j = queue.popleft()
        #     image[i][j] = newColor
        #     visited.add((i, j))
        #     for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        #         neighnouri = i + di
        #         neighnourj = j + dj
        #         if 0 <= neighnouri < m and 0 <= neighnourj < n and (neighnouri, neighnourj) not in visited:
        #             if image[neighnouri][neighnourj] == initialColor:
        #                 image[neighnouri][neighnourj] = newColor
        #                 queue.append((neighnouri, neighnourj))
        # return image
    
    ################################
        #dfs Solution for flood fill
        m = len(image)
        n = len(image[0])
        startColor = image[sr][sc]  # Store the color of the starting pixel

        def dfs(i, j):
            for ni, nj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                if 0 <= i + ni < m and 0 <= j + nj < n and image[i + ni][j + nj] == startColor:
                    image[i + ni][j + nj] = newColor
                    dfs(i + ni, j + nj)

        dfs(sr, sc)
        image[sr][sc] = newColor  # Set the starting pixel to newColor
        return image
