class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()
        for (i,n) in enumerate(nums):
            m = target - n
            if m in seen:
                return sorted([i, nums.index(m)])
            seen.add(n)
        return list()

