class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = 1
        ans = ''
        nums =[]
        for i in range(1,n):
            fact = fact * i
            nums.append(i)
        nums.append(n)
            
        k = k-1
        while True:
            index = k //fact
            char = nums[index]
            ans += str(char)
            nums.remove(char)
            if len(nums) ==0:
                break
            k = k % fact
            fact = fact//len(nums)
        return ans
