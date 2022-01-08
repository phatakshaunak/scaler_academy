'''Q1. Ways to Decode
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message denoted by string A containing digits, determine the total number of ways to decode it modulo 109 + 7.

.



Problem Constraints

1 <= length(A) <= 105



Input Format

The first and the only argument is a string A.



Output Format

Return an integer, representing the number of ways to decode the string modulo 109 + 7..



Example Input

Input 1:

 A = "12"
Input 2:

 A = "8"


Example Output

Output 1:

 2
Output 2:

 1


Example Explanation

Explanation 1:

 Given encoded message "8", it could be decoded as only "H" (8).
 The number of ways decoding "8" is 1.
Explanation 2:

 Given encoded message "12", it could be decoded as "AB" (1, 2) or "L" (12).
 The number of ways decoding "12" is 2.'''

import sys
sys.setrecursionlimit(int(1e6))
class Solution:
	# @param A : string
	# @return an integer
	def numDecodings(self, A):

        mod, memo = int(1e9 + 7), [-1] * len(A)

        # return self.decode_ways(A, 0, mod, memo)

        return self.decode_tab(A)
    
    # Recursion with memoization (Top to bottom)
    def decode_ways(self, A, idx, m, cache):
    
        if idx == len(A):
            return 1
        
        if cache[idx] != -1:
            return cache[idx]

        # Single digit cut
        if '1' <= A[idx] <= '9':
            
            cache[idx] = self.decode_ways(A, idx + 1, m, cache)
        
        # Double digit cut
        if idx + 1 < len(A):
            if ('1' <= A[idx] < '2' and '0' <= A[idx + 1] <= '9') or (A[idx] == '2' and A[idx + 1] <= '6'):
                cache[idx] += self.decode_ways(A, idx + 2, m, cache)
        
        # If code enters if condition, cuts are not valid at idx, return 0

        if cache[idx] == -1:
            cache[idx] = 0

        return cache[idx] % m
    
    # O(2^n) with plain recursion, O(n) with memoization

    # Tabulation bottom up
    def decode_tab(self, s):

        # Define storage array
        dp = [0] * len(s)

        # Define number of ways to cut at first index
        if '1' <= s[0] <= '9':
            dp[0] = 1
        
        else:
            # No decoding possible if first value is not within 1-9
            return 0
        
        for i in range(1, len(s)):

            if '1' <= s[i] <= '9':
                dp[i] += dp[i - 1]
            
            if '10' <= (s[i - 1] + s[i]) <= '26':

                if i == 1:
                    dp[i] += 1
                else:
                    dp[i] += dp[i - 2]
        
        return dp[-1] % int(1e9 + 7)