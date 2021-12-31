'''Q2. ADD OR NOT
Unsolved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an array of integers A of size N and an integer B.

In a single operation, any one element of array can be increased by 1. You are allowed to do atmost B such operations.

Find the number with maximum number of occurrences and return an array C of size 2, where C[0] is number of occurence and C[1] is the number with maximum occurence.
If there are several such numbers, your task is to find the minimum one.



Problem Constraints

1 <= N <= 105

-109 <= A[i] <= 109

0 <= B <= 109



Input Format

The first argument given is the integer array A.
The second argument given is the integer B.



Output Format

Return an array C of size 2, where C[0] is number of occurence and C[1] is the number with maximum occurence.



Example Input

Input 1:

 A = [3, 1, 2, 2, 1]
 B = 3
Input 2:

 A = [5, 5, 5]
 B = 3


Example Output

Output 1:

 [4, 2]
Output 2:

 [3, 5]


Example Explanation

Explanation 1:

 Apply operations on A[2] and A[4]
 A = [3, 2, 2, 2, 2]
 Maximum occurence =  4
 Minimum value of element with maximum occurence = 2
Explanation 2:

 A = [5, 5, 5]
 Maximum occurence =  3
 Minimum value of element with maximum occurence = 5'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):

        '''
        Approach involves first sorting the array. Then check for an optimal value of elements that can be transformed 
        to maximize frequency of current element. This check can be done with binary search. To check if it can be done 
        under B operations, compute a prefix sum array and check if the difference of sum and the max possible sum 
        i.e. frequency * current element is <= B. Do for all elements and update answer
        Sorting ensures a minimum possible optimal answer is chosen.
        '''

        A.sort()
        n = len(A)
        ps = [0] * (n + 1)
        
        # Calculate prefix sum for check during binary search
        for i in range(n):
            ps[i+1] = ps[i] + A[i]

        freq = float('-inf')
        ans = -1

        for i in range(n):
            
            # Low is 1 counting A[i], High is the number of elements until A[i]
            s, e = 1, i + 1

            while s <= e:
                # Find mid (here it is the count of elements to check)
                ct = s + (e - s) // 2

                # Potential operations needed for current count
                ops = (ct * A[i]) - (ps[i+1] - ps[i + 1 - ct])

                # If operations are <= B, possible answer, update if old frequency is lower and move right to search for a better answer
                if ops <= B:
                    if ct > freq:
                        freq = ct
                        ans = A[i]
                    s = ct + 1
                # Smaller count is possible, move left
                else:
                    e = ct - 1
            
        return [freq, ans]