'''Q1. Bulbs
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

N light bulbs are connected by a wire.

Each bulb has a switch associated with it, however due to faulty wiring, a switch also changes the state of all the bulbs to the right of current bulb.

Given an initial state of all bulbs, find the minimum number of switches you have to press to turn on all the bulbs.

You can press the same switch multiple times.

Note: 0 represents the bulb is off and 1 represents the bulb is on.



Problem Constraints

1 <= N <= 5*105
0 <= A[i] <= 1



Input Format

The first and the only argument contains an integer array A, of size N.



Output Format

Return an integer representing the minimum number of switches required.



Example Input

Input 1:

 A = [0, 1, 0, 1]
Input 2:

 A = [1, 1, 1, 1]


Example Output

Output 1:

 4
Output 2:

 0


Example Explanation

Explanation 1:

 press switch 0 : [1 0 1 0]
 press switch 1 : [1 1 0 1]
 press switch 2 : [1 1 1 0]
 press switch 3 : [1 1 1 1]
Explanation 2:

 There is no need to turn any switches as all the bulbs are already on.'''

class Solution:
	# @param A : list of integers
	# @return an integer
	def bulbs(self, A):
	    
	    '''
	    If zero and count odd, do not increment count
	    If zero and count even, increment count
	    If one and count even, do not increment count
	    If one and count odd, increment count
	    '''
	    
	    count = 0
	    
	    for num in A:
	        
	        if (num == 0) and (count % 2 == 0):
	            count += 1
	        
	        elif (num == 1) and (count % 2 != 0):
	            count += 1
	    
	    return count
	    
	   # O(N) time, O(1) space
	    
	   # 0 1 2 3
