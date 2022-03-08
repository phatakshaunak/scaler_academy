'''Q2. Interleaving Strings
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given A, B, C find whether C is formed by the interleaving of A and B.



Problem Constraints

1 <= length(A), length(B) <= 100

1 <= length(C) <= 200



Input Format

The first argument of input contains a string, A.
The second argument of input contains a string, B.
The third argument of input contains a string, C.



Output Format

Return 1 if string C is formed by interleaving of A and B else 0.



Example Input

Input 1:

 A = "aabcc"
 B = "dbbca"
 C = "aadbbcbcac"
Input 2:

 A = "aabcc"
 B = "dbbca"
 C = "aadbbbaccc"


Example Output

Output 1:

 1
Output 2:

 0


Example Explanation

Explanation 1:

 "aa" (from A) + "dbbc" (from B) + "bc" (from A) + "a" (from B) + "c" (from A)
Explanation 2:

 It is not possible to get C by interleaving A and B.'''

class Solution:
	# @param A : string
	# @param B : string
	# @param C : string
	# @return an integer
	def isInterleave(self, A, B, C):
        
        # Sanity Check
        if len(A) + len(B) != len(C):
            return 0
        
        dp = [[-1 for i in range(len(B))] for j in range(len(A))]

        return 1 if self.rec_memo(A, B, C, 0, 0, 0, dp) else 0

    def rec_memo(self, s1, s2, s3, i, j, k, dp):
        
        if i == len(s1) and j == len(s2):
            
            # If all strings exhausted
            if k == len(s3):
                return True
            
            # No interleaving possible
            return False
        
        # Check remaining substrings of s2 and s3
        if i == len(s1):
            return True if s2[j:] == s3[k:] else False

        # Check remaining substrings of s1 and s3
        if j == len(s2):
            return True if s1[i:] == s3[k:] else False
        
        if dp[i][j] == -1:
            dp[i][j] = False
            
            if s1[i] == s3[k]:
                dp[i][j] = dp[i][j] or self.rec_memo(s1, s2, s3, i + 1, j, k + 1, dp)
            
            # Check with s2 only if previous call returned False as we need to check only if an interleaving is possible and not the count
            if s2[j] == s3[k] and not dp[i][j]:
                dp[i][j] = dp[i][j] or self.rec_memo(s1, s2, s3, i, j + 1, k + 1, dp)
        
        return dp[i][j]
    
    # TC O(len(A)*len(B)), SC O(len(A)*len(B))