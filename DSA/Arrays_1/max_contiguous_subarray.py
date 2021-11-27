'''Q6. Max Sum Contiguous Subarray
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Find the contiguous subarray within an array, A of length N which has the largest sum.



Problem Constraints

1 <= N <= 1e6
-1000 <= A[i] <= 1000



Input Format

The first and the only argument contains an integer array, A.



Output Format

Return an integer representing the maximum possible sum of the contiguous subarray.



Example Input

Input 1:

 A = [1, 2, 3, 4, -10] 
Input 2:

 A = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 


Example Output

Output 1:

 10 
Output 2:

 6 


Example Explanation

Explanation 1:

 The subarray [1, 2, 3, 4] has the maximum possible sum of 10. 
Explanation 2:

 The subarray [4,-1,2,1] has the maximum possible sum of 6.'''

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        
        if len(A) == 1:
            return A[0]
        
        if max(A) < 0:
            return max(A)
            
        max_sum, curr = 0, 0
        s,e,start = 0, 0, 0
        
        for i in range(len(A)):
            curr += A[i]
            
            if curr < 0:
                curr = 0
                s = i + 1
            
            if curr > max_sum:
                max_sum = curr
                start = s
                end = i
        
        return max_sum

# Kadane's Algorithm TC O(N) SC O(1)