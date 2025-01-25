# https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        
        q = []
        num_to_queue ={}

        for n in sorted(nums):
            if not q or abs(n - q[-1][-1]) > limit:
                q.append(deque())    
            q[-1].append(n)
            num_to_queue[n] = len(q) -1
        
        ans = []
        for n in nums:
            ele = q[num_to_queue[n]].popleft()
            ans.append(ele)
        
        return ans

