class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):

        # Sort in increasing order by height and decreasing order by width if there is a tie in height
        # Then apply LIS for the width and return maximum value

        # A = sorted(A, key = lambda pair: [pair[0], -pair[1]])

        # Another way is to sort one dimension 
        #and simply check if the left height dimensions are smaller than current height during the LIS process on 
        # width
        
        # A.sort()
        # ans = 1

        # dp = [1 for i in range(len(A))]
        # # dp[0] = 1

        # for i in range(1, len(A)):

        #     curr = 1

        #     for j in range(i):

        #         if A[j][1] < A[i][1] and A[i][0] > A[j][0]:
        #             curr = max(curr, 1 + dp[j])
            
        #     dp[i] = curr
        #     ans = max(ans, dp[i])
        
        # return ans

        return self.rus_dolls_custom_sort(A)

    def rus_dolls(self, A):

        A.sort(key = lambda x: x[0])
        
        n = len(A)
        
        dp = [1 for i in range(n)]
        
        ans = 1
        
        for i in range(1, n):
            
            for j in range(i):
                
                if (A[j][1] < A[i][1]) and (A[i][0] != A[j][0]):
                    
                    if dp[i] < 1 + dp[j]:
                        dp[i] = 1 + dp[j]

            if ans < dp[i]:
                ans = dp[i]
        
        return ans
    
    def rus_dolls_custom_sort(self, A):
        
        n = len(A)

        dp = [1 for i in range(n)]
        
        ans = 1
        
        self.merge_sort(A, 0, n - 1)

        for i in range(1, n):

            for j in range(i):

                if A[j][1] < A[i][1]:
                    
                    if dp[i] < 1 + dp[j]:
                        dp[i] = 1 + dp[j]
            
            if ans < dp[i]:
                ans = dp[i]
        
        return ans
    
    def merge_sort(self, A, i, j):
    
        if i == j:
            return

        mid = i + (j - i) // 2

        self.merge_sort(A, i, mid)

        self.merge_sort(A, mid + 1, j)

        self.custom_merge(A, i, j)

    def custom_merge(self, A, i, j):
        
        tmp = [0 for i in range(j - i + 1)]
        
        mid = i + (j - i) // 2
        
        x, y = i, mid + 1
        
        z = 0
        while x <= mid and y <= j:
            
            if A[x][0] < A[y][0]:
                tmp[z] = A[x]
                x += 1
            
            elif A[x][0] > A[y][0]:
                tmp[z] = A[y]
                y += 1
            
            else:
                if A[x][1] >= A[y][1]:
                    tmp[z] = A[x]
                    x += 1
                
                else:
                    tmp[z] = A[y]
                    y += 1
            
            z += 1
        
        while x <= mid:
            tmp[z] = A[x]
            x += 1
            z += 1
        
        while y <= j:
            tmp[z] = A[y]
            y += 1
            z += 1
        
        for idx in range(i, j + 1):
            
            A[idx] = tmp[idx - i]
        
    # TC O(N^2), SC O(N)