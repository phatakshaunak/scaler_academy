'''Q1. Check Palindrome
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Write a recursive function that checks whether a string A is a palindrome or Not.
Return 1 if the string A is palindrome, else return 0.

Note: A palindrome is a string that's the same when reads forwards and backwards.



Problem Constraints

1 <= A <= 50000

String A consist only of lowercase letters.



Input Format

First and only argument is a string A.



Output Format

Return 1 if the string A is palindrome, else return 0.



Example Input

Input 1:

 A = "naman"
Input 2:

 A = "strings"


Example Output

Output 1:

 1
Output 2:

 0


Example Explanation

Explanation 1:

 "naman" is a palindomic string, so return 1.
Explanation 2:

 "strings" is not a palindrome, so return 0.'''

import sys

sys.setrecursionlimit(1000000)

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        
        def ispal(A,l,r):
            
            # Base Case
            if l >= r:
                return 1
            
            # Recursive Cases
            if A[l] == A[r]:
                return ispal(A,l+1,r-1)
                
            return 0
        
        l, r = 0, (len(A)-1)
        
        return ispal(A,l,r)
        
        
'''Q2. Find Fibonacci
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

The Fibonacci numbers are the numbers in the following integer sequence.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..

In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation:

Fn = Fn-1 + Fn-2

Given a number A, find and return the Ath Fibonacci Number.

Given that F0 = 0 and F1 = 1.



Problem Constraints

0 <= A <= 20



Input Format

First and only argument is an integer A.



Output Format

Return an integer denoting the Ath term of the sequence.



Example Input

Input 1:

 A = 2
Input 2:

 A = 9


Example Output

Output 1:

 1
Output 2:

 34


Example Explanation

Explanation 1:

 f(2) = f(1) + f(0) = 1
Explanation 2:

 f(9) = f(8) + f(7) = 21 + 13  = 34'''

class Solution:
    # @param A : integer
    # @return an integer
    def findAthFibonacci(self, A):
        
        # Base Case
        if A <= 1:
            return A
        
        return self.findAthFibonacci(A-1) + self.findAthFibonacci(A-2)

'''Q1. Sum of Digits!
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a number A, we need to find sum of its digits using recursion.



Problem Constraints

1 <= A <= 109



Input Format

First and only argument is an integer A.



Output Format

Return an integer denoting the sum of digits of the number A.



Example Input

Input 1:

 A = 46
Input 2:

 A = 11


Example Output

Output 1:

 10
Output 2:

 2


Example Explanation

Explanation 1:

 Sum of digits of 46 = 4 + 6 = 10
Explanation 2:

 Sum of digits of 11 = 1 + 1 = 2'''

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        
        arr = []
        while A > 0:
            arr.append(A%10)
            A = A // 10
        
        arr.reverse()
        N = len(arr)
        
        def rec_sum(arr):
            
            # Base case
            if len(arr) == 1:
                return arr[0]
            
            # Recursive case
            return arr[0] + rec_sum(arr[1:])
        
        return rec_sum(arr)