# https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/?envType=daily-question&envId=2024-07-20
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m = len(rowSum)
        n = len(colSum)
        ans = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                val = min(rowSum[i], colSum[j])
                ans[i][j] = val
                rowSum[i] -= val
                colSum[j] -= val
        
        return ans
