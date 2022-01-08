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

        # dp = [[-1] * len(B) for i in range(len(A))]

        # return self.edit_distance(A, B, dp, 0, 0)

        # return self.edit_distance_space_tab(A, B)
        return self.edit_distance_tab(A, B)

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
    
    def edit_distance_tab(self, s1, s2):
    
        n1, n2 = len(s1), len(s2)
        
        dp = [[0] * (n2 + 1) for i in range(n1 + 1)]
        
        # for i in range(1, n1 + 1):
        #     dp[i][0] = i
        
        # for j in range(1, n2 + 1):
        #     dp[0][j] = j 

        for i in range(n1):
                
            for j in range(n2):
                
                # i + 1 deletions when target string is empty (0th column), j + 1 insertions when input string is empty (0th row)
                if j == 0:
                    dp[i + 1][j] = i + 1
                
                if i == 0:
                    dp[i][j + 1] = j + 1

                # if i != 0:
                #     dp[i][0] = i
                
                # if j != 0:
                #     dp[0][j] = j
                
                if s1[i] == s2[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                
                else:
                    in_ = dp[i + 1][j]
                    del_ = dp[i][j + 1]
                    rep_ = dp[i][j]
                    
                    dp[i +1][j + 1] = 1 + min(in_, del_, rep_)
     
        return dp[n1][n2]
    
    def edit_distance_space_tab(self, s1, s2):

        # Convert s1 to s2
        # Define two arrays of size len(s2) + 1

        n1, n2 = len(s1), len(s2)

        dp1, dp2 = [i for i in range(len(s2) + 1)], [0] * (len(s2) + 1)
        
#         print(dp1)
        ans = 0
        # Outer loop iterates over string to be converted and checks with target string character by character
        for i in range(n1):

            for j in range(n2):
                
                if j == 0:
                    dp2[j] = i+1
#                     print(dp1)
#                     print(dp2)
#                     print()

                if s1[i] == s2[j]:
                    # Previous diagonal's answer from dp1 into dp2
                    dp2[j + 1] = dp1[j]
                
                else:
                    # Insertion count
                    in_ = dp2[j]

                    # Deletion count
                    del_ = dp1[j + 1]

                    # Replace count
                    rep_ = dp1[j]

                    dp2[j + 1] = 1 + min(in_, del_, rep_)
            
            ans = dp2[-1]
            # Swap arrays to move to next row
            dp1, dp2 = dp2, dp1
        
        return ans
    
    def edit_distance_tab_1(self, s1, s2):
    
        n1, n2 = len(s1), len(s2)
        
        dp = [[0] * (n2 + 1) for i in range(n1 + 1)]

        for i in range(n1 + 1):
                
            for j in range(n2 + 1):
                
                # Empty input string, j insertions from target string
                if i == 0:
                    dp[0][j] = j
                    
                # Empty target string, i deletions from input string
                elif j == 0:
                    dp[i][j] = i
                
                # If characters match, continue with previous edit distance
                elif s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i - 1][j - 1]
                
                else:
                    
                    # Insertion maintain input string index, get answer from previous column
                    in_ = dp[i][j - 1]
                    
                    # Deletion Maintain target string index, get answer from previous row
                    del_ = dp[i - 1][j]
                    
                    # Replace Continue with previous edit distance
                    rep_ = dp[i - 1][j - 1]
                    
                    dp[i][j] = 1 + min(in_, del_, rep_)
     
        return dp[n1][n2]