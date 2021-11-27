'''Q3. Palindrome Integer
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Determine whether an integer is a palindrome. Do this without extra space.

A palindrome integer is an integer x for which reverse(x) = x where reverse(x) is x with its digit reversed. Negative numbers are not palindromic.

Example :

Input : 12121
Output : True

Input : 123
Output : False'''

class Solution:
	# @param A : integer
	# @return an integer
	def isPalindrome(self, A):
	    
	    B = A + 0
	    
	    # Edge case:
	    if A < 0:
	        return 0
	    
	    if (A%10 == A):
	        return 1
	    
	   # # Find maximum power of 10 in A
	    
	   # i = 1
	    
	   # while A % (10**i) < A:
	   #     if A % (10**i) < A:
	   #         i += 1
	   # max_10 = i-1
	    
	   # pal = 0
	    
	   # #Reconstruct number by calculating in reverse.
	    
	   # while A > 0:
	   #     pal += (A%10) * (10**max_10)
	   #     A //= 10
	   #     max_10 -= 1
	    
	   # if pal == B:
	   #     return 1
	  
	    pal = 0
        while A > 0: 
       	    pal = (pal*10) + (A%10)
       	    A //= 10
       	
	    if pal == B:
	        return 1
	    return 0