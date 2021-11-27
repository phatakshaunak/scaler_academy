'''Q1. Find a peak element
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an array of integers A, find and return the peak element in it. An array element is peak if it is NOT smaller than its neighbors.

For corner elements, we need to consider only one neighbor. We ensure that answer will be unique.

NOTE: Users are expected to solve this in O(log(N)) time.



Problem Constraints

1 <= |A| <= 100000

1 <= A[i] <= 109



Input Format

The only argument given is the integer array A.



Output Format

Return the peak element.



Example Input

Input 1:

A = [1, 2, 3, 4, 5]
Input 2:

A = [5, 17, 100, 11]


Example Output

Output 1:

 5
Output 2:

 100


Example Explanation

Explanation 1:

 5 is the peak.
Explanation 2:

 100 is the peak.'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        
        if len(A) == 1:
            return A[0]
            
        if A[0] > A[1]:
            return A[0]
        
        if A[-1] > A[-2]:
            return A[-1]
            
        s, e = 0, len(A) - 1
        
        while s <= e:
            
            mid = (s + e) // 2
            
            #Check if mid is the peak
            if A[mid] >= A[mid - 1] and A[mid] >= A[mid + 1]:
                return A[mid]
            # Move right if A[mid] is greater than A[mid-1]
            if A[mid] > A[mid - 1]:
                s = mid + 1
            # Move left if A[mid] is greater than A[mid+1]
            else:
                e = mid - 1
        
        return -1
