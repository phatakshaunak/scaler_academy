'''Q3. Inversion count in an array
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description
Given an array of integers A. If i < j and A[i] > A[j] then the pair (i, j) is called an inversion of A. Find the total number of inversions of A modulo (109 + 7).



Problem Constraints
1 <= length of the array <= 100000

1 <= A[i] <= 10^9



Input Format
The only argument given is the integer array A.



Output Format
Return the number of inversions of A modulo (109 + 7).



Example Input
Input 1:

A = [3, 2, 1]
Input 2:

A = [1, 2, 3]


Example Output
Output 1:

3
Output 2:

0


Example Explanation
Explanation 1:

 All pairs are inversions.
Explanation 2:

 No inversions.'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)
        # mod = int(1e9+7)
        if len(A) == 1 or A == None:
            return 0
        return self.merge_sort(A,0,N-1,[0])[0]
        
    def merge_sort(self,A,i,j,inv):
        
        if i == j:
            return
        
        mid = (i + j) // 2
        self.merge_sort(A, i,mid,inv)
        self.merge_sort(A, mid+1,j,inv)
        inv = self.merge(A,i,j,inv)
        
        return inv
    
    def merge(self,arr,i,j,inv):
        
        temp = [0] * (j-i+1)
        
        mid = (i + j) // 2
        
        x,y,z = i, mid+1, 0
        
        while x <= mid and y <= j:
            
            if arr[x] <= arr[y]:
                temp[z] = arr[x]
                x += 1
            
            else:
                temp[z] = arr[y]
                y += 1
                inv[0] = (inv[0] % int(1e9+7) + (mid - x + 1) % int(1e9+7)) % int(1e9+7)
                # inv[0] = inv[0] + (mid - x + 1)
            
            z += 1
        
        while x <= mid:
            temp[z] = arr[x]
            x += 1
            z += 1
        
        while y <= j:
            temp[z] = arr[y]
            y += 1
            z += 1
        
        for idx in range(i,j+1):
            arr[idx] = temp[idx - i]
        
        return inv
            
            # 3 4 5
            # 0 1 2
