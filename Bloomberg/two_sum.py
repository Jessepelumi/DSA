# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            # subtract current loop value to get a potential match
            x = target - nums[i]

            # x must be in nums array and must not be a reused index
            if x in nums and nums.index(x) != i:
                return [i, nums.index(x)]
            

solution = Solution()

# test cases
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