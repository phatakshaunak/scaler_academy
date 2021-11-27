'''Q1. Wave Array
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an array of integers A, sort the array into a wave like array and return it, In other words, arrange the elements into a sequence such that

a1 >= a2 <= a3 >= a4 <= a5…..
note : If there are multiple answers possible, return the one that's lexicographically smallest.



Problem Constraints

1 <= len(A) <= 106
1 <= A[i] <= 106



Input Format

First argument is an integer array A.



Output Format

Return an array arranged in the sequence as described.



Example Input

Input 1:

A = [1, 2, 3, 4]
Input 2:

A = [1, 2]


Example Output

Output 1:

[2, 1, 4, 3]
Output 2:

[2, 1]


Example Explanation

Explanation 1:

One possible answer : [2, 1, 4, 3]
Another possible answer : [4, 1, 3, 2]
First answer is lexicographically smallest. So, return [2, 1, 4, 3].
Explanation 1:

Only possible answer is [2, 1].'''

class Solution:
	# @param A : list of integers
	# @return a list of integers
	def wave(self, A):

        A.sort()

        for i in range(1, len(A), 2):

            A[i], A[i-1] = A[i-1], A[i]
        
        return A

'''Q2. Largest Number
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a array A of non negative integers, arrange them such that they form the largest number.

Note: The result may be very large, so you need to return a string instead of an integer.



Problem Constraints

1 <= len(A) <= 100000
0 <= A[i] <= 2*109



Input Format

First argument is an array of integers.



Output Format

Return a string representing the largest number.



Example Input

Input 1:

 A = [3, 30, 34, 5, 9]
Input 2:

 A = [2, 3, 9, 0]


Example Output

Output 1:

 "9534330"
Output 2:

 "9320"


Example Explanation

Explanation 1:

 A = [3, 30, 34, 5, 9]
 Reorder the numbers to [9, 5, 34, 3, 30] to form the largest number.
Explanation 2:

 Reorder the numbers to [9, 3, 2, 0] to form the largest number 9320.'''

import functools

def cmp(a,b):
    if a+b < b+a:
        return 1
    return -1

class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        
        A = [str(num) for num in A]
        
        # for i in range(len(A)-1):
        #     for j in range(i+1,len(A)):
                
        #         if (A[i] + A[j]) < (A[j] + A[i]):
        #             A[i], A[j] = A[j], A[i]
        
        A = sorted(A,key=functools.cmp_to_key(cmp))
        
        if A[0] == '0':
            return '0'
            
        return ''.join(A)

