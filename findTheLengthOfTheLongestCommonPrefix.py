# https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/submissions/1400798159/?envType=daily-question&envId=2024-09-24

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_number = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, number):
        node = self.root
        for digit in str(number):
            if digit not in node.children:
                node.children[digit] = TrieNode()
            node = node.children[digit]
        node.is_end_of_number = True

    def longest_common_prefix(self, number):
        node = self.root
        common_length = 0
        for digit in str(number):
            if digit in node.children:
                node = node.children[digit]
                common_length += 1
            else:
                break
        return common_length




class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
    # Create a trie and insert all numbers from arr2
        trie = Trie()
        for number in arr2:
            trie.insert(number)

        max_prefix_len = 0

        # For each number in arr1, find the longest common prefix with any number in arr2
        for number in arr1:
            prefix_len = trie.longest_common_prefix(number)
            max_prefix_len = max(max_prefix_len, prefix_len)

        return max_prefix_len
