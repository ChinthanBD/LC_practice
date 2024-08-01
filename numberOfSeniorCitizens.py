# https://leetcode.com/problems/number-of-senior-citizens/submissions/1340971895/?envType=daily-question&envId=2024-08-01
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = 0
        for citizen_detail in details:
            age = int(citizen_detail[11:13])

            if age > 60:
                ans +=1
        return ans
