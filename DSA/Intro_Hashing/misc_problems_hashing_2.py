'''Q1. Subarray with given sum
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an array of positive integers A and an integer B, find and return first continuous subarray which adds to B.

If the answer does not exist return an array with a single element "-1".

First sub-array means the sub-array for which starting index in minimum.



Problem Constraints

1 <= length of the array <= 100000
1 <= A[i] <= 109
1 <= B <= 109



Input Format

The first argument given is the integer array A.

The second argument given is integer B.



Output Format

Return the first continuous sub-array which adds to B and if the answer does not exist return an array with a single element "-1".



Example Input

Input 1:

 A = [1, 2, 3, 4, 5]
 B = 5
Input 2:

 A = [5, 10, 20, 100, 105]
 B = 110


Example Output

Output 1:

 [2, 3]
Output 2:

 -1


Example Explanation

Explanation 1:

 [2, 3] sums up to 5.
Explanation 2:

 No subarray sums up to required number.'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        
        #         # '''Sliding Window will not work with negative numbers in the array. 
        #         # This approach assumes positive integers. time O(n) space O(1) as no hash map/prefix sum array is used'''
        
        # i, j = 0, 0
        # current_sum = A[0]
        # count = 0
        
        # subarrays = []
        
        # while j < len(A):
            
        #     if current_sum < B:
        #         j += 1
                
        #         if j < len(A):
        #             current_sum = current_sum + A[j]
            
        #     elif current_sum == B:
                
        #         count += 1
                
        #         if i == j:
                    
        #             subarrays.append([A[i]])
        #             current_sum = current_sum - A[j]
        #             j += 1
        #             if j < len(A):
        #                 current_sum = current_sum + A[j]
                
        #         else:
        #             subarrays.append(A[i:j+1])
        #             current_sum = current_sum - A[i] - A[j]
        #             i += 1
        #             j += 1
        #             current_sum = current_sum + A[i] + A[j]
            
        #     else:
        #         while current_sum > B:
                    
        #             current_sum = current_sum - A[i]
                    
        #             i += 1
        # if subarrays == []:
        #     return [-1]
        
        # return subarrays, count
            
                    

# #Initially compute a prefix sum array
        
        ps_a = [0] * (len(A)+1)
        
        for i in range(len(A)):
            ps_a[i+1] = ps_a[i] + A[i]
            
        hash_map = {}
        
        N = len(ps_a)
        
        for i in range(N):
            
            if (ps_a[i] - B) in hash_map:
                
                hash_map[ps_a[i]] = i
                
                left = hash_map[ps_a[i]-B]
                right = (i-1)
                return A[left:right+1]
                    
                # if hash_map[ps_a[i]-B] == i-1:
                #     return [A[i-1]]
                
                # else:
                #     left = hash_map[ps_a[i]-B]
                #     right = (i-1)
                #     return A[left:right+1]
            
            else:
                hash_map[ps_a[i]] = i
        
        return [-1]
    
################################################################################################################################################################################################################################################################
                    
'''Q2. Sub-array with 0 sum
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an array of integers A, find and return whether the given array contains a non-empty subarray with a sum equal to 0.

If the given array contains a sub-array with sum zero return 1 else return 0.



Problem Constraints

1 <= |A| <= 100000

-10^9 <= A[i] <= 10^9



Input Format

The only argument given is the integer array A.



Output Format

Return whether the given array contains a subarray with a sum equal to 0.



Example Input

Input 1:

 A = [1, 2, 3, 4, 5]
Input 2:

 A = [-1, 1]


Example Output

Output 1:

 0
Output 2:

 1


Example Explanation

Explanation 1:

 No subarray has sum 0.
Explanation 2:

 The array has sum 0.'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        
        
        # Compute prefix sum array (Use 0 as the first element for convenience)
        ps_a = [0] * (len(A)+1)
        # ps_a[0] = 0
        k = 0
        for i in range(len(A)):
            ps_a[i+1] = ps_a[i] + A[i]
            
        '''The goal is to find a sub array that sums to zero. In terms of prefix sum, we want to find pairs L and R where P[R] - P[L-1] = 0 ; i.e. We need to just find pairs A, B where A-B = k ; This is similar to the 2-sum approach where we store elements in a
           a hash map and iterate to check if (A-k) is present in the hash map. The value present in the hash map signifies the number at the L-1th index in the prefix sum array, while the current number in the iteration corresponds to the Rth index. When we find 
           such a match, that means that the original array contains such a sub array summing to 0 or some k'''
           
        hash_map = {}
        
        for i in ps_a:
            
            if (i-k) in hash_map:
                
                if i in hash_map:
                    hash_map[i] += 1
                
                else:
                    hash_map[i] = 1
                return 1
            else:
                hash_map[i] = 1
        
        return 0

'''Q3. Equal
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an array A of N integers, find the index of values that satisfy P + Q = R + S, where P,Q,R & S are integers values in the array

Expected time complexity O(N2)

NOTE:

1) Return the indices `A1 B1 C1 D1`, so that 
  A[A1] + A[B1] = A[C1] + A[D1]
  A1 < B1, C1 < D1
  A1 < C1, B1 != D1, B1 != C1 

2) If there are more than one solutions, 
   then return the tuple of values which are lexicographical smallest. 

Assume we have two solutions
S1 : A1 B1 C1 D1 ( these are values of indices in the array )  
S2 : A2 B2 C2 D2

S1 is lexicographically smaller than S2 if:
  A1 < A2 OR
  A1 = A2 AND B1 < B2 OR
  A1 = A2 AND B1 = B2 AND C1 < C2 OR 
  A1 = A2 AND B1 = B2 AND C1 = C2 AND D1 < D2
If no solution is possible, return an empty list.



Problem Constraints

1 <= N <= 1000

0 <= A[i] <= 1000



Input Format

Single argument which is an integer array A of size N.



Output Format

Return an array of size 4 which indexes of values P,Q,R and S.



Example Input

Input 1:

 A = [3, 4, 7, 1, 2, 9, 8]
Input 2:

 A = [2, 5, 1, 6]


Example Output

Output 1:

 [0, 2, 3, 5]
Output 2:

 [0, 1, 2, 3]


Example Explanation

Explanation 1:

 A[0] + A[2] = A[3] + A[5]
 Note: indexes returned should be 0-based.
Explanation 2:

 A[0] + A[1] = A[2] + A[3]'''

class Solution:
	# @param A : list of integers
	# @return a list of integers
	def equal(self, A):
	    
	    hash_map = {}
	    answer = [2000,2000,2000,2000]
	    
	    for i in range(len(A)):
	        
	        for j in range(i+1, len(A)):
	            
	            sum1 = A[i] + A[j]
	            
	            if sum1 not in hash_map:
	                hash_map[sum1] = [i,j]
	            
	            else:
	                
	               # if hash_map[sum1][0] != i and hash_map[sum1][0] != j and hash_map[sum1][1] != i and hash_map[sum1][1] != j:
	               
	               if hash_map[sum1][0] < i and hash_map[sum1][1] != i and hash_map[sum1][1] != j:
	                    current_answer = hash_map[sum1].copy()
	                    current_answer.append(i)
	                    current_answer.append(j)
	                    
	                    for k in range(4):
	                        
	                        if current_answer[k] < answer[k]:
	                            answer = current_answer
	                            break
	                        
	                        if current_answer[k] > answer[k]:
	                            break
	                   
	    if answer == [2000,2000,2000,2000]:
	        return []
	    else:   
	        return answer