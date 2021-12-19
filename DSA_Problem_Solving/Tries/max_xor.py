'''Q3. Maximum XOR
Solved
character backgroundcharacter
Stuck somewhere?
Ask for help from a TA & get it resolved
Get help from TA
Problem Description

Given an array of integers A, find and return the maximum result of A[i] XOR A[j], where i, j are the indexes of the array.



Problem Constraints

1 <= length of the array <= 100000
0 <= A[i] <= 109



Input Format

The only argument given is the integer array A.



Output Format

Return an integer denoting the maximum result of A[i] XOR A[j].



Example Input

Input 1:

 A = [1, 2, 3, 4, 5]
Input 2:

 A = [5, 17, 100, 11]


Example Output

Output 1:

 7
Output 2:

 117


Example Explanation

Explanation 1:

 Maximum XOR occurs between element of indicies(0-based) 1 and 4 i.e. 2 ^ 5 = 7.
Explanation 2:

 Maximum XOR occurs between element of indicies(0-based) 1 and 2 i.e. 17 ^ 100 = 117.'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        root = trieNode(-1)
        
        # Initialize trie
        t = trie()
        
        # Add a dummy node
        root = t.get_node(-1)
        
        # Insert first value into the trie
        t.insert(root, A[0])

        # Iterate over remaining values to find a maximum pair
        ans = 0

        for i in range(1, len(A)):

            # Find max xor for A[i] in the trie
            curr = t.find_xor(root, A[i])

            # Update ans
            ans = max(ans, curr)

            # Insert A[i] into the trie
            t.insert(root, A[i])
        
        return ans

class trie:

    def get_node(self, bit_val):
        return trieNode(bit_val)
    
    def insert(self, root, num):
        dummy = root
        for i in range(31, -1, -1):
            bit = 1 if (num & (1 << i)) else 0
#             print(bit)
            if bit not in dummy.children:
                dummy.children[bit] = self.get_node(bit)
            dummy = dummy.children[bit]
    
    def find_xor(self, root, num):
        ans = 0
        dummy = root
        for i in range(31, -1, -1):
            bit = 1 if (num & (1 << i)) else 0
            cbit = 1 ^ bit
            if cbit in dummy.children:
                ans = ans + (1 << i)
                dummy = dummy.children[cbit]
            else:
                dummy = dummy.children[bit]
        
        return ans

class trieNode:
    def __init__(self, bit):
        self.bit = bit
        self.children = dict()

# class Solution:
#     # @param A : list of integers
#     # @return an integer
#     def solve(self, A):

#         # Create 32 bit strings
#         for i in range(len(A)):
#             A[i] = [A[i], self.get_bit_string(A[i])]

#         # Create a trie
#         root = trieNode('dummy')

#         for pair in A:
#             bit = pair[1]
#             dummy = root
#             for b in bit:
#                 if b not in dummy.children:
#                     dummy.children[b] = trieNode(b)
                
#                 dummy = dummy.children[b]
            
#             dummy.isEnd = True
        
#         ans = 0
#         # Find largest complement for each number in A and return their maximum possible XOR.
#         for num in A:
#             s = num[1]
#             curr, p = 0, 31
#             dummy = root
#             for i in range(32):
#                 if s[i] == '1':
#                     # Find complement bit
#                     if '0' in dummy.children:
#                         dummy = dummy.children['0']
#                         curr = curr + (1 << p)
#                     else:
#                         dummy = dummy.children['1']
                        
#                 else:
#                     if '1' in dummy.children:
#                         curr = curr + (1 << p)
#                         dummy = dummy.children['1']
#                     else:
#                         dummy = dummy.children['0']
#                 p -= 1

#             ans = max(ans, curr)
        
#         return ans

#     def get_bit_string(self, num):
#         ans = ''

#         for i in range(32):
#             ans = str(num&1) + ans
#             num = num >> 1
#         return ans

# class trieNode:
#     def __init__(self, char):
#         self.char = char
#         isEnd = False
#         self.children = dict()