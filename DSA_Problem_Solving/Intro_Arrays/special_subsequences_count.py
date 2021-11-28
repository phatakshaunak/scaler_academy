'''Q1. Special Subsequences "AG"
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

You have given a string A having Uppercase English letters.

You have to find that how many times subsequence "AG" is there in the given string.

NOTE: Return the answer modulo 109 + 7 as the answer can be very large.



Problem Constraints

1 <= length(A) <= 105



Input Format

First and only argument is a string A.



Output Format

Return an integer denoting the answer.



Example Input

Input 1:

 A = "ABCGAG"
Input 2:

 A = "GAB"


Example Output

Output 1:

 3
Output 2:

 0


Example Explanation

Explanation 1:

 Subsequence "AG" is 3 times in given string 
Explanation 2:

 There is no subsequence "AG" in the given string.

'''
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        c_a = 0
        count = 0
        
        for i in A:
            if i == 'A':
                c_a += 1
            
            elif i == 'G':
                count += c_a
                
        # c_g = 0
        # for i in range(len(A)-1,-1,-1):
        #     if A[i] == 'G':
        #         c_g += 1
        #     elif A[i] == 'A':
        #         count += c_g
        
        return count % (int(1e9+7))
        
        # 'ABCGAG'