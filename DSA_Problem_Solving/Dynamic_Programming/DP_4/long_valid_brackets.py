'''Q2. Longest valid Parentheses
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a string A containing just the characters '(' and ')'.

Find the length of the longest valid (well-formed) parentheses substring.



Problem Constraints

1 <= length(A) <= 750000



Input Format

The only argument given is string A.



Output Format

Return the length of the longest valid (well-formed) parentheses substring.



Example Input

Input 1:

 A = "(()"
Input 2:

 A = ")()())"


Example Output

Output 1:

 2
Output 2:

 4


Example Explanation

Explanation 1:

 The longest valid parentheses substring is "()", which has length = 2.
Explanation 2:

 The longest valid parentheses substring is "()()", which has length = 4.'''

class Solution:
	# @param A : string
	# @return an integer
	def longestValidParentheses(self, A):

        return self.tabular(A)
    
    def tabular(self, arr):

        n = len(arr)

        dp = [0 for i in range(n)]

        ans = 0

        for i in range(1, n):

            if arr[i] == ')':

                if arr[i - 1] == '(':

                    dp[i] += 2

                    if i - 2 >= 0:

                        dp[i] += dp[i - 2]
                
                elif arr[i - 1] == ')':

                    # Check if there is a matching opening bracket
                    st = i - 1 - dp[i - 1]

                    # If st is a valid opening bracket and >=0
                    if st >= 0 and arr[st] == '(':

                        dp[i] = 2 + dp[i] + dp[i - 1]

                        # If st - 1 is valid, add previous count
                        if st - 1 >= 0:
                            dp[i] += dp[st - 1]

            ans = max(ans, dp[i])
        
        return ans