'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

你可以按任意顺序返回答案。

示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

示例 2：
输入：nums = [3,2,4], target = 6
输出：[1,2]

示例 3：
输入：nums = [3,3], target = 6
输出：[0,1]
'''
from typing import List
class Solution:
    # 方案一：
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(len(nums)):
    #         for j in range(len(nums)):
    #             if nums[i] + nums[j] == target and i != j:
    #                 return [i, j]
    # 方案二：哈希表
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,num in enumerate(nums):
            if target-num in seen:
                return [seen[target-num],i]
            seen[num] =i



solution = Solution()
print(solution.twoSum([2,7,11,15], 9))
print(solution.twoSum([3,2,4], 6))
