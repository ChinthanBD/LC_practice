# https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/submissions/1376771569/?envType=daily-question&envId=2024-09-02
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
       
        total_chalk = sum(chalk)
        k = k % total_chalk  # Reduce k by modulo the sum of chalk
        
        for i, chalk_amount in enumerate(chalk):
            if k < chalk_amount:
                return i
            k -= chalk_amount
        
        return -1       
        # i = 0

        # while k>=chalk[i]:
        #     k-=chalk[i]
        #     i= (i+1) % len(chalk)
        
        # return i
