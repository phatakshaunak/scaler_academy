'''Q2. Sort stack using another stack
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a stack of integers A, sort it using another stack.

Return the array of integers after sorting the stack using another stack.



Problem Constraints

1 <= |A| <= 5000

0 <= A[i] <= 1000000000



Input Format

The only argument given is the integer array A.



Output Format

Return the array of integers after sorting the stack using another stack.



Example Input

Input 1:

 A = [5, 4, 3, 2, 1]
Input 2:

 A = [5, 17, 100, 11]


Example Output

Output 1:

 [1, 2, 3, 4, 5]
Output 2:

 [5, 11, 17, 100]


Example Explanation

Explanation 1:

 Just sort the given numbers.
Explanation 2:

 Just sort the given numbers.'''
 class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

        s1, s2 = [], []

        while A:
            x = A.pop()

            while s1 and s1[-1] > x:
                A.append(s1.pop())
            
            s1.append(x)

        return s1

        # for i in range(len(A)):

        #     if not s1 or s1[-1] <= A[i]:
        #         s1.append(A[i])
            
        #     else:
        #         while s1 and A[i] < s1[-1]:
        #             s2.append(s1.pop())

        #         s1.append(A[i])
            
        #     while s2:
        #         s1.append(s2.pop())
        
        # return s1

