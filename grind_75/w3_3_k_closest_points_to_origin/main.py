# 第一種方式, 用Max heap的方式, 讓heap裡面放入k個元素, 並且照著大到小排列, 
# 當heap中元素數量大於k, 則把最大的元素pop
# heapq是min heap, 所以要從大到小排列要把距離取負數
# 適合n大k小

# 第二種方式, quick select, 找出小於pivot的k的數值, 
# 過程把points較pivot小的數值陸續往左搬, 小於pivot的數量>k則在左半邊找出適當的pivot, 反之則在右邊
# 直到pivot的index=k, 表示前面k個數值都是較小的
# best: O(n), worst(n^2), best avg.

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
        self.quick_select(points, k, 0, len(points)-1)
              
        return points[:k]

    def quick_select(self, points: List[List[int]], k: int, left: int, right: int):
        pivot_distance = points[left][0]**2 + points[left][1]**2

        if left >= right:
            return

        i = left+1
        for j in range(left+1, right):
            distance = points[j][0]**2 + points[j][1]**2
            if distance < pivot_distance:
                points[i], points[j] = points[j], points[i]
                i+=1

        points[left], points[i] = points[i], points[left]

        if i==k:
            return
        elif i < k:
            self.quick_select_solution(points, k, i+1, right)
        else:
            self.quick_select_solution(points, k, 0, right-1)

def main():
    points = [[6,10],[-3,3],[-2,5],[0,2]]
    k = 3
    solution = Solution()
    result = solution.kClosest(points, k)


if __name__ == "__main__":
    main()