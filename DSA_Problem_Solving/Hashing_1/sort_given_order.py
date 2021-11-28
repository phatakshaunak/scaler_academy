'''Q3. Sort Array in given Order
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given two array of integers A and B, Sort A in such a way that the relative order among the elements will be the same as those are in B. For the elements not present in B, append them at last in sorted order.

Return the array A after sorting from the above method.

NOTE: Elements of B are unique.



Problem Constraints

1 <= length of the array A <= 100000

1 <= length of the array B <= 100000

-10^9 <= A[i] <= 10^9



Input Format

The first argument given is the integer array A.

The second argument given is the integer array B.



Output Format

Return the array A after sorting as described.



Example Input

Input 1:

A = [1, 2, 3, 4, 5]
B = [5, 4, 2]
Input 2:

A = [5, 17, 100, 11]
B = [1, 100]


Example Output

Output 1:

[5, 4, 2, 1, 3]
Output 2:

[100, 5, 11, 17]


Example Explanation

Explanation 1:

 Simply sort as described.
Explanation 2:

 Simply sort as described.'''

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        '''
        Frequency map of A
        Fill A with values from B
        Fill temp array with values remaining in A from map
        Append temp to A and return
        '''
        hm = {}
        
        m, n = len(A), len(B)
        
        for val in A:
            if val not in hm:
                hm[val] = 1
            else:
                hm[val] += 1
        
        # Above takes O(m) time
        
        idx = 0
        
        for val in B:
            
            if val in hm:
                while hm[val] > 0:
                    A[idx] = val
                    hm[val] -= 1
                    idx += 1
        # Above takes O(n) time
        
        temp = []
        
        for v in hm:
            for i in range(hm[v]):
                temp.append(v)
        
        # Above takes O(rem) time (rem being the remaining elements in A)
        
        temp.sort()
        
        # Above takes O(rem log rem) time
        
        for j in range(idx, m):
            A[j] = temp[j - idx]
        
        # Above takes O(rem) time
        
        return A

#Overall O(m) + O(n) + O(rem) + O(rem log rem) + O(rem) ~ O(m+n) + O(rem log rem) ; at worst it will be O(m log m) TC and SC O(M)
        