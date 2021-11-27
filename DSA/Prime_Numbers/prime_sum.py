'''Q1. Prime Sum
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an even number A ( greater than 2 ), return two prime numbers whose sum will be equal to given number.

If there are more than one solutions possible, return the lexicographically smaller solution.

If [a, b] is one solution with a <= b, and [c,d] is another solution with c <= d, then 
[a, b] < [c, d], If a < c OR a==c AND b < d. 
NOTE: A solution will always exist. Read Goldbach's conjecture.



Problem Constraints

4 <= A <= 2*107



Input Format

First and only argument of input is an even number A.



Output Format

Return a integer array of size 2 containing primes whose sum will be equal to given number.



Example Input

 4


Example Output

 [2, 2]


Example Explanation

 There is only 1 solution for A = 4.'''

class Solution:
	# @param A : integer
	# @return a list of integers
	def primesum(self, A):
	    
	    def isPrime(num):
	        i = 2
	        while (i*i) <= num:
	            if not num % i:
	                return False
	            i += 1
	        return True
	    
	    val = 2
	    while val <= A//2:
	        if isPrime(val) and isPrime(A-val):
	            return [val,A-val]
	        val += 1
	   
	    
	    
	    # Generate prime numbers 2-A with Sieve of Eratosthenes (AloglogA)
	   # sieve = ['1']*(A+1)
	    
    #     i = 2
    #     while (i*i <= A):
    #         for j in range(i*i,A+1,i):
    #           if sieve[j] == '1':
    #               sieve[j] = '0'
    #         i += 1
            
    #     val = 2
        
    #     while (val*val <= A):
    #         if sieve[val] == '1' and sieve[A-val] == '1':
    #           return [val,A-val]
    #         val += 1
    
    
            
	    
	    
	   # for i in range(2,A+1):
	   #     for j in range(i*i,A+1,i):
	   #         if sieve[j] == 1:
	   #             sieve[j] = 0
	    
	   # for k in range(2,A+1):
	   #     if sieve[k] == 1 and sieve[A-k] == 1:
	   #         return [k,A-k]
	   
	   