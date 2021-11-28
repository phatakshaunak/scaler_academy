'''Q4. Next Permutation
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Implement the next permutation, which rearranges numbers into the numerically next greater permutation of numbers for a given array A of size N.

If such arrangement is not possible, it must be rearranged as the lowest possible order i.e., sorted in an ascending order.

NOTE:

The replacement must be in-place, do not allocate extra memory.
DO NOT USE LIBRARY FUNCTION FOR NEXT PERMUTATION. Use of Library functions will disqualify your submission retroactively and will give you penalty points.


Problem Constraints

1 <= N <= 5 * 105

1 <= A[i] <= 109



Input Format

The first and the only argument of input has an array of integers, A.



Output Format

Return an array of integers, representing the next permutation of the given array.



Example Input

Input 1:

 A = [1, 2, 3]
Input 2:

 A = [3, 2, 1]


Example Output

Output 1:

 [1, 3, 2]
Output 2:

 [1, 2, 3]


Example Explanation

Explanation 1:

 Next permutaion of [1, 2, 3] will be [1, 3, 2].
Explanation 2:

 No arrangement is possible such that the number are arranged into the numerically next greater permutation of numbers.
 So will rearranges it in the lowest possible order.'''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextPermutation(self, A):
        
        i = len(A)-1
        j = i - 1
        low = -1
        while i > 0:
            
            if A[i] > A[j]:
                low = j
                break
            i -= 1
            j -= 1
        
        def rev(arr,l,r):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
            
        if i == 0:
            rev(A,0,len(A)-1)
            return A
        
        for k in range(len(A)-1,low,-1):
            if A[k] > A[low]:
                s_ind = k
                break
        
        # min_g = float("inf")
        
        # for k in range(low+1, len(A)):
        #     if A[k] > A[low]:
        #         if A[k] < min_g:
        #             min_g = A[k]
        #             s_ind = k
        
        A[low], A[s_ind] = A[s_ind], A[low]
        
        rev(A,low+1,len(A)-1)
        
        return A
        
        #TC O(N), SC O(1)
        
        # i_swap, j_swap = -1, -1
        
        # for i in range(len(A)-1,0,-1):
            
        #     j = i - 1
        #     while j >= 0:
        #         if A[i] > A[j]:
                    
        #             #Need to swap only on the right most position to get the next permutation.
        #             if j > j_swap:
        #                 j_swap = j
        #                 i_swap = i
                        
        #             # j_swap = max(j_swap, j)
        #             # i_swap = i
        #             # A[i], A[j] = A[j], A[i]
        #             # A[j+1:] = sorted(A[j+1:])
        #             # return A
                    
        #         j -= 1
        
        # if i_swap == -1 and j_swap == -1:
        #     A.sort()
        #     return A
            
        # A[i_swap], A[j_swap] = A[j_swap], A[i_swap]
        
        # def rev(arr,l,r):
        #     while l < r:
        #         arr[l], arr[r] = arr[r], arr[l]
        #     l += 1
        #     r -= 1
        
        # rev(A,j_swap+1,len(A)-1)
        
        # # A[j_swap+1:] = sorted(A[j_swap+1:])
        
        # return A
'''
23710
27310
27013

find smaller digit on the left and swap with that digit. Then sort all digits after the left most swapped digits.
if a smaller digit is not found, return smallest ascending order permutation

68881 
swap 8 and 9 ; 69831 ; sort(831) ; 69138
'''
# TC O(N^2), SC O(1)