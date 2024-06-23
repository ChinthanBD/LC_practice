class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m,n = len(word1), len(word2)
        i,j = 0, 0
        ans = ''
        while i<m and j<n:
            ans+=word1[i]
            ans+=word2[j]
            i+=1
            j+=1
        
        if i<m:
            ans+=word1[i:]
            i+=1

        if j<n:
            ans+=word2[j:]
            j+=1

        return ans

        