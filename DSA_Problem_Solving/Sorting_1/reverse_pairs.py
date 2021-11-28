'''Q3. Reverse pairs
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an array of integers A, we call (i, j) an important reverse pair if i < j and A[i] > 2*A[j].
Return the number of important reverse pairs in the given array A.



Problem Constraints

1 <= length of the array <= 105

-2 * 109 <= A[i] <= 2 * 109



Input Format

The only argument given is the integer array A.



Output Format

Return the number of important reverse pairs in the given array A.



Example Input

Input 1:

 A = [1, 3, 2, 3, 1]
Input 2:

 A = [4, 1, 2]


Example Output

Output 1:

 2
Output 2:

 1


Example Explanation

Explanation 1:

 There are two pairs which are important reverse i.e (3, 1) and (3, 1).
Explanation 2:

 There is only one pair i.e (4, 1).'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        counts = [0]
        self.merge_sort(A, 0, len(A) - 1, counts)
        return counts[0]
        
    def merge_sort(self, arr, i, j, i_counts):
        
        if i == j:
            return
        mid = (i + j) // 2
        
        self.merge_sort(arr, i, mid, i_counts)
        self.merge_sort(arr, mid+1, j, i_counts)
        
        i_counts[0] = i_counts[0] + self.merge(arr, i, j)
    
    def merge(self, arr, x, y):
        
        mid = (x + y) // 2
        
        # Counting logic
        i1, i2 = x, mid + 1
        imp = 0
#         print(arr[x:mid+1], arr[mid+1:y+1])
        while i1 <= mid and i2 <= y:
            
            if arr[i1] > (2 * arr[i2]):
                
                imp = imp + (mid - i1 + 1)
                i2 += 1
            else:
                i1 += 1
#         print(imp)
        
        # Merging logic
        
        temp = [0] * (y - x + 1)
        l,r,z = x, mid + 1, 0
        
        while l <= mid and r <= y:
            
            if arr[l] <= arr[r]:
                temp[z] = arr[l]
                l += 1
            else:
                temp[z] = arr[r]
                r += 1
            
            z += 1
        
        while l <= mid:
            temp[z] = arr[l]
            l += 1
            z += 1
        
        while r <= y:
            temp[z] = arr[r]
            r += 1
            z += 1
        
        for idx in range(x, y + 1):
            arr[idx] = temp[idx - x]
        
        return imp