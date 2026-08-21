from collections import Counter
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        if count.get(0, 0) > 1:
            return [0] * len(nums)
        prefix = [1] 
        for i in range(1, len(nums)):
            prefix.append(prefix[i-1] * nums[i-1])
        # print(prefix)

        suffix = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        # print(suffix)
 
        return [suffix[i] * prefix[i] for i in range(len(prefix))]