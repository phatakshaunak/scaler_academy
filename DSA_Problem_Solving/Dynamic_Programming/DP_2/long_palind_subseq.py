'''Q1. Longest Palindromic Subsequence
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a string A. Find the longest palindromic subsequence (A subsequence which does not need to be contiguous and is a palindrome).

You need to return the length of longest palindromic subsequence.



Problem Constraints

1 <= length of(A) <= 103



Input Format

First and only integer is a string A.



Output Format

Return an integer denoting the length of longest palindromic subsequence.



Example Input

Input 1:

 A = "bebeeed"
Input 2:

 A = "aedsead"


Example Output

Output 1:

 4
Output 2:

 5


Example Explanation

Explanation 1:

 The longest palindromic subsequence is "eeee", which has a length of 4.
Explanation 2:

 The longest palindromic subsequence is "aedea", which has a length of 5.'''

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):

        return self.long_pal_sub_tab(A)
    
    def long_pal_sub_tab(self, s):
    
        n = len(s)
        dp = [[0 for i in range(n)] for j in range(n)]
        
        # We build the answer by calculating the answers for substrings starting at length 1 to len(s)
        # Iterate through a loop from 1 to N
        for i in range(1, n + 1):
            
            # There are multiple starting positions, 0 to N - i
            for st in range(0, n - i + 1):
                
                # Get end index using start and length
                e = i - 1 + st
                
                # If one length, add one to the answer (diagonal)
                if st == e:
                    dp[st][e] = 1
                
                # For a length two string, we can write a separate case to correctly fill the answer
                # Or simply use the recurrence relation of going to st + 1, e - 1 since invalid cells are
                # filled with zero
                elif s[st] == s[e]:
                    dp[st][e] = 2 + dp[st + 1][e - 1]
                
                # When characters are not equal
                else:
                    dp[st][e] = max(dp[st + 1][e], dp[st][e - 1])
        
        return dp[0][n - 1]

    def l_pal_sub_rec(self, s, dp, i, j):
        
        # Out of bounds
        if i > j:
            return 0
        
        # Single character is a palindrome
        if i == j:
            return 1
        
        if s[i] == s[j]:
            if dp[i][j] == -1:
                dp[i][j] = 2 + self.l_pal_sub_rec(s, dp, i + 1, j - 1)
        
        else:
            if dp[i][j] == -1:
                dp[i][j] = max(self.l_pal_sub_rec(s, dp, i, j - 1), self.l_pal_sub_rec(s, dp, i + 1, j))
        
        return dp[i][j]

    # Applying LCS on the string and its reverse, we can get the answer
    def lcs_bottom_space(self, s1, s2):
        
        # Per recurrence relation only two arrays are needed to compute the answer
        # Define a 2 arrays of column size equal to the length of any of the strings
        
        n1, n2 = len(s1), len(s2)
        ans = float('-inf')
        # Extra 0 pad to avoid edge case problems
        
        # Initially dp1 is filled with zeros and acts as an initializer for the first character comparison from
        # s2 and all of s1
        dp1, dp2 = [0] * (n1 + 1), [0] * (n1 + 1)
        
        # Iterate over s2 on the outer loop and s1 in the inner loop
        
        for i in range(1, n2 + 1):
            
            for j in range(1, n1 + 1):
                
                if s2[i - 1] == s1[j - 1]:
                    dp2[j] = 1 + dp1[j - 1]
                
                else:
                    dp2[j] = max(dp1[j], dp2[j - 1])
                
                ans = max(ans, dp2[j])
            
            # After comparing one character of s2 with all of s1, swap the rows for the next iteration
            dp1, dp2 = dp2, dp1
        
        return ans