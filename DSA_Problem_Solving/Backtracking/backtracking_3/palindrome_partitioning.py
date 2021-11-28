'''Q2. Palindrome Partitioning
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a string A, partition A such that every string of the partition is a palindrome.

Return all possible palindrome partitioning of A.

Ordering the results in the answer : Entry i will come before Entry j if :
len(Entryi[0]) < len(Entryj[0]) OR
(len(Entryi[0]) == len(Entryj[0]) AND len(Entryi[1]) < len(Entryj[1])) OR * * *
(len(Entryi[0]) == len(Entryj[0]) AND ... len(Entryi[k] < len(Entryj[k]))


Problem Constraints

1 <= len(A) <= 15



Input Format

First argument is a string A of lowercase characters.



Output Format

Return a list of all possible palindrome partitioning of s.



Example Input

Input 1:

A = "aab"
Input 2:

A = "a"


Example Output

Output 1:

 [
    ["a","a","b"]
    ["aa","b"],
  ]
Output 2:

 [
    ["a"]
  ]


Example Explanation

Explanation 1:

In the given example, ["a", "a", "b"] comes before ["aa", "b"] because len("a") < len("aa").
Explanation 2:

In the given example, only partition possible is "a" .'''

class Solution:
    # @param A : string
    # @return a list of list of strings
    def partition(self, A):

        N = len(A)
        idx, curr, ans = 0, [], []

        self.recurse(0, A, curr, ans, N)

        return ans

    def recurse(self, idx, A, curr, ans, N):

        if idx == N:
            ans.append(curr.copy())
            return
        
        for i in range(idx, N):

            if self.is_pal(A[idx:i+1]):
                curr.append(A[idx:i+1])
                self.recurse(i+1, A, curr, ans, N)
                curr.pop()
    
    def is_pal(self, st):
        i, j = 0, len(st) - 1

        while i < j:
            if st[i] != st[j]:
                return False
            i += 1
            j -= 1
        return True

    # TC: n * 2^n, SC: O(n)... n is the length of the string
