;;;'''Q5. Count ways to make sum of odd and even indexed elements equal by removing an array element
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an array, arr[] of size N, the task is to find the count of array indices such that removing an element from these indices makes the sum of even-indexed and odd-indexed array elements equal.



Problem Constraints

1<=n<=1e5
-1e5<=A[i]<=1e5


Input Format

First argument contains an array A of integers of size N


Output Format

Return the count of array indices such that removing an element from these indices makes the sum of even-indexed and odd-indexed array elements equal.



Example Input

Input 1:
A=[2, 1, 6, 4]
Input 2:

A=[1, 1, 1]


Example Output

Output 1:
1
Output 2:

3


Example Explanation

Explanation 1:
Removing arr[1] from the array modifies arr[] to { 2, 6, 4 } such that, arr[0] + arr[2] = arr[1]. 
Therefore, the required output is 1. 
Explanation 2:

 Removing arr[0] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1] 
Removing arr[1] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1] 
Removing arr[2] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1] 
Therefore, the required output is 3.'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        
        if len(A) == 1:
            return 1
        
        n = len(A)
        # We will start traversing the array from i = 0 to i = n-1. For i =0, compute four variables, l_odd, l_even, r_odd and r_even
        
        l_odd, l_even, r_odd, r_even = 0, 0, 0, 0
        count = 0
        
        for i in range(1,n):
            if i % 2 == 0:
                r_odd += A[i]
            else:
                r_even += A[i]
        
        if l_odd + r_odd == l_even + r_even:
            count += 1
        
        i = 1
        
        while i <= n-1:
            
            if (i-1) % 2 == 0: # Removing the odd index
                l_even += A[i-1]
                r_even -= A[i]
            else: # Removing the even index
                l_odd += A[i-1]
                r_odd -= A[i]
            
            if l_odd + r_odd == l_even + r_even:
                count += 1
            
            i += 1
        
        # A prefix sum array solution with O(N) time and O(N) space is also possible for this problem. That is as follows
        
        return count
            
# Time complexity O(N), space complexity O(1)
'''Intuition: The idea is to consider the index to be removed as a partition and then compute the even and odd sums. This is similar to the equilibrium index problem. 
   A similar logic to the equilibrium index problem for this class, we can consider 4 separate sums ; left_odd, left_even and right_odd, right_even. 
   The idea is to understand how these four variables will change (i.e. what needs to be added/subtracted) as we traverse each index of the array
   Similar to the equilibrium index question, we intialize our four sums assuming the 0th index was removed. After that we can continue traversing and manipulating the
   variables based on what index is being removed
'''