def rod_cutting(length, price, i, j, dp):
    
    if j == 0 or i >= len(length):
        return 0
    
    if dp[i][j] == -1:
        
        cut = float('-inf')
        
        skip = rod_cutting(length, price, i + 1, j, dp)
        
        if j - length[i] >= 0:
            cut = price[i] + rod_cutting(length, price, i, j - length[i], dp)
        
        dp[i][j] = max(skip, cut)
    
    return dp[i][j]

length = [1, 2, 3, 4, 5, 6, 7, 8]
price = [1, 5, 8, 9, 10, 17, 17, 20]

# length = [1, 2, 3, 4, 5]
# price = [2, 5, 7, 8, 0]

dp = [[-1 for i in range(length[-1] + 1)] for j in range(len(length))]

print(rod_cutting(length, price, 0, length[-1], dp))