
class Solution:
    # @param A : list of list of chars
    def solveSudoku(self, A):
        
        A = [[ch for ch in arr] for arr in A]
        
        def is_valid(A,x,y,n):
            
            for i in range(9):
                if A[x][i] == n:
                    return False
                if A[i][y] == n:
                    return False
            
            grid_i = (x//3)*3
            grid_j = (y//3)*3
            
            for r_ in range(grid_i, grid_i+3):
                
                for j_ in range(grid_j, grid_j+3):
                    
                    if A[r_][j_] == n:
                        return False
            return True
        
        def backtrack(A,r,c):
            if c > 8:
                return backtrack(A,r+1,0)
            
            if r > 8:
#                 print(A)
                return True
            
            if A[r][c] != '.':
                return backtrack(A,r,c+1)
            
            for num in range(1, 10):
                if is_valid(A, r, c, str(num)):
                    A[r][c] = str(num)
                    
                    if backtrack(A,r,c+1):
                        return True   # This condition gets reached once all spots are correctly filled
                    else:
                        A[r][c] = '.' # Backtrack as function returned false as 1-9 did not pass constraints
            return False # Exhausted 1-9 as they did not satisfy condition
        
        b = backtrack(A,0,0)
#         print(b)
        A = [[''.join(arr)] for arr in A]
        print(A)
#         return [[''.join(arr)] for arr in A]