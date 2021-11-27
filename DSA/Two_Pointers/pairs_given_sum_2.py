'''Q1. Pairs with given sum II
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a sorted array of integers (not necessarily distinct) A and an integer B, find and return how many pair of integers ( A[i], A[j] ) such that i != j have sum equal to B.

Since the number of such pairs can be very large, return number of such pairs modulo (109 + 7).



Problem Constraints

1 <= |A| <= 100000

1 <= A[i] <= 10^9

1 <= B <= 10^9



Input Format

The first argument given is the integer array A.

The second argument given is integer B.



Output Format

Return the number of pairs for which sum is equal to B modulo (10^9+7).



Example Input

Input 1:

A = [1, 1, 1]
B = 2
Input 2:

 
A = [1, 1]
B = 2


Example Output

Output 1:

 3
Output 2:

 1


Example Explanation

Explanation 1:

 Any two pairs sum up to 2.
Explanation 2:

 only pair (1, 2) sums up to 2.'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        
        hm = {}
        i, j = 0, len(A) - 1
        ans=  0
        m = int(1e9+7)
        
        for val in A:
            
            if (B - val) in hm:
                ans = (ans % m + hm[B - val] % m) % m
            
            if val in hm:
                hm[val] += 1
            else:
                hm[val] = 1
        
        return ans
        
        # while i < j:
            
        #     if A[i] + A[j] > B:
        #         j -= 1
            
        #     elif A[i] + A[j] < B:
        #         i += 1
            
        #     else:
        #         if A[i] == A[j]:
        #             x = (j - i + 1)
        #             ans = (ans % m + (x * (x - 1) // 2) % m) % m
        #             return ans
                
        #         else:
        #             l, r = 1, 1
                    
        #             while A[i] == A[i + 1]:
        #                 l += 1
        #                 i += 1
                    
        #             while A[j] == A[j - 1]:
        #                 r += 1
        #                 j -= 1
                    
        #             i += 1
        #             j -= 1
                
        #             ans = ans % m + (l % m * r % m) % m
            
        # return ans % m
            
            