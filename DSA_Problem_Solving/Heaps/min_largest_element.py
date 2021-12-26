'''Q3. Minimum largest element
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an array A of N numbers, you have to perform B operations. In each operation, you have to pick any one of the N elements and add original value(value stored at index before we did any operations) to it's current value. You can choose any of the N elements in each operation.

Perform B operations in such a way that the largest element of the modified array(after B operations) is minimised. Find the minimum possible largest element after B operations.



Problem Constraints

1 <= N <= 106
0 <= B <= 105
-105 <= A[i] <= 105



Input Format

First argument is an integer array A.
Second argument is an integer B.



Output Format

Return an integer denoting the minimum possible largest element after B operations.



Example Input

Input 1:

 A = [1, 2, 3, 4] 
 B = 3
Input 2:

 A = [5, 1, 4, 2] 
 B = 5


Example Output

Output 1:

 4
Output 2:

 5


Example Explanation

Explanation 1:

 Apply operation on element at index 0, the array would change to [2, 2, 3, 4]
 Apply operation on element at index 0, the array would change to [3, 2, 3, 4]
 Apply operation on element at index 0, the array would change to [4, 2, 3, 4]
 Minimum possible largest element after 3 operations is 4.
Explanation 2:

 Apply operation on element at index 1, the array would change to [5, 2, 4, 2]
 Apply operation on element at index 1, the array would change to [5, 3, 4, 2]
 Apply operation on element at index 1, the array would change to [5, 4, 4, 2]
 Apply operation on element at index 1, the array would change to [5, 5, 4, 2]
 Apply operation on element at index 3, the array would change to [5, 5, 4, 4]
 Minimum possible largest element after 5 operations is 5.'''

import heapq
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        # Keep a state array to store new state (or a variable)
        # Make a min heap of twice the original values to choose the best possible value.
        # Change the value in the state array to the current heap min
        # Increment the current heap min with original value and push to heap
        # Repeat B times and get max value from state array

        tmp = [[2*A[i], i] for i in range(len(A))]
        # state = [i for i in A]
        state = max(A)
        heapq.heapify(tmp)
        while B:
            # print(tmp)
            top = heapq.heappop(tmp)
            state = max(state, top[0])
            # state[top[1]] = top[0]
            top[0] = top[0] + A[top[1]]
            heapq.heappush(tmp, top)
            B -= 1
        
        return state
        
        # TC O(B*logN) SC O(N)
        # max_ = float('-inf')
        # for val in state:
        #     max_ = max(max_,val)
        
        # return max_