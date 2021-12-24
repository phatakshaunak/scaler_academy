'''
Q2. B-th Smallest Prime Fraction
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

A sorted array of integers, A contains 1, plus some number of primes. Then, for every p < q in the list, we consider the fraction p/q.

What is the B-th smallest fraction considered?

Return your answer as an array of integers, where answer[0] = p and answer[1] = q.



Problem Constraints

1 <= length(A) <= 2000
1 <= A[i] <= 30000
1 <= B <= length(A)*(length(A) - 1)/2



Input Format

The first argument of input contains the integer array, A.
The second argument of input contains an integer B.



Output Format

Return an array of two integers, where answer[0] = p and answer[1] = q.



Example Input

Input 1:

 A = [1, 2, 3, 5]
 B = 3
Input 2:

 A = [1, 7]
 B = 1


Example Output

Output 1:

 [2, 5]
Output 2:

 [1, 7]


Example Explanation

Explanation 1:

 The fractions to be considered in sorted order are:
 [1/5, 1/3, 2/5, 1/2, 3/5, 2/3]
 The third fraction is 2/5.
Explanation 2:

 The fractions to be considered in sorted order are:
 [1/7]
 The first fraction is 1/7.
'''

import heapq
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):

        # Assume array A is sorted
        tmp = []
        n = len(A)

        for i in range(n - 1):

            p = ((A[i] / A[n-1]), i, (n - 1))
            tmp.append(p)
        
        # O(N) down-heapify (considering non leaf nodes)
        heapq.heapify(tmp)

        while B > 0:

            top = heapq.heappop(tmp)

            # Check if another fraction with current numerator can be generated
            if top[2] > top[1] + 1:
                p = ((A[top[1]] / A[top[2] - 1]), top[1], (top[2] - 1))
                heapq.heappush(tmp, p)

            B -= 1
        
        return [A[top[1]], A[top[2]]]

        # TC: O(BlogN), SC: O(N)