# 要用Multi-source BFS才會快, 把所有0的座標放進queue, 
# 再對這些座標逐步往外擴展, 只要距離比較小就紀錄

from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:        
        rows, cols = len(mat), len(mat[0])
        dist = [[float('inf')] * cols for _ in range(rows)]
        queue = deque()
        
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    queue.append((r,c))

        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        while queue:
            r, c = queue.popleft()
            for direction_r, direction_c in directions:
                step_r, step_c = r+direction_r, c+direction_c
                if 0<=step_r<rows and 0<=step_c<cols:
                    if dist[step_r][step_c] > dist[r][c]+1:
                        dist[step_r][step_c] = dist[r][c]+1
                        queue.append((step_r,step_c))
        return dist

def main():
    mat = [[0,0,0],[0,1,0],[0,0,0]]
    solution = Solution()
    result = solution.updateMatrix(mat)

if __name__ == '__main__':
    main()