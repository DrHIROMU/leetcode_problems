# 先排序, 後利用2 pointer找出所有與第i個數字相加為0的兩個數字
# nums[i]如果與nums[i-1]重複, 則跳過, 其中因為nums有先排序, 所以只需要比對當前的數字與前數字是否相同
# 當找到總和為零的三個數字後left+1, right-1, 遇到重複繼續走
 
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)-2):
            if nums[i]>0:
                break
    
            if i>0 and nums[i]==nums[i-1]:
                continue

            left, right = i+1, len(nums)-1

            while left<right:
                total = nums[i]+nums[left]+nums[right]

                if total==0:
                    result.append([nums[i], nums[left], nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                elif total<0:
                    left+=1
                else:
                    right-=1
        return result

def main():
    nums = [-1,0,1,2,-1,-4]
    solution = Solution()
    result = solution.threeSum(nums)
    print(result)

if __name__ == '__main__':
    main()