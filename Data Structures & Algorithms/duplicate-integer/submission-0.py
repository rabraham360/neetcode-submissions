class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = set()
        for i in range(0, len(nums)):
            if nums[i] in map:
                return True
            map.add(nums[i])
        return False