# 分3段處理, 小於newInterval.start, 重疊, 大於newInterval.end
# 因為intervals已排序, 所以第一段interval直接放進結果, 
# 接著確認有無interval.start <= newInterval.end的重疊段, 找出最小值與最大值做為新的interval插入
# 最後把interval.start > newInterval.end的區段直接放進結果

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start = newInterval[0]
        new_end = newInterval[1]
        new_intervals: List[List[int]] = []

        i=0
        n=len(intervals)

        #interval before new interval
        while i<n and intervals[i][1] < new_start:
            new_intervals.append(intervals[i])
            i+=1

        #overlapping
        while i<n and intervals[i][0] <= new_end:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])            
            i+=1

        new_intervals.append(newInterval)

        #interval after new interval
        while i<n:
            new_intervals.append(intervals[i])
            i+=1

        print(new_intervals)
        return new_intervals        
        

def main():
    solution = Solution()
    intervals = [[1,3],[6,9]]
    new_interval = [9,10]
    intervals = solution.insert(intervals, new_interval)

if __name__ == '__main__':
    main()