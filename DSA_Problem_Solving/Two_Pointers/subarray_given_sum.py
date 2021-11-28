'''Q4. Subarray with given sum
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
        
        # # Prefix Array
        # ps = [0 for i in range(len(A)+1)]
        
        # for i in range(len(A)):
        #     ps[i+1] = ps[i] + A[i]
            
        # hm = {}
        
        # for j in range(len(ps)):
            
        #     if (ps[j] - B) in hm:
        #         return A[hm[ps[j] - B]:j]
            
        #     else:
        #         hm[ps[j]] = j
        
        # return [-1]
        
        # # TC O(N), SC O(N)
        
        i, j = 0, 0
        curr = 0
        
        while j < len(A):
            
            if curr < B:
                curr += A[j]
                j += 1
            
            elif curr > B:
                curr -= A[i]
                i += 1
            
            else:
                return A[i:j]

            # elif curr == B:
            #     return A[i:j]
        
        while i < len(A) and curr >= B:
            
            # Here j has reached the end ; thus the condition curr < B does not need to be checked as we have added all the elements with the j pointer ; only check for subarrays where sum >= B by moving the i pointer to the end
            
            if curr == B:
                return A[i:j] # O(N)
            
            elif curr > B:
                curr -= A[i]
                i += 1
                
        return [-1]
            
# TC O(N) 1st loop, O(N) 2nd loop and O(N) for returning .... O(3N) ~ O(N) ; space O(1) as not using any extra data structure apart from array asked to return