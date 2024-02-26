#  https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/?envType=study-plan-v2&envId=top-interview-150


from typing import List
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        ans = []
        word_length = len(words[0])
        total_length = len(words) * word_length
        word_count = {}

        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        for i in range(len(s) - total_length + 1):
            substring = s[i:i + total_length]
            word_seen = {}
            j = 0
            while j < total_length:
                word = substring[j:j + word_length]
                if word in word_count:
                    if word in word_seen:
                        word_seen[word] += 1
                    else:
                        word_seen[word] = 1

                    if word_seen[word] > word_count[word]:
                        break
                else:
                    break
                j += word_length
            if j == total_length:
                ans.append(i)

        return ans
