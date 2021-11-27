'''Q1. Add Binary Strings
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given two binary strings, return their sum (also a binary string).
Example:

a = "100"

b = "11"
Return a + b = "111".'''

class Solution:
	# @param A : string
	# @param B : string
	# @return a strings
	def addBinary(self, A, B):
	    
	    ans = ''
	    carry = 0
	    
	    i, j = len(A) - 1, len(B) - 1
	    
	    while (i >= 0) and (j >= 0):
	        
	        val = int(A[i]) + int(B[j]) + carry
	        
	        ans = str(val % 2) + ans
	        carry = val // 2
	        
	        i -= 1
	        j -= 1
	    
	    while i >= 0:
	        
	        val = int(A[i]) + carry
	        
	        ans = str(val % 2) + ans
	        carry = val // 2
	        
	        i -= 1
	   
	    while j >= 0:
	        
	        val = int(B[j]) + carry
	        
	        ans = str(val % 2) + ans
	        carry = val // 2
	        
	        j -= 1
	    
	    
	    if carry == 1:
	        ans = '1' + ans
	        
	    return ans
	    
	    '''
	    7: 111
	    7: 111
	       1010
	    11: 1011
	    
	    
	    '''
	    
