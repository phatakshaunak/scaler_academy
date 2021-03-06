'''Q1. Word Break
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Given a string A and a dictionary of words B, determine if A can be segmented into a space-separated sequence of one or more dictionary words.

Input Format:

The first argument is a string, A.
The second argument is an array of strings, B.
Output Format:

Return 0 / 1 ( 0 for false, 1 for true ) for this problem.
Constraints:

1 <= len(A) <= 6500
1 <= len(B) <= 10000
1 <= len(B[i]) <= 20
Examples:

Input 1:
    A = "myinterviewtrainer",
    B = ["trainer", "my", "interview"]

Output 1:
    1

Explanation 1:
    Return 1 ( corresponding to true ) because "myinterviewtrainer" can be segmented as "my interview trainer".

Input 2:
    A = "a"
    B = ["aaa"]

Output 2:
    0

Explanation 2:
    Return 0 ( corresponding to false ) because "a" cannot be segmented as "aaa".'''

import sys
sys.setrecursionlimit(int(1e6))
class Solution:
    # @param A : string
    # @param B : list of strings
    # @return an integer
    def wordBreak(self, A, B):

        N = len(A)
        
        idx = 0
        memo = [-1 for i in range(len(A))]
        
        ans = self.recurse(idx, A, B, N, memo)
        
        return ans

    def recurse(self, s, st, d, n, memo):

        if s == n:
            
            return 1

        if memo[s] == -1:
            memo[s] = 0
            for i in range(s, n):
                
                if st[s:i + 1] in d:
                    
                    if self.recurse(i + 1, st, d, n, memo):
                        memo[s] = 1

                        return memo[s]
                
            memo[s] = 0
            
        return memo[s]