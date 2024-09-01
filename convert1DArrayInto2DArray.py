# https://leetcode.com/problems/convert-1d-array-into-2d-array/submissions/1375023272/?envType=daily-question&envId=2024-09-01
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        ans = []
        for r in range(m):
            start = r * n
            end = start + n
            ans.append(original[start:end])
        

        return ans
