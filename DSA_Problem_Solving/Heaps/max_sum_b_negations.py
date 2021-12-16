'''Q2. Maximum array sum after B negations
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an array of integers A and an integer B. You must modify the array exactly B number of times. In single modification, we can replace any one array element A[i] by -A[i].

You need to perform these modifications in such a way that after exactly B modifications, sum of the array must be maximum.



Problem Constraints

1 <= length of the array <= 5*105
1 <= B <= 5 * 106
-100 <= A[i] <= 100



Input Format

First argument given is an integer array A.
Second argument given is an integer B.



Output Format

Return an integer denoting the maximum array sum after B modifications.



Example Input

Input 1:

 A = [24, -68, -29, -9, 84]
 B = 4
Input 2:

 A = [57, 3, -14, -87, 42, 38, 31, -7, -28, -61]
 B = 10


Example Output

Output 1:

 196
Output 2:

 362


Example Explanation

Explanation 1:

 Final array after B modifications = [24, 68, 29, -9, 84]
Explanation 2:

 Final array after B modifications = [57, -3, 14, 87, 42, 38, 31, 7, 28, 61]'''

import heapq
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        ans = sum(A)

        heapq.heapify(A)

        while B:
            if A[0] < 0:
                top = heapq.heappop(A)
                ans = ans - (2 * top)
                heapq.heappush(A, (-1 * top))
                B -= 1
            else:
                if A != 0 and B&1:
                    ans = ans - A[0] + (-1 * A[0])
                return ans

        return ans

        # Convert array to min heap
        # heapq.heapify(A)

        # Next steps: Negate all negative elements. If you encounter a 0 as min, return the sum as no negation possible. If a positive number is the min value, negate only when the # of operations left is odd
        # while B:
        #     if A[0] < 0:
        #         top = heapq.heappop(A)
        #         top = top * -1
        #         heapq.heappush(A, top)
        #         B -= 1
        #     else:
        #         if A[0] != 0 and B&1:
        #             top = heapq.heappop(A)
        #             top = top * -1
        #             heapq.heappush(A, top)
        #             B = 0
        #         # Break statement needed when A[0] is 0 or > 0 and B is odd or even. If B is even or the min element is 0, don't change anything, simply return the sum. If B is odd and positive min, change sign, break and return sum
                # break
        
        # return sum(A)