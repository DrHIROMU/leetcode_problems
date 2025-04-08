# 要用Multi-source BFS才會快, 把所有0作為起點放進queue, 逐步往外擴展

from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:        
        rows, cols = len(mat), len(mat[0])
        dist = [[float('inf')] * cols for _ in range(rows)]

        num_rows = len(mat)
        num_cols = len(mat[0])
        nearest_zero_map = [[-1 for _ in range(num_cols)] for _ in range(num_rows)]
        non_zero_positions = []
        zero_positions = []

        for r_index in range(num_rows):
            for c_index in range(num_cols):
                cell = mat[r_index][c_index]
                if cell == 0:
                    nearest_zero_map[r_index][c_index] = 0
                    zero_positions.append([r_index, c_index])
                    if r_index > 0:
                        if mat[r_index-1][c_index] != 0:
                            nearest_zero_map[r_index-1][c_index] = 1                            
                    if r_index < num_rows-1:
                        if mat[r_index+1][c_index] != 0:
                            nearest_zero_map[r_index+1][c_index] = 1                            
                    if c_index > 0:
                        if mat[r_index][c_index-1] != 0:
                            nearest_zero_map[r_index][c_index-1] = 1                            
                    if c_index < num_cols-1:
                        if mat[r_index][c_index+1] != 0:
                            nearest_zero_map[r_index][c_index+1] = 1                           

                else:
                    if nearest_zero_map[r_index][c_index] == 1:
                        continue
                    if r_index > 0:
                        if mat[r_index-1][c_index] == 0:
                            nearest_zero_map[r_index][c_index] = 1
                            continue
                    if r_index < num_rows-1:
                        if mat[r_index+1][c_index] == 0:
                            nearest_zero_map[r_index][c_index] = 1
                            continue
                    if c_index > 0:
                        if mat[r_index][c_index-1] == 0:
                            nearest_zero_map[r_index][c_index] = 1
                            continue
                    if c_index < num_cols-1:
                        if mat[r_index][c_index+1] == 0:
                            nearest_zero_map[r_index][c_index] = 1
                            continue
                    non_zero_positions.append([r_index, c_index])                                      
        
        for zero in zero_positions:
            zero_r = zero[0]
            zero_c = zero[1]
            for non_zero in non_zero_positions:
                non_zero_r = non_zero[0]
                non_zero_c = non_zero[1]
                distance = abs(non_zero_r-zero_r)+abs(non_zero_c-zero_c)
                non_zero_value = nearest_zero_map[non_zero_r][non_zero_c]
                if non_zero_value == -1 or non_zero_value > distance:
                    nearest_zero_map[non_zero_r][non_zero_c] = distance
        
        return nearest_zero_map

def main():
    mat = [[0,0,0],[0,1,0],[0,0,0]]
    solution = Solution()
    result = solution.updateMatrix(mat)

if __name__ == '__main__':
    main()