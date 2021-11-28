'''Q1. Minimum Absolute Difference
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an array of integers A, find and return the minimum value of | A [ i ] - A [ j ] | where i != j and |x| denotes the absolute value of x.



Problem Constraints

1 <= length of the array <= 100000

-109 <= A[i] <= 109



Input Format

The only argument given is the integer array A.



Output Format

Return the minimum value of | A[i] - A[j] |.



Example Input

Input 1:

 A = [1, 2, 3, 4, 5]
Input 2:

 A = [5, 17, 100, 11]


Example Output

Output 1:

 1
Output 2:

 6


Example Explanation

Explanation 1:

 The absolute difference between any two adjacent elements is 1, which is the minimum value.
Explanation 2:

 The minimum value is 6 (|11 - 5| or |17 - 11|).'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        if len(A) == 1:
            return A[0]
        
        A.sort()
        min_val = float("inf")
        for i in range(1,len(A)):
            if abs(A[i]-A[i-1]) < min_val:
                min_val = abs(A[i]-A[i-1])
        
        return min_val

'''Time complexity O(nlogn), Space complexity O(n) for sorting'''
