'''Q2. Contact Finder
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

We want to make a custom contacts finder applications as part of our college project. The application must perform two types of operations:

Type 1: Add name B[i] ,denoted by 0 in vector A where B[i] is a string in vector B denoting a contact name. This must store B[i] as a new contact in the application.

Type 2: Find partial for B[i] ,denoted by 1 in vector A where B[i] is a string in vector B denoting a partial name to search the application for. It must count the number of contacts starting with B[i].

You have been given sequential add and find operations. You need to perform each operation in order.

And return as an array of integers, answers for each query of type 2(denoted by 1 in A) .



Problem Constraints

1 <= |A| <= 10000

1 <= |length of strings in B| <= 10



Input Format

First argument is the vector A, which denotes the type of query.

Second argument is the vector B, which denotes the string for corresponding query.



Output Format

Return an array of integers, denoting answers for each query of type 1.



Example Input

Input 1:

A = [0, 0, 1, 1]
B = ["hack", "hacker", "hac", "hak"]
Input 2:

A = [0, 1]
B = ["abcde", "abc"]


Example Output

Output 1:

 
[2, 0]
Output 2:

[1]


Example Explanation

Explanation 1:

 
We perform the following sequence of operations:
Add a contact named "hack".
Add a contact named "hacker".
Find the number of contact names beginning with "hac". There are currently two contact names in the application and both of them start with "hac", so we have 2.
Find the number of contact names beginning with "hak". There are currently two contact names in the application but neither of them start with "hak", so we get0.
Explanation 2:

 
Add "abcde"
Find words with prefix "abc". We have answer as 1.'''

class Solution:
    # @param A : list of integers
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A, B):

        n = len(A)
        dummy = TrieNode('dummy')
        ans = []

        for i in range(n):

            if A[i] == 0:
                root = dummy
                # Insert into the trie
                for c in B[i]:
                    if c not in root.children:
                        root.children[c] = TrieNode(c)
                    root = root.children[c]
                    root.prefixCount += 1
                root.isEnd = True
            
            else:
                # We need to search a prefix in the trie
                root = dummy
                early_flag = False
                for c in B[i]:
                    if c not in root.children:
                        early_flag = True
                        break
                    root = root.children[c]

                if not early_flag:
                    ans.append(root.prefixCount)
                else:
                    ans.append(0)
        
        return ans

class TrieNode:
    def __init__(self, char):
        self.char = char
        self.isEnd = False
        self.children = {}
        self.prefixCount = 0