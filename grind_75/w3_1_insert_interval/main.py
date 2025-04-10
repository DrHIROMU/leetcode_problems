from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start = newInterval[0]
        new_end = newInterval[1]
        new_intervals: List[List[int]] = []
        new_interval: List[int] = [0,0]

        for interval in intervals:            
            start = interval[0]
            end = interval[1]
            

        return new_intervals        
        

def main():
    solution = Solution()
    intervals = [[1,3],[6,9]]
    new_interval = [2,5]
    intervals = solution.insert(intervals, new_interval)

if __name__ == '__main__':
    main()