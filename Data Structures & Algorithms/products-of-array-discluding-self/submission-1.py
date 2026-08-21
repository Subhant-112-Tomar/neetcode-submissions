from collections import Counter
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        count = Counter(nums)
        for i in range(len(nums)):
            prod = 1
            for key, freq in count.items():
                if key == nums[i]:
                    prod *= key ** (freq - 1)
                else:
                    prod *= key ** freq
            output.append(prod)
        return output
