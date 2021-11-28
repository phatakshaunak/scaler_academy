'''Q3. Strange Equality
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an integer A.
Two numbers X and Y are defined as follows:

X is the greatest number smaller than A such that XOR sum of X and A is the same as the sum of X and A.
Y is the smallest number greater than A such that XOR sum of Y and A is the same as the sum of Y and A.
Find and return the XOR of X and Y.

NOTE 1: XOR of X and Y is defined as X ^ Y where '^' is the BITWISE XOR operator.

NOTE 2: Your code will be run against a maximum of 100000 Test Cases.



Problem Constraints

1 <= A <= 109



Input Format

First and only argument is an integer A.



Output Format

Return an integer denoting the XOR of X and Y.



Example Input

A = 5


Example Output

10


Example Explanation

The value of X will be 2 and the value of Y will be 8. The XOR of 2 and 8 is 10.'''

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        
        '''
        Sum of two numbers is expressed as (A+B) = A^B + 2*(A&B)
        We need (A+B) = A^B ; i.e. we need A&B to be zero. For the smallest number greater than A, we can consider the smallest power of 2
        greater than A. In this way, all the bits of A will be unset as the MSB of a power of 2 is 1 and all others are unset.
        Similarly, the greatest number smaller than A, will be the complement of A. Here we can't simply select a smaller power of 2 as
        the MSB of A may be set. A complement will flip all bits and thus return 0
        Ex. 5 -- 101  ; 7 -- 111
        '''
        
        # To get the higher power of 2 for A, we can calculate its bit size, add 1 to it and get 2's power. 
        # To calculate complement, again use number of bits, iterate over the number and unset set bits and vice versa.
        
        def bit_size(n):
            count = 0
            while n:
                count += 1
                n = n >> 1
            return count
        
        max_bits = bit_size(A)
        
        Y = (1<<(max_bits))
        
        X = 0
        i = 0
        while A:
            if not A&1:
                X = X + (1<<i)
            A = A >> 1
            i += 1
        
        return X^Y