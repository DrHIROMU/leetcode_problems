# 走到第i個數字, 比較第i個數字有沒有比前面加總大, 如果有, 以i當新的起始, 如果沒有, 繼續加總
# 比較目前加總與目前最大的加總比起來哪個大

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        max_so_far = nums[0]
        sum_so_far = nums[0]
        for i in range(1, len(nums)):
            sum_so_far += nums[i]
            if nums[i] > sum_so_far:
                sum_so_far = nums[i]

            if sum_so_far > max_so_far:
                max_so_far = sum_so_far

        return max_so_far

def main():
    solution = Solution()
    nums = [5,4,-1,7,8]
    sum = solution.maxSubArray(nums)
    print(sum)

if __name__ == '__main__':
    main()