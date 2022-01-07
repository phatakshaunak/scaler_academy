'''Q3. Longest Common Subsequence
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given two strings A and B. Find the longest common subsequence ( A sequence which does not need to be contiguous), which is common in both the strings.

You need to return the length of such longest common subsequence.



Problem Constraints

1 <= Length of A, B <= 1005



Input Format

First argument is a string A.
Second argument is a string B.



Output Format

Return an integer denoting the length of the longest common subsequence.



Example Input

Input 1:

 A = "abbcdgf"
 B = "bbadcgf"
Input 2:

 A = "aaaaaa"
 B = "ababab"


Example Output

Output 1:

 5
Output 2:

 3


Example Explanation

Explanation 1:

 The longest common subsequence is "bbcgf", which has a length of 5.
Explanation 2:

 The longest common subsequence is "aaa", which has a length of 3.'''

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):

        # State will represented by i and j where i and j are indices for A and B
        # To follow a bottom up approach,
        # For transitions, if characters match, we get the answer from i-1, j-1 and add 1 to it
        # Else, we get the max value from decrementing an index on either strings

        n1, n2 = len(A), len(B)
        ans = 0
        
        # Add an extra row/column 0 padding to avoid many edge cases to store the subsequences
        
        dp = [[0 for i in range(n1 + 1)] for j in range(n2 + 1)]

        for i in range(n1):

            for j in range(n2):

                if A[i] == B[j]:

                    # Get answer by decrementing i and j by 1
                    # Also use j as first indexer as we are iterating down the rows for each column
                    dp[j + 1][i + 1] = 1 + dp[j][i]
                
                else:
                    # Max value from 1 row or column offset
                    dp[j + 1][i + 1] = max(dp[j + 1][i], dp[j][i + 1])
                
                # Update ans
                ans = max(ans, dp[j + 1][i + 1])
        
        return ans