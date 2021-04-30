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


# If there is a m*n matrix. it leads to 2^((m-1)*(n-1)) ways to finish
class Solution(object):
    def maxProductPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """