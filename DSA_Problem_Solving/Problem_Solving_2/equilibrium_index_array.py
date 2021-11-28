'''Q3. Equilibrium index of an array
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

You are given an array A of integers of size N.

Your task is to find the equilibrium index of the given array

Equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.

NOTE:

Array indexing starts from 0.
If there is no equilibrium index then return -1.
If there are more than one equilibrium indexes then return the minimum index.



Problem Constraints

1<=N<=1e5
-1e5<=A[i]<=1e5


Input Format

First arugment contains an array A .


Output Format

Return the equilibrium index of the given array. If no such index is found then return -1.


Example Input

Input 1:
A=[-7, 1, 5, 2, -4, 3, 0]
Input 2:

A=[1,2,3]


Example Output

Output 1:
3
Output 2:

-1


Example Explanation

Explanation 1:
3 is an equilibrium index, because: 
A[0] + A[1] + A[2] = A[4] + A[5] + A[6]
Explanation 1:

There is no such index.'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        
        left_sum = 0
        right_sum = sum(A[1:]) #(~O(N) complexity for taking sum)
        
        if left_sum == right_sum:
            return 0
        
        for i in range(1, len(A)):
            left_sum += A[i-1]
            right_sum -= A[i]
            
            if left_sum == right_sum:
                return i
        
        return -1

#Time complexity O(N), space complexity O(1)
'''The intuition for this problem is to understand how to slide across the array updating your sums to the left and right of the 
equilibrium indices. We need to try each index as an equilibrium index. The traversal can be either started from left->right or right->left
Initially, if A[0] is chosen as the equilibrium index, then the left sum is considered as zero as no elements to its left. 
Right sum is just sum(A[1;]). As we increase the equilibrium index, all that needs to be done is add the previous element into the 
left sum and subtract the current equilibrium index from the right sum. At the end the right sum becomes zero when we reach A[N-1]'''