# 第一種方式, 用Max heap的方式, 讓heap裡面放入k個元素, 並且照著大到小排列, 
# 當heap中元素數量大於k, 則把最大的元素pop
# heapq是min heap, 所以要從大到小排列要把距離取負數
# 適合n大k小

# 第二種方式, quick select, 找出小於pivot的k的數值, best: O(n), worst(n^2), best avg.

import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k == len(points):
            return points
        
        # result = self.max_heap_solution(points, k)
        result = self.quick_select_solution(points, k)

        print(result)
        return result

    def max_heap_solution(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_heap = []
        for point in points:
            x = point[0]
            y = point[1]
            distance = -(x**2 + y**2)
            heapq.heappush(points_heap, (distance, point))
            if len(points_heap) > k:
                heapq.heappop(points_heap)    

        return [point for _, point in points_heap]

    def quick_select_solution(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest_points = []
        pivot_index = 0

        while len(closest_points) == k:
            pivot = points[pivot_index]
            pivot_distance = pivot[0]**2 + pivot[1]**2
            for i in range(1, len(points)):
                point = points[i]
                distance = point[0]**2 + point[1]**2
                if distance < pivot_distance:
                    closest_points.append(point)
                    
            if len(closest_points) == k:
                break

            closest_points = []
            pivot_index+=1

        return closest_points


def main():
    points = [[6,10],[-3,3],[-2,5],[0,2]]
    k = 3
    solution = Solution()
    result = solution.kClosest(points, k)


if __name__ == "__main__":
    main()