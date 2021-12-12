'''Q1. Shortest Unique Prefix
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a list of N words. Find shortest unique prefix to represent each word in the list.

NOTE: Assume that no word is prefix of another. In other words, the representation is always possible



Problem Constraints

1 <= Sum of length of all words <= 106



Input Format

First and only argument is a string array of size N.



Output Format

Return a string array B where B[i] denotes the shortest unique prefix to represent the ith word.



Example Input

Input 1:

 A = ["zebra", "dog", "duck", "dove"]
Input 2:

A = ["apple", "ball", "cat"]


Example Output

Output 1:

 ["z", "dog", "du", "dov"]
Output 2:

 ["a", "b", "c"]


Example Explanation

Explanation 1:

 Shortest unique prefix of each word is:
 For word "zebra", we can only use "z" as "z" is not any prefix of any other word given.
 For word "dog", we have to use "dog" as "d" and "do" are prefixes of "dov".
 For word "du", we have to use "du" as "d" is prefix of "dov" and "dog".
 For word "dov", we have to use "dov" as "d" and do" are prefixes of "dog".  
 
Explanation 2:

 "a", "b" and c" are not prefixes of any other word. So, we can use of first letter of each to represent.'''

class Solution:
	# @param A : list of strings
	# @return a list of strings
	def prefix(self, A):

        # Create a trie
        dummy = TrieNode('dummy')

        for word in A:
            root = dummy
            for char in word:
                if char not in root.children:
                    root.children[char] = TrieNode(char)

                # Move root to char node and increment the prefix count for char
                root = root.children[char]
                root.prefix_count += 1
            # Mark the word ending
            root.isEnd = True
        
        # Now for each word find the shortest prefix, i.e. earliest node with prefix_count = 1
        ans = []
        for word in A:
            root = dummy
            curr = ''
            for char in word:
                curr = curr + char
                if root.children[char].prefix_count == 1:
                    ans.append(curr)
                    break
                else:
                    root = root.children[char]
        return ans

class TrieNode:
    def __init__(self, char):
        self.char = char
        self.isEnd = False
        self.children = dict()
        self.prefix_count = 0