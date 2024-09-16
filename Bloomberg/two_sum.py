# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            x = target - nums[i]
            if x in nums and x != nums[i]:
                return [i, nums.index(x)]
            

solution = Solution()

class CaseOne:
    nums = [2, 7, 11, 15]
    target = 9

class CaseTwo:
    nums = [3, 2, 4]
    target = 6

caseOne = CaseOne()
caseTwo = CaseTwo()

resultOne = solution.twoSum(nums=caseOne.nums, target=caseOne.target)
resultTwo = solution.twoSum(nums=caseTwo.nums, target=caseTwo.target)
print(resultOne, resultTwo)