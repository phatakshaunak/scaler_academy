'''Q1. 2 Sum
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 < index2. Please note that your returned answers (both index1 and index2 ) are not zero-based. Put both these numbers in order in an array and return the array from your function ( Looking at the function signature will make things clearer ). Note that, if no pair exists, return empty list.

If multiple solutions exist, output the one where index2 is minimum. If there are multiple solutions with the minimum index2, choose the one with minimum index1 out of them.

Input: [2, 7, 11, 15], target=9
Output: index1 = 1, index2 = 2'''

class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return a list of integers
	def twoSum(self, A, B):
	    hash_map = {}
	    
	    for i in range(len(A)):
	        
	        # Second condition in the if statement is to avoid using duplicates present in the given array
	        
	        if (B - A[i] not in hash_map) and (A[i] not in hash_map):
	            hash_map[A[i]] = i
	        
	        elif (B - A[i]) in hash_map:
	            
	            index_1 = hash_map[(B - A[i])] + 1
	            index_2 = i + 1
	            
	            return[index_1, index_2]
	       
	       #if A[i] in hash_map:
	       #    return [hash_map[A[i]]+1,i+1]
	           
	       #if B - A[i] not in hash_map:
	       #    hash_map[B-A[i]] = i
	   
	    return []    

'''Q2. Common Elements
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given two integer array A and B of size N and M respectively. Your task is to find all the common elements in both the array.

NOTE:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.


Problem Constraints

1 <= N, M <= 105

1 <= A[i] <= 109



Input Format

First argument is an integer array A of size N.

Second argument is an integer array B of size M.



Output Format

Return an integer array denoting the common elements.



Example Input

Input 1:

 A = [1, 2, 2, 1]
 B = [2, 3, 1, 2]
Input 2:

 A = [2, 1, 4, 10]
 B = [3, 6, 2, 10, 10]


Example Output

Output 1:

 [1, 2, 2]
Output 2:

 [2, 10]


Example Explanation

Explanation 1:

 Elements (1, 2, 2) appears in both the array. Note 2 appears twice in both the array.
Explantion 2:

 Elements (2, 10) appears in both the array.'''

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        
        if len(A) > len(B):
            return self.solve(B, A)
        
        hash = {}
        common = []
        
        for i in A:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1
                
        for j in B:
            if j in hash and hash[j] > 0:
                common.append(j)
                hash[j] -= 1
        
        return common

'''Q3. Pairs With Given Xor
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an 1D integer array A containing N distinct integers.

Find the number of unique pairs of integers in the array whose XOR is equal to B.

NOTE:

Pair (a, b) and (b, a) is considered to be same and should be counted once.


Problem Constraints

1 <= N <= 105

1 <= A[i], B <= 107



Input Format

First argument is an 1D integer array A.

Second argument is an integer B.



Output Format

Return a single integer denoting the number of unique pairs of integers in the array A whose XOR is equal to B.



Example Input

Input 1:

 A = [5, 4, 10, 15, 7, 6]
 B = 5
Input 2:

 A = [3, 6, 8, 10, 15, 50]
 B = 5


Example Output

Output 1:

 1
Output 2:

 2


Example Explanation

Explanation 1:

 (10 ^ 15) = 5
Explanation 2:

 (3 ^ 6) = 5 and (10 ^ 15) = 5'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        dict_A = {}
        count = 0
        for i in A:
            
            if B^i not in dict_A:
                dict_A[i] = 1
                
            # elif B^i in dict_A:
            else:
                count += 1
        
        return count

