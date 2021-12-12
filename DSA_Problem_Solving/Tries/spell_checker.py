'''Q2. Spelling Checker
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an array of words A (dictionary) and another array B (which contain some words).

You have to return the binary array (of length |B|) as the answer where 1 denotes that the word is present in the dictionary and 0 denotes it is not present.

Formally, for each word in B, you need to return 1 if it is present in Dictionary and 0 if it is not.

Such problems can be seen in real life when we work on any online editor (like Google Documnet), if the word is not valid it is underlined by a red line.

NOTE: Try to do this in O(n) time complexity.



Problem Constraints

1 <= |A| <= 1000

1 <= sum of all strings in A <= 50000

1 <= |B| <= 1000



Input Format

First argument is array of strings A.

First argument is array of strings B.



Output Format

Return the binary array of integers according to the given format.



Example Input

Input 1:

A = [ "hat", "cat", "rat" ]
B = [ "cat", "ball" ]
Input 2:

A = [ "tape", "bcci" ]
B = [ "table", "cci" ]


Example Output

Output 1:

[1, 0]
Output 2:

[0, 0]


Example Explanation

Explanation 1:

Only "cat" is present in the dictionary.
Explanation 2:

None of the words are present in the dictionary.'''

class Solution:
    # @param A : list of strings
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A, B):

        # Create a trie with the dictionary words. Then iterate and check all the given words
        dummy = TrieNode('dummy')
        # Loop over the dictionary words
        for word in A:
            root = dummy
            # Loop over characters
            for char in word:
                if char in root.children:
                    # If character is present, point root to that character
                    root = root.children[char]
                    # Increment counter for the root node
                    root.prefix_count += 1
                else:
                    # Add a new TrieNode for the new character to root's children and increment it's counter
                    new_node = TrieNode(char)
                    new_node.prefix_count += 1
                    root.children[char] = new_node
                    root = root.children[char]
            root.isEnd = True
        
        # Now we need to check if the given words are present in the dictionary.
        # Two failing cases, the word is present but the isEnd for last character is not True
        # Second, all the characters in the word are not present

        ans = []
        for word in B:
            early_flag = False
            # Start at the dummy node
            root = dummy
            # Loop over the words characters
            for char in word:
                # If character is not present, break out and add zero to answer
                if char not in root.children:
                    ans.append(0)
                    early_flag = True
                    break
                else:
                    # Move to the next character
                    root = root.children[char]
            
            # Once out, check if early flag is False (i.e. all characters are present, then see if isEnd is True)
            if not early_flag:
                if root.isEnd:
                    # Word is present in the dictionary
                    ans.append(1)
                else:
                    ans.append(0)
        
        return ans

class TrieNode:
    def __init__(self, char):
        self.char = char
        self.isEnd = False
        self.children = dict()
        self.prefix_count = 0