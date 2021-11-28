'''Q1. Permutations of A in B
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

You are given two strings A and B of size N and M respectively.

You have to find the count of all permutations of A present in B as a substring. You can assume a string will have only lowercase letters.



Problem Constraints

1 <= N < M <= 105



Input Format

Given two argument, A and B of type String.



Output Format

Return a single Integer, i.e number of permutations of A present in B as a substring.



Example Input

Input 1:

 A = "abc"
 B = "abcbacabc"
Input 2:

 A = "aca"
 B = "acaa"


Example Output

Output 1:

 5
Output 2:

 2


Example Explanation

Explanation 1:

 Permutations of A that are present in B as substring are:
    1. abc
    2. cba
    3. bac
    4. cab
    5. abc
    So ans is 5.
Explanation 2:

 Permutations of A that are present in B as substring are:
    1. aca
    2. caa '''

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        
        # Optimized approach with a sliding window without comparing hash maps

        # Generate a frequency map for chars in A
        hm = {}
        m, n = len(B), len(A)
        need, ans = 0, 0
        for val in A:
            if val not in hm:
                hm[val] = 1
            else:
                hm[val] += 1
            need += 1

        # Evaluate first window of size len(A) to see if it is a permutation

        for i in range(n):
            # Check if B[i] in hash map
            if B[i] in hm:
                #Check if it's frequency is > 0, then decrement need as 1 less element is needed to match characters in A
                if hm[B[i]] > 0:
                    need -= 1
                # Decrement A[i]'s frequency
                hm[B[i]] -= 1
        
        #After processing first window, check if need = 0, i.e. a valid permutation is found
        if need == 0:
            ans += 1
        
        # Iterate through the remaining array and repeat the above process
        for j in range(n, m):
            
            # No need to update if incoming and outgoing characters are the same
            if B[j - n] != B[j]:
                # Remove (j-n)th element, add to frequency if present in map, increment need if frequency is >= zero, if negative don't change need
                if B[j - n] in hm:
                    if hm[B[j - n]] >= 0:
                        need += 1
                    hm[B[j - n]] += 1
                
                # Add jth element if present
                if B[j] in hm:
                    # Decrement need if it's frequency is > 0
                    if hm[B[j]] > 0:
                        need -= 1
                    hm[B[j]] -= 1
                
            #Check if need zero for current window and increment ans if true
            if need == 0:
                ans += 1
        
        return ans
        '''
        Two hash maps and compare both for each window.
        Create frequency map of A and that of B for length(A). Then slide across B reducing/removing left element and comparing to A
        '''

        # hm_a, hm_b, ans = {}, {}, 0

        # for val in A:
        #     if val not in hm_a:
        #         hm_a[val] = 1
        #     else:
        #         hm_a[val] += 1
        
        # n, m = len(A), len(B)

        # for i in range(n):
        #     if B[i] not in hm_b:
        #         hm_b[B[i]] = 1
        #     else:
        #         hm_b[B[i]] += 1
        
        # if hm_a == hm_b:
        #     ans += 1
        
        # for j in range(n,m,1):

        #     if hm_b[B[j - n]] > 1:
        #        hm_b[B[j - n]] -= 1

        #     else:
        #         del hm_b[B[j - n]]

        #     if B[j] not in hm_b:
        #         hm_b[B[j]] = 1
        #     else:
        #         hm_b[B[j]] += 1
            
        #     if hm_a == hm_b:
        #         ans += 1
        
        # return ans

'''Q2. Valid Sudoku
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Determine if a Sudoku is valid, according to: http://sudoku.com.au/TheRules.aspx

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.



The input corresponding to the above configuration :

["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
A partially filled sudoku which is valid.

Note:

A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
Return 0 / 1 ( 0 for false, 1 for true ) for this problem

See Expected Output'''

class Solution:
	# @param A : tuple of strings
	# @return an integer
	def isValidSudoku(self, A):
	    
	    N = len(A)
	    
	    row = [set() for i in range(N)]
	    col = [set() for i in range(N)]
	    cube = [set() for i in range(N)]
	    
	    for i in range(N):
	        for j in range(N):
	            
	            if A[i][j] != '.' and A[i][j] in row[i]:
	                return 0
	            row[i].add(A[i][j])
	            
	            if A[i][j] != '.' and A[i][j] in col[j]:
	                return 0
	            col[j].add(A[i][j])
	            
	            grid_c = ((i//3)*3) + (j//3)
	            
	            if A[i][j] != '.' and A[i][j] in cube[grid_c]:
	                return 0
	            cube[grid_c].add(A[i][j])
	   
	    return 1
	            
    # 	hash_1, hash_2, hash_3 = {}, {}, {}
    	
    # 	N = len(A)
    # 	# Consider row and column violations:
    # 	for i in range(N):
    # 	    for j in range(N):
    	        
    # 	        if A[i][j] != '.':
    # 	            if A[i][j] not in hash_1:
    # 	                hash_1[A[i][j]] = 1
    	                
    # 	            elif A[i][j] in hash_1:
    # 	                return 0
    	        
    # 	        if A[j][i] != '.':
    # 	            if A[j][i] not in hash_2:
    # 	                hash_2[A[j][i]] = 1
    	                
    # 	            elif A[j][i] in hash_2:
    # 	                return 0
    	       
    # 	    hash_1.clear()
    # 	    hash_2.clear()
    	  
    # 	# Consider each 3X3 grid for any violations
    	
    # 	counter_row = 3
    # 	counter_col = 9
    	
    # 	for i in range(N):
    	    
    # 	    counter_row -= 1
    	    
    # 	    if counter_row < 0:
    # 	        hash_1.clear()
    # 	        hash_2.clear()
    # 	        hash_3.clear()
    # 	        counter = 2
    	        
    # 	    if counter_col == 0:
    # 	        counter_col = 9
    	        
    # 	    for j in range(N):
    	        
    # 	        counter_col -= 1
    	        
    # 	        if counter_col >= 6:
    	            
    # 	            if A[i][j] != '.':
    # 	                if A[i][j] not in hash_1:
    # 	                    hash_1[A[i][j]] = 1
    	                   
    # 	                elif A[i][j] in hash_1:
    # 	                    return 0
    	       
    # 	        elif counter_col >= 3 and counter_col < 6:
    	            
    # 	            if A[i][j] != '.':
    # 	                if A[i][j] not in hash_2:
    # 	                    hash_2[A[i][j]] = 1
    	                   
    # 	                elif A[i][j] in hash_2:
    # 	                    return 0
    	       
    # 	        else:
    	            
    # 	            if A[i][j] != '.':
    # 	                if A[i][j] not in hash_3:
    # 	                    hash_3[A[i][j]] = 1
    	                   
    # 	                elif A[i][j] in hash_3:
    # 	                    return 0
    	       
    #     return 1