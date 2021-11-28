'''Q2. Rearrange Array
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Rearrange a given array so that Arr[i] becomes Arr[Arr[i]] with O(1) extra space.

Example:

Input : [1, 0]
Return : [0, 1]
Lets say N = size of the array. Then, following holds true :

All elements in the array are in the range [0, N-1]
N * N does not overflow for a signed integer'''

class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference. 
    # You do not need to return anything in this case. 
    def arrange(self, A):
        
        N = len(A)
        
        for i in range(N):
            
            A[i] = A[i] + (A[A[i]]%N)*N
        
        for i in range(N):
            A[i] = A[i] // N
        
        return A

'''
We need to replace A[i] with A[A[i]]. 
Consider two numbers, a and b. 
a is the original number and b is the new number. 
both a,b < N (length of array)
If we change a as (a + b*n). This number can be updated to get both a and b back. 
To get b, do (a+b*n) // n as a//n = 0 (a<n) and (b*n//n) = b. 
To get a, do (a+b*n) % n, as (b*n) % n = 0 and a < n, thus a % n = a

The operation A[A[i]]%N ensures to only extract the original b value that we want to replace the a value with as we are dynamically changing all array values and may not have the original b values in place as simply doing A[A[i]] may lead to A[i]>N.

This approach takes advantage of the fact that all numbers in the array are between 0 and N. The important insight is that we are storing a number at an index such that we can obtain both the old and new numbers at that index by mathematical operations like // and %
'''