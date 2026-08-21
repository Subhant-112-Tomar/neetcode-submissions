from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = Counter(nums)
        items = sorted(h.items(), key = lambda x : x[1], reverse = True)
        

        return [x[0] for x in items[:k]]
