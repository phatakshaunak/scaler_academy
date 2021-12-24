'''Q1. Distribute Candy
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?



Problem Constraints

1 <= N <= 105
-109 <= A[i] <= 109



Input Format

First and only argument is an integer array A representing the rating of children.



Output Format

Return an integer, representing the minimum candies to be given.



Example Input

Input 1:

 A = [1, 2]
Input 2:

 A = [1, 5, 2, 1]


Example Output

Output 1:

 3
Output 2:

 7


Example Explanation

Explanation 1:

 The candidate with 1 rating gets 1 candy and candidate with rating 2 cannot get 1 candy as 1 is its neighbor. 
 So rating 2 candidate gets 2 candies. In total, 2 + 1 = 3 candies need to be given out.
Explanation 2:

 Candies given = [1, 3, 2, 1]'''

class Solution:
	# @param A : list of integers
	# @return an integer
	def candy(self, A):

        n = len(A)

        l = [1] * n
        r = [1] * n

        # l[0] = 1
        # r[n-1] = 1
        # Consider left neighbors
        for i in range(1, n):
            if A[i] > A[i-1]:
                l[i] = l[i-1] + 1
            # else:
            #     l[i] = 1
        
        # Consider right neighbors
        for i in range(n-2, -1, -1):
            if A[i] > A[i+1]:
                r[i] = r[i+1] + 1
            # else:
            #     r[i] = 1
        
        ans = 0
        for i in range(n):
            ans = ans + max(l[i], r[i])
        
        return ans