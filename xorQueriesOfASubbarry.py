# https://leetcode.com/problems/xor-queries-of-a-subarray/?envType=daily-question&envId=2024-09-13
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        prefix = [0] * (n + 1)  # Create prefix array with an extra 0 at the beginning
        
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] ^ arr[i - 1]
        
        # Step 2: Process each query
        ans = []
        for start, end in queries:
            ans.append(prefix[end + 1] ^ prefix[start])
        
        return ans
