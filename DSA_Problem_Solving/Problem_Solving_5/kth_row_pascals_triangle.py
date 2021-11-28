'''Q3. Kth Row of Pascal's Triangle
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an index k, return the kth row of the Pascal's triangle.
Pascal's triangle: To generate A[C] in row R, sum up A'[C] and A'[C-1] from previous row R - 1.

Example:

Input : k = 3

Return : [1,3,3,1]
Note: k is 0 based. k = 0, corresponds to the row [1].

Note: Could you optimize your algorithm to use only O(k) extra space?'''

class Solution:
    # @param A : integer
    # @return a list of integers
    
    def comb(self, a, b):

        if b == 0 or a == b:
            return 1

        else:
            num = a
            den = 1
            ans = 1
            for i in range(b):
                
                ans = (ans * num) / den
                
                num -= 1
                den += 1

        return int(ans)
    
    def getRow(self, A):
        
        ans = []
        
        for i in range(A+1):
            
            ans.append(self.comb(A,i))
        
        return ans

#Time O(k^2), Space O(k)