'''Q3. Majority Element
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an array of size n, find the majority element. The majority element is the element that appears more than floor(n/2) times.
You may assume that the array is non-empty and the majority element always exist in the array.

Example :

Input : [2, 1, 2]
Return  : 2 which occurs 2 times which is greater than 3/2.'''

class Solution:
	# @param A : tuple of integers
	# @return an integer
	def majorityElement(self, A):
	    
	    # Apart from a brute force approach using frequency hash map which will take extra space, we can implement Moore's Voting Algorithm which runs in O(N) time but O(1) space

        # Initialize variables to track majority element and a counter

        maj, counter = 0, 0
        N = len(A)
        '''
        Traverse the array. If the counter is zero, increment and update the majority variable
        If majority is element == A[i], incremenet counter, else decrement counter
        
        If a majority element does not exist, we need to traverse again to check if the last majority element's count
        in the first loop is N/2+1. If not, we do not have any majority
        Moore's Voting Algorithm
        '''
	    for i in range(len(A)):
            
            if counter == 0:
                counter += 1
                maj = A[i]
            
            elif A[i] == maj:
                counter += 1
            
            elif A[i] != maj:
                counter -= 1
        
        maj_count = 0
        for i in range(len(A)):
            
            if A[i] == maj:
                maj_count += 1
        
        if maj_count >= ((N//2)+1):
            return maj
        
        else:
            return -1
	    
	   # hash_map = {}
	    
	   # for i in range(len(A)):
	        
	   #     if A[i] not in hash_map:
	   #         hash_map[A[i]] = 1
	        
	   #     else:
	   #         hash_map[A[i]] += 1
	    
	   # for i in hash_map:
	        
	   #     if hash_map[i] >= (len(A)//2) + 1:
	   #         return i

# O(N) time, O(N) space brute force solution
