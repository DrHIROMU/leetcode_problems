#

from collections import deque
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest_points = []

        for point in points:
            x = point[0]
            y = point[1]
            sq_distance = x**2 + y**2
            if len(closest_points) < k:
                closest_points.append(point)
            else:
                max_distance = None
                max_distance_index = -1
                for i in range(len(closest_points) - 1, -1, -1):
                    closest_point = closest_points[i]
                    closest_distance = closest_point[0]**2+closest_point[1]**2
                    if max_distance is None or closest_distance > max_distance:
                        max_distance = closest_distance
                        max_distance_index = i
                if max_distance > sq_distance:
                    closest_points[max_distance_index] = point

        # print(closest_points)
        return closest_points

def main():
    points = [[6,10],[-3,3],[-2,5],[0,2]]
    k = 3
    solution = Solution()
    result = solution.kClosest(points, k)


if __name__ == "__main__":
    main()