'''Q3. 3 Sum
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an array A of N integers, find three integers in A such that the sum is closest to a given number B. Return the sum of those three integers.

Assume that there will only be one solution.



Problem Constraints

-108 <= B <= 108
1 <= N <= 104
-108 <= A[i] <= 108


Input Format

First argument is an integer array A of size N.

Second argument is an integer B denoting the sum you need to get close to.



Output Format

Return a single integer denoting the sum of three integers which is closest to B.



Example Input

Input 1:

A = [-1, 2, 1, -4]
B = 1
Input 2:

 
A = [1, 2, 3]
B = 6


Example Output

Output 1:

2
Output 2:

6


Example Explanation

Explanation 1:

 The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)
Explanation 2:

 Take all elements to get exactly 6.'''

class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def threeSumClosest(self, A, B):
	    
	    A.sort()
	    ans = float('inf')
	    
	    if len(A) == 3:
	        return sum(A)
	    
	    if len(A) < 3 or A == [] or not A:
	        return 0
        
        # Run a loop fixing first index and apply two pointers to the remaining array. Run loop from i = 0 to N-2
        
        for i in range(0, len(A) - 2):

            j, k = i+1, len(A) - 1
    
            # Find a value as close to target as possible. Need to do a rolling update with each check
            while j < k:
                
                # Update ans if necessary
                if abs(A[i]+A[j]+A[k] - B) < abs(ans - B):
                        
                        ans = A[i]+A[j]+A[k]
                
                if A[i] + A[j] + A[k] > B:
                    
                    # if ans == float('inf'):
                    #     ans = A[i]+A[j]+A[k]
                        
                    # if (A[i]+A[j]+A[k]) - B < abs(ans - B):
                        
                    #     ans = (A[i]+A[j]+A[k])
                        
                    k -= 1
                    
                elif A[i] + A[j] + A[k] == B:
                    
                    return A[i] + A[j] + A[k]
                    
                else:
                    
                    # if ans == float('inf'):
                    #     ans = A[i]+A[j]+A[k]
                    
                    # if B - (A[i]+A[j]+A[k]) < abs(B - ans):
                        
                    #     ans = A[i]+A[j]+A[k]
                    
                    j += 1
        
        return ans