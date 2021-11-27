'''Q2. Longest Substring Without Repeat
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a string A, find the length of the longest substring without repeating characters.

Note: Users are expected to solve in O(N) time complexity.



Problem Constraints

1 <= size(A) <= 106

String consists of lowerCase,upperCase characters and digits are also present in the string A.



Input Format

Single Argument representing string A.



Output Format

Return an integer denoting the maximum possible length of substring without repeating characters.



Example Input

Input 1:

 A = "abcabcbb"
Input 2:

 A = "AaaA"


Example Output

Output 1:

 3
Output 2:

 2


Example Explanation

Explanation 1:

 Substring "abc" is the longest substring without repeating characters in string A.
Explanation 2:

 Substring "Aa" or "aA" is the longest substring without repeating characters in string A.'''

class Solution:
	# @param A : string
	# @return an integer
	def lengthOfLongestSubstring(self, A):

        hm, i, ans = {}, 0, float('-inf')

        for j in range(len(A)):

            if A[j] not in hm:
                hm[A[j]] = 1
            else:
                hm[A[j]] += 1
            
            # Shrink the window if a duplicate is encountered
            while hm[A[j]] > 1:
                hm[A[i]] -= 1
                i += 1
            
            ans = max(ans, j - i + 1)
        
        return ans