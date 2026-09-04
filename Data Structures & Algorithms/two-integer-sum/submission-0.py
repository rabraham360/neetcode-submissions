class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_nums = {}
        prev_nums[nums[0]] = 0
        for i in range(1, len(nums)):
            new_target = target - nums[i]
            if(new_target in prev_nums):
                return [prev_nums[new_target],i]
            prev_nums[nums[i]] = i

        return [-1,-1]