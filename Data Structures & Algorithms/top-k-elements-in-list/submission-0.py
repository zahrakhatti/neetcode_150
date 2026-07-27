from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        count_sorted = sorted(count, key = lambda n: count[n], reverse = True)
        return count_sorted[0:k]