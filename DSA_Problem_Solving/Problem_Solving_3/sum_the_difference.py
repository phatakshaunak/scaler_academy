'''Q2. Sum the Difference
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an integer array A of size N.
You have to find all possible non-empty subsequence of the array of numbers and then, for each subsequence, find the difference between the largest and smallest numbers in that subsequence Then add up all the differences to get the number.

As the number may be large, output the number modulo 1e9 + 7 (1000000007).

NOTE: Subsequence can be non-contiguous.



Problem Constraints

1 <= N <= 10000

1<= A[i] <=1000



Input Format

First argument is an integer array A.



Output Format

Return an integer denoting the output.



Example Input

Input 1:

A = [1, 2]
Input 2:

A = [1]


Example Output

Output 1:

 1
Output 2:

 0


Example Explanation

Explanation 1:

All possible non-empty subsets are:
[1]    largest-smallest = 1 - 1 = 0
[2]    largest-smallest = 2 - 2 = 0
[1 2]  largest-smallest = 2 - 1 = 1
Sum of the differences = 0 + 0 + 1 = 1
So, the resultant number is 1
Explanation 2:

 Only 1 subsequence of 1 element is formed.'''

class Solution:
	# @param A : list of integers
	# @return an integer
	def solve(self, A):
	    
	    A.sort()
    
        mod = int(1e9+7)
    
        maxi, mini = 0, 0
        
        N = len(A)
        ans = 0
        for i in range(len(A)):
            
            maxi = (maxi + (2**i)*A[i]) % mod
            
            mini = (mini + (2**(N-i-1))*A[i]) % mod
        
        return (maxi - mini) % mod


'''
A = [5,3,2,6,-1]

Sorted A = [-1, 2, 3, 5, 6]

How many subsequences would 5 be the maximum: 2^3
5 ; 5,3 ; 5,3,2 ; 5,3,2,-1 ; 5,2 ; 5,-1 ; 5,3,-1 ; 5,2,-1

If we sort the array, we can traverse each subsequence using a nested loop.Two pointers i and j will determine the start (or minimum) and maximum(end) of the subsequence
Ex. in sorted array -1,2,3,5,6 ; if we have i = 0, j = 2 ; we have min = 0 & max = 3 ; We do this for all such subsequences calculating a term 2^(j-i-1) * (A[j]-A[i) ; the 2^ term determines the # of times we can observe the ith and jth element as min and max

This solution would be an O(n^2) time and O(1) space solution.

To remove the nested loop, we can tackle the min and max counts separately. The question to ask would be: How many times would an element occur as a minimum/maximum in a subsequence. We can then simply multiply the occurence and the element and add the corresponding
values to the max and min terms ultimately calculating the difference. This would be an O(N) time O(1) space solution.

The key intution here is to understand the use of applying sorting to simplify the problem. As we are dealing with subsequences and only need to consider min and max, even if sorting changes the order, we can still determine the # of times any element would be max
or min in any subsequence
'''

    