from collections import deque

class Node:
    def __init__(self):
        # Array to store links to child nodes (26 for each letter of the alphabet)
        self.links = [None] * 26
        # Counter to track the number of words that end at this node
        self.end_of_word = 0
        # Counter to track the number of words that have this node as a prefix
        self.prefix = 0

class Trie:
    def __init__(self):
        # Initialize the root node of the trie
        self.root = Node()
        
    def insert(self, word):
        # Insert a word into the trie
        node = self.root
        for char in word:
            # Calculate the position of the character in the links array
            pos = ord(char) - ord('a')
            # If the node doesn't have a child node corresponding to the character, create one
            if not node.links[pos]:
                node.links[pos] = Node()
            node = node.links[pos]
            # Increment the prefix count for each node as we traverse the trie
            node.prefix += 1
        # Increment the end_of_word count for the final node
        node.end_of_word += 1
        

    def countWordsEqualTo(self, word):
        # Initialize the current node as the root of the trie.
        node = self.root
        
        # Traverse through each character in the word.
        for char in word:
            # Calculate the index of the character in the links array.
            pos = ord(char) - ord('a')
            
            # If the current character doesn't exist in the trie, return 0.
            if not node.links[pos]:
                return 0
            
            # Move to the next node corresponding to the current character.
            node = node.links[pos]
            
        # Return the count of occurrences of the word in the trie.
        return node.end_of_word

    def countWordsStartingWith(self, word):
        # Initialize the current node as the root of the trie.
        node = self.root
        
        # Traverse through each character in the prefix.
        for char in word:
            # Calculate the index of the character in the links array.
            pos = ord(char) - ord('a')
            
            # If the current character doesn't exist in the trie, return 0.
            if not node.links[pos]:
                return 0
            
            # Move to the next node corresponding to the current character.
            node = node.links[pos]
            
        # Return the count of words with the given prefix in the trie.
        return node.prefix


    def erase(self, word):
        # Remove a word from the trie
        node = self.root
        for char in word:
            pos = ord(char) - ord('a')
            if not node.links[pos]:
                # Word doesn't exist in the trie, so nothing to erase
                return
            node = node.links[pos]
            # Decrement prefix count for the current node as we traverse the trie
            node.prefix -= 1
        # If the word exists in the trie, decrement the end_of_word count
        if node.end_of_word > 0:
            node.end_of_word -= 1
