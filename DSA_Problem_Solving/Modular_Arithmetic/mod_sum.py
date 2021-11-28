'''Q1. Mod Sum
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an array of integers A, calculate the sum of A [ i ] % A [ j ] for all possible i, j pairs. Return sum % (109 + 7) as an output.



Problem Constraints

1 <= length of the array A <= 105

1 <= A[i] <= 103



Input Format

The only argument given is the integer array A.



Output Format

Return a single integer denoting sum % (109 + 7).



Example Input

Input 1:

 A = [1, 2, 3]
Input 2:

 A = [17, 100, 11]


Example Output

Output 1:

 5
Output 2:

 61


Example Explanation

Explanation 1:

 (1 % 1) + (1 % 2) + (1 % 3) + (2 % 1) + (2 % 2) + (2 % 3) + (3 % 1) + (3 % 2) + (3 % 3) = 5'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        
        mod = int(1e9+7)
        ans = 0
        hm = {}
        
        for i in A:
            if i not in hm:
                hm[i] = 1
            else:
                hm[i] += 1
        
        for v1 in hm:
            for v2 in hm:
                if v1 != v2:
                    cont = hm[v1] * hm[v2]
                    ans = (ans % mod + (cont * (v1 % v2)) % mod) % mod
        
        return ans
        