'''Q3. Pick from both sides!
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an integer array A of size N.

You can pick B elements from either left or right end of the array A to get maximum sum.

Find and return this maximum possible sum.

NOTE: Suppose B = 4 and array A contains 10 elements then

You can pick first four elements or can pick last four elements or can pick 1 from front and 3 from back etc . you need to return the maximum possible sum of elements you can pick.


Problem Constraints

1 <= N <= 105

1 <= B <= N

-103 <= A[i] <= 103



Input Format

First argument is an integer array A.

Second argument is an integer B.



Output Format

Return an integer denoting the maximum possible sum of elements you picked.



Example Input

Input 1:

 A = [5, -2, 3 , 1, 2]
 B = 3
Input 2:

 A = [1, 2]
 B = 1


Example Output

Output 1:

 8
Output 2:

 2


Example Explanation

Explanation 1:

 Pick element 5 from front and element (1, 2) from back so we get 5 + 1 + 2 = 8
Explanation 2:

 Pick element 2 from end as this is the maximum we can get'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        
        # Base Cases
        '''If B = length of array A, return sum of array A
           If B = 1, and length of array A is 1, return A[0], elif length of array > 1, return max(A[0],A[len(A)-1]
        '''
        
        if B == len(A):
            return sum(A)
        
        elif B == 1 and len(A) == 1:
            return A[0]
        
        elif B == 1 and len(A) > 1:
            return max(A[0], A[len(A)-1])
        
        '''Cases when B > 1 and A > 1, O(N) space and time'''
        N = len(A)
        # # Calculate the prefix sum array
        
        # PS = [0 for i in range(N+1)]
        
        # for i in range(1,N+1):
        #     PS[i] = PS[i-1] + A[i-1]
        
        # max_sum = float('-inf')
        
        # i = B
        
        # while i >= 0 :
            
        #     curr = (PS[N] - PS[N-i]) + PS[B-i]
        #     max_sum  = max(max_sum, curr)
            
        #     i -= 1
        
        '''Fixed sliding window approach
            O(N) time, O(1) space'''
        
        max_sum = 0
        
        for i in range(N-B,N):
            max_sum += A[i]
        curr = max_sum
            
        for i in range(B):
            
            curr = curr + A[i] - A[N-B+i]
            # print(max_sum, curr, A[i], A[N-B+i],)
            max_sum = max(max_sum, curr)
        
        return max_sum