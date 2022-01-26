'''class Solution:
	# @param A : integer
	# @param B : list of integers
	# @param C : list of integers
	# @return an integer
	def solve(self, A, B, C):

        # Do a topological sort using BFS (modified Kahn's algorithm) and if valid, return 1 else 0

        # Stack to store 0 degree nodes
        st = []

        # Build adjacency list and in degree node array
        adj = [[] for i in range(A + 1)]
        in_ = [0 for i in range(A + 1)]

        for i in range(len(B)):

            adj[B[i]].append(C[i])

            in_[C[i]] += 1
        
        # Find non dependent courses, i.e. 0 in degrees
        for i in range(1, len(in_)):

            if in_[i] == 0:
                st.append(i)
        
        # Now loop through all until stack is not empty
        # Keep a count of elements being added to the topological order
        ct = 0

        while st:

            top = st.pop()
            ct += 1
            # Iterate top's adjacency list and decrement their indegrees by 1, append to stack if they become 0
            for nb in adj[top]:

                in_[nb] -= 1

                if in_[nb] == 0:
                    st.append(nb)
        
        # Check if ct is equal to the number of nodes, if yes, then return 1 else 0
        if ct == A:
            return 1
        
        return 0

    # TC: O(V + E), SC: O(V + E)'''

class Solution:
	# @param A : integer
	# @param B : list of integers
	# @param C : list of integers
	# @return an integer
	def solve(self, A, B, C):

        # Do a topological sort using BFS (modified Kahn's algorithm) and if valid, return 1 else 0

        # Stack to store 0 degree nodes
        st = []

        # Build adjacency list and in degree node array
        adj = [[] for i in range(A + 1)]
        in_ = [0 for i in range(A + 1)]

        for i in range(len(B)):

            adj[B[i]].append(C[i])

            in_[C[i]] += 1
        
        # Find non dependent courses, i.e. 0 in degrees
        for i in range(1, len(in_)):

            if in_[i] == 0:
                st.append(i)
        
        # Now loop through all until stack is not empty
        # Keep a count of elements being added to the topological order
        ct = 0

        while st:

            top = st.pop()
            ct += 1
            # Iterate top's adjacency list and decrement their indegrees by 1, append to stack if they become 0
            for nb in adj[top]:

                in_[nb] -= 1

                if in_[nb] == 0:
                    st.append(nb)
        
        # Check if ct is equal to the number of nodes, if yes, then return 1 else 0
        if ct == A:
            return 1
        
        return 0

    # TC: O(V + E), SC: O(V + E)