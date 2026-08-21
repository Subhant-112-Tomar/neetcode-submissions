class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for i in range(len(nums)):
            if count.get(nums[i],0):
                return True
            count[nums[i]] = count.get(nums[i], 0) + 1
        return False