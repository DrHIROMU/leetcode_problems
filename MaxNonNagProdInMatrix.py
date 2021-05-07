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
class Solution(object):
    def maxProductPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        position = {'x':0, 'y':0}
        products = self.productsInPosition(grid, position)

        # print(products)

        maxProduct = max(products)

        if maxProduct < 0:
            return -1

        maxProduct = maxProduct % (pow(10,9)+7)
        return maxProduct

    def productsInPosition(self, grid, position):        
        products = []
        x = position['x']
        y = position['y']
        rows = len(grid)
        cols = len(grid[0])
        number = grid[x][y]

        if x+1 >= rows and y+1>=cols:        
            products.append(grid[x][y])
            return products

        positionMoveRight = {'x': x, 'y': y+1}
        positionMoveDown = {'x': x+1, 'y': y}  
        rightMaxProduct = None
        downMaxProduct = None

        if x+1 < rows: 
            downProducts = self.productsInPosition(grid, positionMoveDown)
            max,min = 0
            for product in downProducts:
                if product > max:
                    max = product
                if 
                products.append(number * product)

        if y+1 < cols:
            rightProducts = self.productsInPosition(grid, positionMoveRight)
            for product in rightProducts:
                products.append(number * product)

        return products

s = Solution()
# grid = [[1,2],
#         [-2,-3]]
grid = [[-1,-4,2],
        [4,3,-1],
        [2,-4,4],
        [1,-1,-4]]
# grid = [[-1,-2,-3],
#         [-2,-3,-3],
#         [-3,-3,-2]]
ans = s.maxProductPath(grid)
print(ans)