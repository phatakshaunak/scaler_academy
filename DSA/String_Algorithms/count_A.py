'''Q1. Count A
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

You are given a string A. Find the number of substrings that start and end with 'a'.



Problem Constraints

1 <= |A| <= 105

String will have only lowercase English letters.



Input Format

Given the only argument is a String A.



Output Format

Return number of substrings that start and end with 'a'.



Example Input

Input 1:

 A = "aab"
Input 2:

 A = "bcbc"


Example Output

Output 1:

 3
Output 2:

 0


Example Explanation

Explanation 1:

 Substrings that start and end with 'a' are:
    1. "a"
    2. "aa"
    3. "a"
Explanation 2:

 There are no substrings that start and end with 'a'.'''

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):

        ans, ct = 0, 0

        N = len(A)

        for i in range(N):
            if A[i] == 'a':
                ans = ans + ct + 1
                ct = ct + 1
        
        return ans