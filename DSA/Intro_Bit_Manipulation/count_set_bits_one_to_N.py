'''Q2. Count Total Set Bits
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given a positive integer A, the task is to count the total number of set bits in the binary representation of all the numbers from 1 to A.

Return the count modulo 109 + 7.



Problem Constraints

1 <= A <= 109



Input Format

First and only argument is an integer A.



Output Format

Return an integer denoting the ( Total number of set bits in the binary representation of all the numbers from 1 to A )modulo 109 + 7.



Example Input

Input 1:

 A = 3
Input 2:

 A = 1


Example Output

Output 1:

 4
Output 2:

 1


Example Explanation

Explanation 1:

 DECIMAL    BINARY  SET BIT COUNT
    1          01        1
    2          10        1
    3          11        2
 1 + 1 + 2 = 4 
 Answer = 4 % 1000000007 = 4
Explanation 2:

 A = 1
  DECIMAL    BINARY  SET BIT COUNT
    1          01        1
 Answer = 1 % 1000000007 = 1'''

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        
        #Time complexity: O(NlogN), Space complexity: O(1)
        mod = int(1e9 + 7)
        # def find_bits(num):
            
        #     bits = 0
            
        #     while num > 0:
        #         bits += num % 2
        #         num = num >> 1
            
        #     return bits
        
        # count = 0
        
        # for i in range(1,A+1):
            
        #     count = (count % mod + (find_bits(i)) % mod ) % mod
        
        # return count
        
        # Time complexity: O(N), Space Complexity: O(N)
        '''hm = {0:0, 1: 1}
        ans = 1
        
        for num in range(2, A+1):
            
            hm[num] = hm[num//2] + (num % 2)
            ans = ((ans % mod) + (hm[num] % mod)) % mod
        
        return ans'''
        # Optimized # 2
        
        def closest_2(num):
            
            ans = 0
            
            while num > 0:
                num = num >> 1
                ans += 1
            
            return (ans - 1)
        
        if A == 0 or A == 1:
            return A
        
        bits = 0
        x = closest_2(A)
        bits = bits + (x * 2**(x-1))
        
        rem = A - (2**x - 1)
        
        bits = bits + rem
        
        bits = bits + self.solve(rem-1)
        
        return bits % mod