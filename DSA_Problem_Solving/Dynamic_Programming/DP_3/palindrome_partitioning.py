'''Q3. Palindrome Partitioning II
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a string A, partition A such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of A.



Problem Constraints

1 <= length(A) <= 501



Input Format

The first and the only argument contains the string A.



Output Format

Return an integer, representing the minimum cuts needed.



Example Input

Input 1:

 A = "aba"
Input 2:

 A = "aab"


Example Output

Output 1:

 0
Output 2:

 1


Example Explanation

Explanation 1:

 "aba" is already a palindrome, so no cuts are needed.
Explanation 2:

 Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.'''

class Solution:
    # @param A : string
    # @return an integer
    def minCut(self, A):

        # First get a 2D array filled for whether a substring is a palindrome
        dp = self.pal_substrings(A)

        # Iterate over suffix and try all cuts

        # Define a 1-D array to store cuts needed upto index i to make palindromic substrings for s[0 : i + 1]
        n = len(A)
        arr = [0 for i in range(n)]

        for j in range(1, n):
            
            # Ans variable to store min cuts needed until j
            ans = float('inf')

            # Define left index i
            for i in range(j, 0, -1):
                # Start checking cuts from index j to index 1 as s[0] is already a palindrome

                # Check from dp if substring s[i:j+1] is a palindrome
                if dp[i][j]:
                    # Update ans with value until previous index, i.e. i - 1

                    # Check if given prefix substring is already a palindrome
                    if dp[0][j]:
                        ans = 0
                    
                    else:
                        ans = min(ans, 1 + arr[i - 1])
            
            # Update final answer until index j
            arr[j] = ans
        
        return arr[n - 1]
    
    # Overall TC: O(N^2), SC: O(N^2)
    
    # Helper function to find if any substring is a palindrome. Returns a filled 2D array
    def pal_substrings(self, s):
    
        n = len(s)
        
        # Define 2D DP table
        dp = [[None for i in range(n)] for j in range(n)]
        # Iterate through length of substrings possible (1 to n)
        for i in range(1, n + 1):
            
            # Multiple start positions are possible
            for st in range(n - i + 1):
                # Calculate end index for substring
                e = i - 1 + st
                
                # Base cases, length 1 and 2
                if st == e:
                    dp[st][e] = True
                
                elif e - st + 1 == 2:
                    # Substring length 2, True if chars match
                    if s[st] == s[e]:
                        dp[st][e] = True
                    else:
                        dp[st][e] = False
                
                # Usual recurrence relation
                elif s[st] == s[e]:
                    # Check if previous substring is also valid
                    dp[st][e] = True and dp[st + 1][e - 1]
                else:
                    # Not a valid palindrome
                    dp[st][e] = False
        
        return dp