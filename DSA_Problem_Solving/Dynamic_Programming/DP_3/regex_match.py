'''Q1. Regular Expression II
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Implement wildcard pattern matching with support for ' ? ' and ' * ' for strings A and B.

' . ' : Matches any single character.
' * ' : Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).



Problem Constraints

1 <= length(A), length(B) <= 104



Input Format

The first argument of input contains a string A.
The second argument of input contains a string B denoting the pattern.



Output Format

Return 1 if the patterns match else return 0.



Example Input

Input 1:

 A = "aab"
 B = "c*a*b"
Input 2:

 A = "acz"
 B = "a.a"


Example Output

Output 1:

 1
Output 2:

 0


Example Explanation

Explanation 1:

 'c' can be repeated 0 times, 'a' can be repeated 1 time. Therefore, it matches "aab".
 So, return 1.
Explanation 2:

 '.' matches any single character. First two character in string A will be match. 
 But the last character i.e 'z' != 'a'. Return 0.'''

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def isMatch(self, A, B):
        
        return 1 if self.tabular(A, B) else 0
    
    def tabular(self, s, p):

        n, m = len(s), len(p)

        dp = [[False for i in range(m + 1)] for j in range(n + 1)]

        # Match empty strings
        dp[0][0] = True

        # Iterate first row
        for i in range(1, m + 1):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i - 2]
            else:
                dp[0][i] = False

        # Iterate first column, all false except first cell
        for j in range(1, n + 1):
            dp[j][0] = False

        # Iterate string and pattern
        for i in range(1, n + 1):

            for j in range(1, m + 1):
                
#                 print(i, j)
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    # Get answer from previous diagonal
                    dp[i][j] = dp[i - 1][j - 1]

                # If characters do not match
                elif s[i - 1] != p[j - 1] and p[j - 1].isalpha():
                    dp[i][j] = False

                # If we get a *
                # elif p[j - 1] == '*':
                else:
                    # If previous character in pattern matches current string char or is a ., 
                    # Consider answer for multiple matches from previous row and if char* matches nothing
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j - 2] or dp[i - 1][j]

                    else:
                        # Get answer if we match nothing
                        dp[i][j] = dp[i][j - 2]
        
        return dp[n][m]