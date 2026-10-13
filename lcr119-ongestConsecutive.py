'''
LCR 119. 最长连续序列
中等

给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

示例 1：
输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。

示例 2：
输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9


提示：
0 <= nums.length <= 104
-109 <= nums[i] <= 109

进阶：可以设计并实现时间复杂度为 O(n) 的解决方案吗？
'''




from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for x in num_set:
            if x - 1 in num_set:
                continue              # x 不是起点，跳过
            length = 1
            while x + length in num_set:
                length += 1
            longest = max(longest, length)
        return longest

if __name__ == '__main__':
    solution = Solution()
    nums = [0,3,7,2,5,8,4,6,0,1]
    print(solution.longestConsecutive(nums))