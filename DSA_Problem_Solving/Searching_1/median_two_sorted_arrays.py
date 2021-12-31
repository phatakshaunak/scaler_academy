'''Q2. Median of Array
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

There are two sorted arrays A and B of size N and M respectively.

Find the median of the two sorted arrays ( The median of the array formed by merging both the arrays ).

NOTE:

The overall run time complexity should be O(log (m+n)).
IF the number of elements in the merged array is even, then the median is the average of (n/2)th and (n/2+1)th element. For example, if the array is [1 2 3 4], the median is (2 + 3) / 2.0 = 2.5.


Problem Constraints

1 <= N, M <= 106



Input Format

First argument is an integer array A of size N.
Second argument is an integer array B of size M.



Output Format

Return a decimal value denoting the median of two sorted arrays.



Example Input

Input 1:

 A = [1, 4, 5]
 B = [2, 3]
Input 2:

 A = [1, 2, 3]
 B = [4]


Example Output

Output 1:

 3.0
Output 2:

 2.5


Example Explanation

Explanation 1:

 The median of both the sorted arrays will be 3.0.
Explanation 2:

 The median of both the sorted arrays will be (2+3)/2 = 2.5.'''

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):

        if len(A) > len(B):
            return self.findMedianSortedArrays(B, A)
        
        n, m = len(A), len(B)

        if not A:
            if m & 1:
                return B[m//2]

            return (B[m//2] + B[m//2 - 1]) / 2

        s, e = 0, n - 1
        half = (n + m) // 2

        # Run a while True loop for handling some edge cases
        while True:

            mid = s + (e - s) // 2
            b = half - mid - 2

            # Cases when choosing all or no elements from either arrays to partition, handle out of bounds using -inf and +inf

            A_left = A[mid] if mid >= 0 else float('-inf')
            B_left = B[b] if b >= 0 else float('-inf')

            A_right = A[mid + 1] if mid < (n - 1) else float('inf')
            B_right = B[b + 1] if b < (m - 1) else float('inf')

            # Condition when split is correct
            if A_left <= B_right and B_left <= A_right:

                # Check if odd
                if (n + m) & 1:
                    # Median will be the minimum of the right elements of A and B
                    return min(A_right, B_right)

                # Median will be average of max of left elements and min of right elements of A and B
                return (max(A_left, B_left) + min(A_right, B_right)) / 2
            
            # When we choose less elements from A
            elif B_left > A_right:
                # Move low to mid + 1
                s = mid + 1
            
            else:
                # When we choose more elements from A
                # A_left > B_right
                e = mid - 1
        
        return 0