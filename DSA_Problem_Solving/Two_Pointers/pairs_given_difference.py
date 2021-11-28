'''Q2. Pairs with Given Difference
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an one-dimensional integer array A of size N and an integer B.

Count all distinct pairs with difference equal to B.

Here a pair is defined as an integer pair (x, y), where x and y are both numbers in the array and their absolute difference is B.



Problem Constraints

1 <= N <= 104

0 <= A[i], B <= 105



Input Format

First argument is an one-dimensional integer array A of size N.

Second argument is an integer B.



Output Format

Return an integer denoting the count of all distinct pairs with difference equal to B.



Example Input

Input 1:

 A = [1, 5, 3, 4, 2]
 B = 3
Input 2:

 A = [8, 12, 16, 4, 0, 20]
 B = 4
Input 3:

 A = [1, 1, 1, 2, 2]
 B = 0


Example Output

Output 1:

 2
Output 2:

 5
Output 3:

 2


Example Explanation

Explanation 1:

 There are 2 unique pairs with difference 3, the pairs are {1, 4} and {5, 2} 
Explanation 2:

 There are 5 unique pairs with difference 4, the pairs are {0, 4}, {4, 8}, {8, 12}, {12, 16} and {16, 20} 
Explanation 3:

 There are 2 unique pairs with difference 0, the pairs are {1, 1} and {2, 2}.'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        A.sort()
        if len(A) < 2:
            return 0
    
        count = 0
        N = len(A)
        i, j = 0, 1
        
        while j < N:
            
            if A[j] - A[i] < B:
                j += 1
            
            elif A[j] - A[i] > B:
                i += 1
            
            else:
                if i != j:
                # print('i', i, 'j', j, 'A[i]', A[i], 'A[j]', A[j])
                    count += 1
                    x, y = A[i], A[j]

                    # Skip duplicates while A[i] == A[i+1] won't work as even if i < N i+1 can go out of range
                    while i < N and A[i] == x:
                        i += 1

                    while j < N and A[j] == y:
                        j += 1
                else:
                    j += 1
                
        return count

        # hm = {}

        # for val in A:
        #     if val not in hm:
        #         hm[val] = 1
        #     else:
        #         hm[val] += 1

        # N = len(A)
        # ans = 0
        # for j in range(len(A)):

        #     if (A[j] - B) in hm:

        #         if B == 0:
        #             if hm[A[j]] > 1:
        #                 ans += 1
        #                 del hm[A[j]]
        #         else:
        #             ans += 1
        #             del hm[A[j] - B]
        
        # return ans