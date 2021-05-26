'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

'''
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
'''


class Solution:
    def twoSum(self , nums, target):
        for i_index,i_value in enumerate(nums):
            for j_index,j_value in enumerate(nums):
                if i_index == j_index and i_value == j_value:
                    pass
                else:
                    if i_value + j_value == target:
                        return [i_index,j_index] 

s = Solution()
print(s.twoSum([3,0,3],6))


'''
Success
Details :
Runtime: 7664 ms, faster than 5.01% of Python online submissions for Two Sum.
Memory Usage: 14.1 MB, less than 15.46% of Python online submissions for Two Sum.

'''
