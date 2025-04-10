from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, target)
        
    def binary_search(self, nums: List[int], target: int):
        if nums is None or len(nums) == 0:
            return -1       

        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1            

def main():
    solution = Solution()
    nums = [-1,0,3,5,9,12]
    target = 3
    result = solution.search(nums, target)
    print(result)

if __name__ == '__main__':
    main() 