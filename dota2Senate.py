# https://leetcode.com/problems/dota2-senate/submissions/1406243113/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        D, R = deque(), deque()

        for i, c in enumerate(senate):
            if c == 'R':
                R.append(i)
            else:
                D.append(i)
        
        while R and D:
            d_index = D.popleft()
            r_index = R.popleft()

            if d_index < r_index:
                D.append(d_index+len(senate))
            else:
                R.append(r_index+len(senate))
        
        return "Radiant" if R else "Dire"

