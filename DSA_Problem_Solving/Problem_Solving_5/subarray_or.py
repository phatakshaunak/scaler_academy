'''Q3. SUBARRAY OR
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an array of integers A of size N.

Value of a subarray is defined as BITWISE OR of all elements in it.

Return the sum of Value of all subarrays of A % 109 + 7.



Problem Constraints

1 <= N <= 105

1 <= A[i] <= 108



Input Format

The first argument given is the integer array A.



Output Format

Return the sum of Value of all subarrays of A % 109 + 7.



Example Input

Input 1:

 A = [1, 2, 3, 4, 5]
Input 2:

 A = [7, 8, 9, 10]


Example Output

Output 1:

 71
Output 2:

 110


Example Explanation

Explanation 1:

 Value([1]) = 1
 Value([1, 2]) = 3
 Value([1, 2, 3]) = 3
 Value([1, 2, 3, 4]) = 7
 Value([1, 2, 3, 4, 5]) = 7
 Value([2]) = 2
 Value([2, 3]) = 3
 Value([2, 3, 4]) = 7
 Value([2, 3, 4, 5]) = 7
 Value([3]) = 3
 Value([3, 4]) = 7
 Value([3, 4, 5]) = 7
 Value([4]) = 4
 Value([4, 5]) = 5
 Value([5]) = 5
 Sum of all these values = 71
Explanation 2:

 Sum of value of all subarray is 110.'''

from math import log2 as log

class Solution:
    # @param A : list of integers
    # @return an integer
    
    def check_zero(self, A):
        
        i, j = 0, 0
        sum_0, len_0 = 0, 0
        
        while j <= (len(A) - 1):
            
            if A[j] == 0:
                len_0 = (j - i + 1)
                j += 1
            
            else:
                if len_0 > 0:
                    sum_0 += int(len_0 * (len_0 + 1) / 2)
                    len_0 = 0
                
                j += 1
                i = j
        
        if len_0 > 0:
            sum_0 += int(len_0 * (len_0 + 1) / 2)
        
        return sum_0
        
    def solve(self, A):
        
        # Find maximum bit positions to iterate on
        
        max_bits = int(log(max(A))) + 1
        sum_orr = 0
        mod = int(1e9+7)
        
        for i in range(max_bits):
            
            bit_arr = []
            
            for num in A:
                
                # Iterate over all numbers and extract bit positions for all numbers
                
                bit_val = (num>>i)&1
                bit_arr.append(bit_val)
                
            # Find number of subarrays with atleast one 1s as this will contribute to the OR sum
            
            total = int((len(bit_arr) * (len(bit_arr) + 1)) / 2) 
            
            num_arr = total - self.check_zero(bit_arr)
                
            # Add the contribution at the ith bit
                
            # Left shift is equivalent to using 2**i
            contribution = ((1<<i) % mod * num_arr % mod) % mod 
                
            sum_orr = ((sum_orr % mod) + (contribution % mod)) % mod
            
            
        return sum_orr % mod