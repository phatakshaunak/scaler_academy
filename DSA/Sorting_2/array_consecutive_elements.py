'''Q2. Array with consecutive elements
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an array of positive integers A, check and return whether the array elements are consecutive or not.
NOTE: Try this with O(1) extra space.



Problem Constraints

1 <= length of the array <= 100000
1 <= A[i] <= 10^9



Input Format

The only argument given is the integer array A.



Output Format

Return 1 if the array elements are consecutive else return 0.



Example Input

Input 1:

 A = [3, 2, 1, 4, 5]
Input 2:

 A = [1, 3, 2, 5]


Example Output

Output 1:

 1
Output 2:

 0


Example Explanation

Explanation 1:

 As you can see all the elements are consecutive, so we return 1.
Explanation 2:

 Element 4 is missing, so we return 0.'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        A.sort()
        N = len(A)
        if len(A) <= 1:
            return 1

        for i in range(1, N):
            if A[i] - A[i-1] != 1:
                return 0
        
        return 1
