'''Q3. Sum of min and max
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an array A of both positive and negative integers.

Your task is to compute sum of minimum and maximum elements of all sub-array of size B.

NOTE: Since the answer can be very large, you are required to return the sum modulo 109 + 7.



Problem Constraints

1 <= size of array A <= 105

-109 <= A[i] <= 109

1 <= B <= size of array



Input Format

The first argument denotes the integer array A.
The second argument denotes the value B



Output Format

Return an integer that denotes the required value.



Example Input

Input 1:

 A = [2, 5, -1, 7, -3, -1, -2]
 B = 4
Input 2:

 A = [2, -1, 3]
 B = 2


Example Output

Output 1:

 18
Output 2:

 3


Example Explanation

Explanation 1:

 Subarrays of size 4 are : 
    [2, 5, -1, 7],   min + max = -1 + 7 = 6
    [5, -1, 7, -3],  min + max = -3 + 7 = 4      
    [-1, 7, -3, -1], min + max = -3 + 7 = 4
    [7, -3, -1, -2], min + max = -3 + 7 = 4   
    Sum of all min & max = 6 + 4 + 4 + 4 = 18 
Explanation 2:

 Subarrays of size 2 are : 
    [2, -1],   min + max = -1 + 2 = 1
    [-1, 3],   min + max = -1 + 3 = 2
    Sum of all min & max = 1 + 2 = 3'''

    from collections import deque

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        n = len(A)
        ans = 0
        m = int(1e9+7)

        # First compute sliding window minimum sum for window size B

        # Use a deque to store indices of minimum elements
        q = deque()

        for i in range(n):

            # Remove from rear until elements are greater than A[i]
            while q and A[q[-1]] > A[i]:
                q.pop()
            
            # Append index
            q.append(i)

            # Remove out of window indices
            if q[0] <= (i - B):
                q.popleft()
            
            # Add to answer if index >= B - 1
            if i >= B - 1:
                ans = (ans % m + A[q[0]] % m) % m
        
        # Clear deque for sliding window maximum
        while q: q.pop()

        # Compute sliding window maximum sum for window size B

        for j in range(n):

            # Remove elements from the rear until they are smaller than A[i]
            while q and A[q[-1]] < A[j]:
                q.pop()
            
            # Append index
            q.append(j)

            # Remove out of window indices from the front
            if q[0] <= (j - B):
                q.popleft()
                
            # Add to the answer if index >= B - 1
            if j >= B - 1:
                ans = (ans % m + A[q[0] % m]) % m
        
        return ans

        # TC O(N), SC O(N)