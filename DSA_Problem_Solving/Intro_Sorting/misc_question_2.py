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

'''Q3. Unique Elements
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

You are given an array A of N elements. You have to make all elements unique, to do so in one step you can increase any number by one.

Find the minimum number of steps.



Problem Constraints

1 <= N <= 105
1 <= A[i] <= 109



Input Format

The only argument given is an Array A, having N integers.



Output Format

Return the Minimum number of steps required to make all elements unique.



Example Input

Input 1:

 A = [1, 1, 3]
Input 2:

 A = [2, 4, 5]


Example Output

Output 1:

 1
Output 2:

 0


Example Explanation

Explanation 1:

 We can increase the value of 1st element by 1 in 1 step and will get all unique elements. i.e [2, 1, 3].
Explanation 2:

 All elements are distinct.'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        A.sort()

        ans = 0

        for i in range(1, len(A)):

            if A[i] == A[i - 1]:
                ans += 1
                A[i] += 1
            
            elif A[i] < A[i-1]:
                ans = ans + A[i-1] - A[i] + 1
                A[i] = A[i] + A[i-1] - A[i] + 1
        
        return ans

'''Q4. Elements Removal
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an integer array A of size N. In one operation, you can remove any element from the array, and the cost of this operation is the sum of all elements in the array present before this operation.

Find the minimum cost to remove all elements from the array.



Problem Constraints

0 <= N <= 1000
1 <= A[i] <= 103



Input Format

First and only argument is an integer array A.



Output Format

Return an integer denoting the total cost of removing all elements from the array.



Example Input

Input 1:

 A = [2, 1]
Input 2:

 A = [5]


Example Output

Output 1:

 4
Output 2:

 5


Example Explanation

Explanation 1:

 Given array A = [2, 1]
 Remove 2 from the array => [1]. Cost of this operation is (2 + 1) = 3.
 Remove 1 from the array => []. Cost of this operation is (1) = 1.
 So, total cost is = 3 + 1 = 4.
 
Explanation 2:

 There is only one element in the array. So, cost of removing is 5.'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        
        A.sort()
        cost = 0
        N = len(A)
        
        for i in range(len(A)):
            cost += (N*A[i])
            N -= 1
        
        return cost

