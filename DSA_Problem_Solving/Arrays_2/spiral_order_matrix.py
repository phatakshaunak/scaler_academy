'''Q1. Spiral Order Matrix II
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order.



Problem Constraints

1 <= A <= 1000



Input Format

First and only argument is integer A


Output Format

Return a 2-D matrix which consists of the elements in spiral order.



Example Input

Input 1:

1
Input 2:

2


Example Output

Output 1:

[ [1] ]
Output 2:

[ [1, 2], [4, 3] ]


Example Explanation

Explanation 1:

 
Only 1 is to be arranged.
Explanation 2:

1 --> 2
      |
      |
4<--- 3'''

class Solution:
	# @param A : integer
	# @return a list of list of integers
	def generateMatrix(self, A):
	    
	    top, bottom, left, right = 0, (A-1), 0, (A-1)
	    
	    ans = [[0]*A for i in range(A)]
	    count = 1
	    
	    while (top <= bottom) and (left <= right):
	        
	        for i in range(left, right+1):
	            ans[top][i] += count
	            count += 1
	        top += 1
	        
	        for j in range(top, bottom+1):
	            ans[j][right] += count
	            count += 1
	        right -= 1
	        
	        for k in range(right, left-1, -1):
	            ans[bottom][k] += count
	            count += 1
	        bottom -= 1
	        
	        for l in range(bottom, top-1, -1):
	            ans[l][left] += count
	            count += 1
	        left += 1
	    
	    return ans     