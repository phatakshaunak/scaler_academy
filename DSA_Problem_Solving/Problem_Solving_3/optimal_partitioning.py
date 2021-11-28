'''Q1. Optimal Partitioning
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

You are given an array A having N integers.

You have to divide / split the array into 2 subsequence partitions such that:

Both the partitions are non-empty.
Each integer A[i] in the array belongs to exactly one of the two partitions.
Absolute difference between the maximum of first partition and the minimum of second partition is minimum possible.
If B and C represent the two partitions, then size(B) >= 1, size(C) >= 1 and |max(B) - min(C)| is minimum possible. You have to find such a spliting and tell the minimum value of |max(B) - max(C)|.



Problem Constraints

2 <= N <= 105

-109 <= A[i] <= 109



Input Format

First and only argument is an integer array A.



Output Format

Return a single integer denoting the absolute difference.



Example Input

Input 1:

 A = [3, 1, 2, 6, 4]
Input 2:

 A = [2, 1, 3, 2, 4, 3]


Example Output

Output 1:

 1 
Output 2:

 0 


Example Explanation

Explanation 1:

 B = [1, 2, 4]
 C = [3, 6]
 max(B) = 4, min(C) = 3
 abs(max(B) - min(C)) = abs(4 - 3) = abs(1) = 1 
Explanation 2:

 B = [2, 1]
 C = [3, 2, 4, 3]
 max(B) = 2, min(C) = 2
 abs(max(B) - min(C)) = abs(2 - 2) = abs(0) = 0'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        
        A.sort()
        
        min_diff = float("inf")
        
        for i in range(1, len(A)):
            
            min_diff = min((A[i]-A[i-1]),min_diff)
            
        return min_diff
