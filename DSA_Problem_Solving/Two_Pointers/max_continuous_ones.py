'''Q2. Max Continuous Series of 1s
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a binary array A, find the maximum sequence of continuous 1's that can be formed by replacing at-most B zeroes.

For this problem, return the indices of maximum continuous series of 1s in order.

If there are multiple possible solutions, return the sequence which has the minimum start index.



Problem Constraints

0 <= B <= 105

1 <= size(A) <= 105

A[i]==0 or A[i]==1



Input Format

First argument is an binary array A.

Second argument is an integer B.



Output Format

Return an array of integers denoting the indices(0-based) of 1's in the maximum continuous series.



Example Input

Input 1:

 A = [1 1 0 1 1 0 0 1 1 1 ]
 B = 1
Input 2:

 A = [1, 0, 0, 0, 1, 0, 1]
 B = 2


Example Output

Output 1:

 [0, 1, 2, 3, 4]
Output 2:

 [3, 4, 5, 6]


Example Explanation

Explanation 1:

 Flipping 0 present at index 2 gives us the longest continous series of 1's i.e subarray [0:4].
Explanation 2:

 Flipping 0 present at index 3 and index 5 gives us the longest continous series of 1's i.e subarray [3:6].'''

class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return a list of integers
	def maxone(self, A, B):

        i, j, l, r = 0, 0, -1, -1
        n = len(A)
        ans = -1
        while j < n:
        
            '''
            During each movement of j, we are ensuring we land on a valid subarray (i.e. count of zeros <= B). If not, we shrink by moving i until the contraints are satisfied
            Then we keep monitoring our answer and updating it if we encounter a larger consecutive one sequence
            '''
            if A[j] == 0:
                B -= 1
            
            while B < 0:
                if A[i] == 0:
                    B += 1
                i += 1
            
            if (j - i + 1) > ans:
                ans = (j - i + 1)
                l, r = i, j

            j += 1
        
        return [val for val in range(l,r+1)]

'''
https://www.youtube.com/watch?v=nKhteIRZ2Ok
'''