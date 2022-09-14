# Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Your goal is to reach the last index in the minimum number of jumps.
# You can assume that you can always reach the last index.

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [2,3,0,1,4]
# Output: 2

# Constraints:
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 105

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        res = 0
        last = 0
        cur = 0

        for i in range(0, len(nums)):
            if i > last:
                last = cur
                res += 1
            cur = max(cur, i+nums[i])
        
        return res

s = Solution()
print(s.jump([2,3,1,1,4]))