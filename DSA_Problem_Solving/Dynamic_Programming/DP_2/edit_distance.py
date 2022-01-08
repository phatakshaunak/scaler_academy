'''Q2. Edit Distance
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given two strings A and B, find the minimum number of steps required to convert A to B. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character


Problem Constraints

1 <= length(A), length(B) <= 450



Input Format

The first argument of input contains a string, A.
The second argument of input contains a string, B.



Output Format

Return an integer, representing the minimum number of steps required.



Example Input

Input 1:

 A = "abad"
 B = "abac"
Input 2:

 A = "Anshuman"
 B = "Antihuman


Example Output

Output 1:

 1
Output 2:

 2


Example Explanation

Exlanation 1:

 A = "abad" and B = "abac"
 After applying operation: Replace d with c. We get A = B.
 
Explanation 2:

 A = "Anshuman" and B = "Antihuman"
 After applying operations: Replace s with t and insert i before h. We get A = B.'''

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, A, B):

        dp = [[-1] * len(B) for i in range(len(A))]

        return self.edit_distance(A, B, dp, 0, 0)

    def edit_distance(self, s1, s2, dp, i, j):
    
        #     if i == len(s1) and j == len(s2):
        #         return 0
        if i == len(s1):
            return len(s2) - j
        
        if j == len(s2):
            return len(s1) - i
        
        if s1[i] == s2[j]:
            
            if dp[i][j] == -1:
                dp[i][j] = self.edit_distance(s1, s2, dp, i + 1, j + 1)
            
        else:
            if dp[i][j] == -1:
                
                in_ = self.edit_distance(s1, s2, dp, i, j + 1)
                del_ = self.edit_distance(s1, s2, dp, i + 1, j)
                rep_ = self.edit_distance(s1, s2, dp, i + 1, j + 1)
                
                dp[i][j] = 1 + min(in_, del_, rep_)
        
        return dp[i][j]