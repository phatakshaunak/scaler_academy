
# Python3 Program to print sum of all  
# the elements of a binary tree  
  
# Binary Tree Node  
  
""" utility that allocates a new Node  
with the given key """
class newNode:  
  
    # Construct to create a new node  
    def __init__(self, key):  
        self.key = key 
        self.left = None
        self.right = None
        self.depth = None

def sum_(root):
    
    if not root:
        return 0
    
    return root.key + sum_(root.left) + sum_(root.right)

def max_val(root):
    if not root:
        return float('-inf')
    
    return max(root.key, max_val(root.left), max_val(root.right))

def min_val(root):
    if not root:
        return float('inf')
    
    return min(root.key, min_val(root.left), min_val(root.right))

def ht_bt(root):
    if not root:
        return -1
    
    return 1 + max(ht_bt(root.left), ht_bt(root.right))

def depth(root, d, max_depth):
    if not root:
        return
    root.depth = d
    max_depth[0] = max(d, max_depth[0])
    depth(root.left, d + 1, max_depth)
    depth(root.right, d + 1, max_depth)

root = newNode(1)
root.left = newNode(2)  
root.right = newNode(3)  
root.left.left = newNode(4)  
root.left.right = newNode(5)  
root.right.left = newNode(6)  
root.right.right = newNode(7)  
root.right.left.right = newNode(8)

print('Sum of all nodes with post order traversal: ', sum_(root))
print('Maximum of all nodes with post order traversal: ', max_val(root))
print('Minimum of all nodes with post order traversal: ', min_val(root))
print('Height of the binary tree: ', ht_bt(root))
max_depth = [0]
print('Setting depth of all nodes of the tree', depth(root, 0, max_depth))
print('Maximum depth of the tree: ', max_depth[0])
# # Function to find sum of all the element  
# def addBT(root):  
#     if (root == None): 
#         return 0
#     return (root.key + addBT(root.left) + 
#                        addBT(root.right))  
  
# # Driver Code  
# if __name__ == '__main__': 
#     root = newNode(1)  
#     root.left = newNode(2)  
#     root.right = newNode(3)  
#     root.left.left = newNode(4)  
#     root.left.right = newNode(5)  
#     root.right.left = newNode(6)  
#     root.right.right = newNode(7)  
#     root.right.left.right = newNode(8)  
  
#     sum = addBT(root)  
  
#     print("Sum of all the nodes is:", sum) 
  
# # This code is contributed by 
# # Shubham Singh(SHUBHAMSINGH10) 