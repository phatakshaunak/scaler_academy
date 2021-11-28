'''Q2. Sub-array with 0 sum
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an array of integers A, find and return whether the given array contains a non-empty subarray with a sum equal to 0.

If the given array contains a sub-array with sum zero return 1 else return 0.



Problem Constraints

1 <= |A| <= 100000

-10^9 <= A[i] <= 10^9



Input Format

The only argument given is the integer array A.



Output Format

Return whether the given array contains a subarray with a sum equal to 0.



Example Input

Input 1:

 A = [1, 2, 3, 4, 5]
Input 2:

 A = [-1, 1]


Example Output

Output 1:

 0
Output 2:

 1


Example Explanation

Explanation 1:

 No subarray has sum 0.
Explanation 2:

 The array has sum 0.'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        
        hs = set()
        hs.add(0)
        curr = 0
        
        for val in A:
            curr += val
            
            if curr in hs:
                return 1
                
            hs.add(curr)
        
        return 0
        
        # using a running sum is space efficient ; can also use a prefix sum array to do the same thing just extra memory
    #     A: [1, -2, 2, 4, 0, -4]
    # ps:  0, 1, -1, 1, 5, 0, 1
    #     curr = 1, -1, 
            
