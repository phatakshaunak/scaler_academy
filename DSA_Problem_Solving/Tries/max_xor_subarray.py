'''Q4. Maximum XOR Subarray
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an array A of integers of size N. Find the subarray AL, AL+1, AL+2, … AR with 1<=L<=R<=N which has maximum XOR value.

NOTE: If there are multiple subarrays with same maximum value, return the subarray with minimum length. If length is same, return the subarray with minimum starting index.



Problem Constraints

1 <= N <= 100000
0 <= A[i] <= 109



Input Format

First and only argument is an integer array A.



Output Format

Return an integer array B of size 2. B[0] is the starting index(1-based) of the subarray and B[1] is the ending index(1-based) of the subarray.



Example Input

Input 1:

 A = [1, 4, 3]
Input 2:

 A = [8]


Example Output

Output 1:

 [2, 3]
Output 2:

 [1, 1]


Example Explanation

Explanation 1:

 There are 6 possible subarrays of A:
 subarray            XOR value
 [1]                     1
 [4]                     4
 [3]                     3
 [1, 4]                  5 (1^4)
 [4, 3]                  7 (4^3)
 [1, 4, 3]               6 (1^4^3)

 [4, 3] subarray has maximum XOR value. So, return [2, 3].
Explanation 2:

 There is only one element in the array. So, the maximum XOR value is equal to 8 and the only possible subarray is [1, 1].'''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

        N = len(A)
        # Create a prefix xor array
        ps = [0] * (N + 1)

        for i in range(N):
            ps[i + 1] = ps[i] ^ A[i]
        
        # Initialize a trie node
        t = trie()

        # Get a dummy node
        root = t.get_node(-1)

        # Insert 0 from prefix array into trie
        t.insert(root, ps[0], 0)

        # Iterate over remaining elements in the prefix array to find a maximum value
        max_val = 0

        st, e = -1, -1
        
        for i in range(1, N + 1):
            # Find max xor
            curr, end = t.find_xor(root, ps[i])

            # Update answer and add conditions for equality
            if curr > max_val:
                max_val = curr
                st, e = end, i
            
            if curr == max_val:
                if (e - st) > (i - end):
                    st, e = end, i
                
                elif (e - st) == (i - end):
                    if end < st:
                        st, e = end, i
            
            # Insert ps[i]
            t.insert(root, ps[i], i)
        
        return [st+1, e]

class trie:

    def get_node(self, bit_val):
        return trieNode(bit_val)
    
    def insert(self, root, num, idx):
        dummy = root
        
        for i in range(31, -1, -1):
            
            bit = 1 if (num & (1 << i)) else 0
            
            if bit not in dummy.children:
                dummy.children[bit] = self.get_node(bit)
            
            dummy = dummy.children[bit]

        dummy.index = idx
    
    def find_xor(self, root, num):
        ans, dummy = 0, root

        for i in range(31, -1, -1):
            
            bit = 1 if (num & (1 << i)) else 0
            cbit = bit ^ 1

            if cbit in dummy.children:
                ans = ans + (1 << i)
                dummy = dummy.children[cbit]
            else:
                dummy = dummy.children[bit]

        return ans, dummy.index

class trieNode:
    def __init__(self, bit):
        self.bit = bit
        self.children = {}
        self.index = None