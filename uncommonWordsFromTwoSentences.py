# https://leetcode.com/problems/uncommon-words-from-two-sentences/?envType=daily-question&envId=2024-09-17
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        mpp_s1 = Counter(s1.split())
        mpp_s2 = Counter(s2.split())
        ans = []
        for word, freq in mpp_s1.items():
            if freq ==1 and  mpp_s2.get(word, 0) == 0:
                ans.append(word)

        for word, freq in mpp_s2.items():
            if freq ==1 and  mpp_s1.get(word, 0) == 0:
                ans.append(word)

        return ans
