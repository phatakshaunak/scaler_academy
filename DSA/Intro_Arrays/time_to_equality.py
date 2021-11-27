'''Q4. Time to equality
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an integer array A of size N. In one second you can increase the value of one element by 1.

Find the minimum time in seconds to make all elements of the array equal.


Problem Constraints

1 <= N <= 1000000
1 <= A[i] <= 1000


Input Format

First argument is an integer array A.


Output Format

Return an integer denoting the minimum time to make all elements equal.


Example Input

A = [2, 4, 1, 3, 2]


Example Output

8


Example Explanation

We can change the array A = [4, 4, 4, 4, 4]. The time required will be 8 seconds.
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        
        # This will have a time complexity of O(n)
        maximum = max(A)
        sec = 0
        
        # This will have a time complexity of O(n)
        for i in A:
            sec += (maximum - i)
        
        return sec


# O(n) time, O(1) space
