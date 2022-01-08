'''Q2. Regular Expression Match
Attempted
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Implement wildcard pattern matching with support for ' ? ' and ' * ' for strings A and B.

' ? ' : Matches any single character.
' * ' : Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).



Problem Constraints

1 <= length(A), length(B) <= 104



Input Format

The first argument of input contains a string A.
The second argument of input contains a string B.



Output Format

Return 1 if the patterns match else return 0.



Example Input

Input 1:

 A = "aaa"
 B = "a*"
Input 2:

 A = "acz"
 B = "a?a"


Example Output

Output 1:

 1
Output 2:

 0


Example Explanation

Explanation 1:

 Since '*' matches any sequence of characters. Last two 'a' in string A will be match by '*'.
 So, the pattern matches we return 1.
Explanation 2:

 '?' matches any single character. First two character in string A will be match. 
 But the last character i.e 'z' != 'a'. Return 0.'''

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def isMatch(self, A, B):

        return 1 if self.regex_tabulation_space(A, B) else 0

#         # Define storage array of size len(A) * len(B)
#         dp = [[-1] * len(B) for i in range(len(A))]
        
#         ans = self.regex_recursive(A, B, 0, 0, dp)
# #         print(dp)
#         return 1 if ans else 0

    def regex_recursive(self, A, B, i, j, dp):

        # Base Cases
        if i == len(A) and j == len(B):
            return True
        
        if i < len(A) and j == len(B):
            return False
        
        if i == len(A):
            if B[j] != '*':
                return False
            
            # Iterate until B is exhausted
            return self.regex_recursive(A, B, i, j + 1, dp)
        
#         print(i, j)
        if A[i] == B[j]:
#             print(i, j)
            if dp[i][j] == -1:

                dp[i][j] = self.regex_recursive(A, B, i + 1, j + 1, dp)
        
        elif A[i].isalpha() and B[j].isalpha() and A[i] != B[j]:
            
            if dp[i][j] == -1:
                dp[i][j] = False
        
        elif B[j] == '?':

            if dp[i][j] == -1:
                dp[i][j] = self.regex_recursive(A, B, i + 1, j + 1, dp)
        
        else:
            # Matching *
            
            if dp[i][j] == -1:

                dp[i][j] = self.regex_recursive(A, B, i, j + 1, dp) or self.regex_recursive(A, B, i + 1, j, dp)
        
        return dp[i][j]
    
    def regex_tabulation(self, s, p):
    
        n1, n2 = len(s), len(p)
        
        dp = [[0 for i in range(n2 + 1)] for j in range(n1 + 1)]
        
        # Empty strings
        dp[0][0] = True
        
        # Fill first column: empty pattern and string, all false
        for i in range(1, n1 + 1):
            dp[i][0] = False
        
        # Fill first row: False if current char in P != * else use previous column's state
        for j in range(1, n2 + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
            else:
                dp[0][j] = False
        
        # Iterate from 1st row and column
        for i in range(1, n1 + 1):
            
            for j in range(1, n2 + 1):
                
                # If both alphabets and match
                if s[i - 1].isalpha() and p[j - 1].isalpha():
                    
                    if  s[i - 1] == p[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1]
                    
                    else:
                        # Alphabets don't match, state is False
                        dp[i][j] = False
                
                # If pattern is a ?
                elif p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                
                # If pattern character is a *
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        
        return dp[n1][n2]
    
    def regex_tabulation_space(self, s, p):
    
        n1, n2 = len(s), len(p)
        
        dp1, dp2 = [0 for i in range(n2 + 1)], [0 for i in range(n2 + 1)]
        
        #dp1 initially represents comparing an empty string s with given pattern
        dp1[0] = True
        
        for i in range(1, n2 + 1):
            # If pattern char is * fill previous answer, else fill False
            if p[i - 1] == '*':
                dp1[i] = dp1[i - 1]
            else:
                dp1[i] = False
        
        # First value of dp2 should be False as it is an alphabet and can't match with empty string
        dp2[0] = False
        
        # Iterate over string and pattern
        for i in range(1, n1 + 1):
            
            for j in range(1, n2 + 1):
                
                # If both alphabets and match
                if s[i - 1].isalpha() and p[j - 1].isalpha():
                    
                    if  s[i - 1] == p[j - 1]:
                        dp2[j] = dp1[j - 1]
                    
                    else:
                        dp2[j] = False
                
                # If pattern char is a ?
                elif p[j - 1] == '?':
                    dp2[j] = dp1[j - 1]
                
                # Else, current pattern char is a *
                else:
                    dp2[j] = dp2[j - 1] or dp1[j]
            
            ans = dp2[n2]
            
            # Swap arrays
            dp1, dp2 = dp2, dp1

            #dp1 initially has a True value at 0th position, hence change that after the swap
            dp2[0] = False
        
        return ans
