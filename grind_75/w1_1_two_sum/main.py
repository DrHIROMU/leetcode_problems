

class solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        diff = {}
        for index, num in enumerate(nums):
            if num in diff:
                return [diff[num], index]
            diff[target - num] = index        
        return []

def main():
    nums = [2, 7, 11, 15]
    target = 9
    s = solution()
    print(s.twoSum(nums, target))

if __name__ == '__main__':
    main()