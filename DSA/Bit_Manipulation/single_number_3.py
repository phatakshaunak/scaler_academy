'''Q4. Single Number III
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an array of numbers A , in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Note: Output array must be sorted.



Problem Constraints

2 <= |A| <= 100000
1 <= A[i] <= 109



Input Format

First argument is an array of interger of size N.



Output Format

Return an array of two integers that appear only once.



Example Input

Input 1:

A = [1, 2, 3, 1, 2, 4]
Input 2:

A = [1, 2]


Example Output

Output 1:

[3, 4]
Output 2:

[1, 2]


Example Explanation

Explanation 1:

 3 and 4 appear only once.
Explanation 2:

 1 and 2 appear only once.'''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        
        xor = 0
        for num in A:
            xor = xor ^ num
        
        # def find_first_set_bit(num):
        #     ct = 0
        #     while num:
        #         if num&1:
        #             return ct
        #         ct += 1
        #         num = num >> 1
        #     return -1
        
        # set_i = find_first_set_bit(xor)
        set_i = xor&(xor-1)^xor
        val1, val2 = 0, 0
        
        for a in A:
            if set_i&a:
                val1 = val1 ^ a
            else:
                val2 = val2 ^ a
            # if (a>>set_i)&1:
            #     val1 = val1 ^ a
            # else:
            #     val2 = val2 ^ a
        
        return sorted([val1,val2])