# 1594. Maximum Non Negative Product in a Matrix
# You are given a rows x cols matrix grid. Initially,
# you are located at the top-left corner (0, 0),
# and in each step, you can only move right or down in the matrix.

# Among all possible paths starting from the top-left corner (0, 0)
# and ending in the bottom-right corner (rows - 1, cols - 1),
# find the path with the maximum non-negative product.
# The product of a path is the product of all integers
# in the grid cells visited along the path.

# Return the maximum non-negative product modulo 109 + 7.
# If the maximum product is negative return -1.

# Notice that the modulo is performed after getting the maximum product.


# 如果是r*c的矩陣, 會有C c取(r-1) + C c取1總可能性
# 此問題要用DP解, 否則效能太差

class Solution(object):
    def maxProductPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # n m 2
        MOD = pow(10, 9)+7
        n = len(grid)
        m = len(grid[0])
        minMax = []

        dp = [[[0] * 2 for i in range(m)] for j in range(n)]

        # max
        dp[0][0][0] = grid[0][0]
        # min
        dp[0][0][1] = grid[0][0]

        # init 1st col
        for i in range(1, n):
            dp[i][0][0] = (dp[i - 1][0][0] * grid[i][0])
            dp[i][0][1] = (dp[i - 1][0][1] * grid[i][0])

        # init 1st row
        for j in range(1, m):
            dp[0][j][0] = (dp[0][j - 1][0] * grid[0][j])
            dp[0][j][1] = (dp[0][j - 1][1] * grid[0][j])

        # calcualte matrix
        for i in range(1, n):
            for j in range(1, m):
                if(grid[i][j] > 0):
                    dp[i][j][0] = max(
                        dp[i - 1][j][0] * grid[i][j], dp[i][j - 1][0] * grid[i][j])
                    dp[i][j][1] = min(
                        dp[i - 1][j][1] * grid[i][j], dp[i][j - 1][1] * grid[i][j])
                elif(grid[i][j] < 0):
                    dp[i][j][0] = max(
                        dp[i - 1][j][1] * grid[i][j], dp[i][j - 1][1] * grid[i][j])
                    dp[i][j][1] = min(
                        dp[i - 1][j][0] * grid[i][j], dp[i][j - 1][0] * grid[i][j])
                else:
                    # grid[i][j] == 0
                    dp[i][j][0] = 0
                    dp[i][j][1] = 0

        res = dp[n - 1][m - 1][0]

        if res < 0:
            return -1

        res = res % MOD

        return res


# class Solution(object):
#     def maxProductPath(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """
#         position = {'x': 0, 'y': 0}
#         products = self.productsInPosition(grid, position)

#         # print(products)

#         maxProduct = max(products)

#         if maxProduct < 0:
#             return -1

#         maxProduct = maxProduct % (pow(10, 9)+7)
#         return maxProduct

#     def productsInPosition(self, grid, position):
#         products = []
#         x = position['x']
#         y = position['y']
#         rows = len(grid)
#         cols = len(grid[0])
#         number = grid[x][y]

#         if x+1 >= rows and y+1 >= cols:
#             products.append(grid[x][y])
#             return products

#         positionMoveRight = {'x': x, 'y': y+1}
#         positionMoveDown = {'x': x+1, 'y': y}
#         rightMaxProduct = None
#         downMaxProduct = None

#         if x+1 < rows:
#             downProducts = self.productsInPosition(grid, positionMoveDown)

#             for product in downProducts:
#                 products.append(number * product)

#         if y+1 < cols:
#             rightProducts = self.productsInPosition(grid, positionMoveRight)
#             for product in rightProducts:
#                 products.append(number * product)

#         filteredProducts = []
#         max = min = products[0]
#         for product in products:
#             if product > max and product >= 0:
#                 max = product
#             if product < min and product <= 0:
#                 min = product

#         filteredProducts.append(max)
#         filteredProducts.append(min)

#         print(filteredProducts)

#         return filteredProducts


s = Solution()
# grid = [[1, 2],
#         [-2, -3],
#         [1, 1]]

# grid = [[-1, 3, 0],
#         [3, -2, 3],
#         [-1, 1, -4]]

# grid = [[1,-1,2,1,-1,0,0,4,3,2,0,-2,-2],
# [-2,3,3,-1,-1,0,0,-2,4,-3,3,0,0],
# [-4,-1,-1,-2,2,-1,-2,-2,0,3,-1,-4,1],
# [-3,4,-3,0,-3,1,-3,1,4,4,-4,-4,-2],
# [3,-3,1,0,-1,-4,-4,-4,3,2,2,3,3],
# [2,-1,-1,-4,-3,-3,4,2,3,4,4,-4,0],
# [4,-1,2,-3,-1,-1,-3,-4,4,4,4,-3,-1],
# [-3,-4,4,-2,-1,2,3,-1,2,3,4,4,-4],
# [-3,-1,-2,1,1,-1,-3,-4,-3,1,-3,3,-4],
# [2,4,4,4,-3,-3,1,-1,3,4,-1,1,4],
# [2,-2,0,4,-1,0,-2,4,-4,0,0,2,-3],
# [1,1,-3,0,-4,-4,-4,-4,0,-1,-4,-1,0],
# [3,-1,-3,-3,-3,-2,-1,4,-1,-2,4,2,3]]


# grid = [[-1, -4, 2],
#         [4, 3, -1],
#         [2, -4, 4],
#         [1, -1, -4]]

grid = [[-1, -4, 2], [4, 3, -1], [2, -4, 4], [1, -1, -4]]
ans = s.maxProductPath(grid)
print(ans)
